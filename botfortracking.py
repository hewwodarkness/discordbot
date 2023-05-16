import discord
from discord.ext import commands
from discord import Intents
from discord import utils
import json
import asyncio
import requests
import datetime

from tokenbotfortracking import TOKEN

from tokendiscord import client_id
from tokendiscord import client_secret

from ossapi import Ossapi
api = Ossapi(client_id, client_secret)

intents = Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
client = discord.Client(intents=intents)
tracked_users = []

json_file = 'tracked_users.json'

# Load tracked_users from the JSON file


async def osu_score_check():
    api = Ossapi(client_id, client_secret)
    previous_activity = {}
    
    for entry in tracked_users:
        channel_id = entry["channel_id"]
        nickname_id = entry["user_id"]

        channel = client.get_channel(channel_id)
        if channel is None:
            print(f"Invalid channel ID: {channel_id}")
            continue

        try:
            response = requests.post(
                "https://osu.ppy.sh/oauth/token",
                data={
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": "client_credentials",
                    "scope": "public",
                },
            )

            access_token = response.json()["access_token"]

            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "x-api-version": str(20220707),
            }

            while True:
                try:
                    response = requests.get(
                        f"https://osu.ppy.sh/api/v2/users/{nickname_id}/osu", headers=headers)

                    if response.ok:
                        user_data = response.json()
                        statistics = user_data["statistics"]
                        username = user_data["username"]
                        avatar_url = user_data["avatar_url"]

                    recent_activity = api.user_scores(
                        user_id=nickname_id, limit=1, offset=0, type='recent')

                    if recent_activity:
                        recent_activity_id = recent_activity[0].id
                        if nickname_id not in previous_activity or recent_activity_id != previous_activity[nickname_id].id:
                            usernameosu = api.user(
                                nickname_id, mode="osu").username
                            embed = discord.Embed(color=0x00ff00)

                            embed.set_thumbnail(url=avatar_url)
                            embed.set_author(
                                name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                                    user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"),
                                url=f"https://osu.ppy.sh/users/{user_data['id']}",
                                icon_url=avatar_url)
                            embed.add_field(
                                name='', value=f"**[{recent_activity[0].beatmapset.artist} - {recent_activity[0].beatmapset.title} [{recent_activity[0].beatmap.version}]]({recent_activity[0].beatmap.url})**", inline=False)

                            accuracy_str = '{:.2%}'.format(
                                recent_activity[0].accuracy)

                            created_at = recent_activity[0].created_at
                            timestamp = int(created_at.timestamp())
                            discord_time = datetime.fromtimestamp(timestamp)
                            discord_time_str = discord_time.strftime('<t:%s:R>' % timestamp)
                            embed.add_field(
                                name="",
                                value=f"✦ +{recent_activity[0].mods} ✦ {accuracy_str} ✦ x{recent_activity[0].max_combo} ✦ {discord_time_str}",
                                inline=False)

                            if recent_activity[0].pp is None:
                                embed.add_field(
                                    name="", value=f"✦ {recent_activity[0].rank.name} rank ✦ 0 pp", inline=False)
                            else:
                                embed.add_field(
                                    name="", value=f"✦ {recent_activity[0].rank.name} rank ✦ {recent_activity[0].pp}pp", inline=False)

                            thumbnail_url = f'https://b.ppy.sh/thumb/{recent_activity[0].beatmapset.id}l.jpg'
                            embed.set_thumbnail(url=thumbnail_url)
                            beatmap_length = recent_activity[0].beatmap.total_length
                            minutes, seconds = divmod(beatmap_length, 60)
                            beatmap_length_str = f"{minutes:02d}:{seconds:02d}"
                            embed.add_field(
                                name='Beatmap Information',
                                value=f"{beatmap_length_str} ~ CS{recent_activity[0].beatmap.cs} AR{recent_activity[0].beatmap.ar} ~ BPM{recent_activity[0].beatmap.bpm} ~ {recent_activity[0].beatmap.difficulty_rating}★")

                            mapperusername = api.user(
                                recent_activity[0].beatmap.user_id, mode="osu").username
                            mapperuseravatarurl = api.user(
                                recent_activity[0].beatmap.user_id, mode="osu").avatar_url

                            last_updated1 = recent_activity[0].beatmap.last_updated
                            timestamp1 = int(last_updated1.timestamp())
                            discord_time1 = datetime.fromtimestamp(timestamp1)
                            embed.set_footer(
                                text=f"Mapped by {mapperusername} ✦ Ranked on {discord_time1}",
                                icon_url=mapperuseravatarurl)

                            await channel.send(embed=embed)

                            previous_activity[nickname_id] = recent_activity[0]
                    print("SCORE")
                    print(nickname_id)
                    print("SCORE checked")
                except IndexError:
                    print(f"Recent activity is empty for user ID {nickname_id}. Skipping to next iteration.")

                await asyncio.sleep(20)
        except Exception as e:
            print(f"An error occurred: {e}")



def load_tracked_users():
    global tracked_users
    try:
        with open(json_file, 'r') as file:
            tracked_data = json.load(file)
    except FileNotFoundError:
        print("JSON file not found. Starting with an empty list.")

# Save tracked_users to the JSON file


def save_tracked_users():
    tracked_data = [{'channel_id': channel_id, 'user_id': nickname_id}
                    for channel_id, nickname_id in tracked_users]

    try:
        with open(json_file, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.extend(tracked_data)

    with open(json_file, 'w') as file:
        json.dump(existing_data, file)


@bot.event
async def on_ready():
    print('Bot is ready.')
    load_tracked_users()


@bot.event
async def on_message(message):
    if message.content.startswith('!tracking'):
        await message.channel.send("Please specify the channel you want to use for tracking.")

        while True:
            channel_response = await bot.wait_for('message', check=lambda m: m.author == message.author)

            try:
                # Convert channel ID to integer
                channel_id = int(channel_response.content.strip("<>#"))
                channel = utils.get(bot.get_all_channels(), id=channel_id)
                if channel is None:
                    raise ValueError
                break
            except ValueError:
                await message.channel.send("Invalid channel ID. Please provide a valid channel ID.")

        await message.channel.send("Please enter the nickname you want to track.")
        nickname_response = await bot.wait_for('message', check=lambda m: m.author == message.author)

        channel_id = int(channel_response.content.strip("<>#")
                         )  # Convert channel ID to integer

        nickname = nickname_response.content
        nickname_id = api.user(nickname).id

        tracked_users.append((channel_id, nickname_id))

        await message.channel.send(f"Tracking enabled for channel {channel_response.content}(id: {channel_id}) and name(s) {nickname_response.content}(id: {nickname_id}).")
        save_tracked_users()
        load_tracked_users()

    await bot.process_commands(message)


@bot.command()
async def tracking(ctx):
    # Add the existing osu_score_check() code here
    # Modify it to use the channel ID and names obtained from the tracking setup

    await ctx.send("Osu! score check in progress...")
    client.loop.create_task(osu_score_check())


bot.run(TOKEN)
