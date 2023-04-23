import discord
import asyncio
from datetime import datetime, date
import threading
import win32con
import win32gui
import pystray
from PIL import Image
import os
from tokendiscord import TOKEN
from tokendiscord import client_id
from tokendiscord import client_secret
import discord
import random
import requests
from rule34Py import rule34Py
import io
import aiohttp

r34Py = rule34Py()
user_ids = ["9217626","2927048", "18802053", "10394538", "7587763", "blednak", "Virgo", "SS is hard", "P e n g u", "Inoculum", "rikka", "wimpn", "Sure", "Hammer", "noercy", "worldchallenge", "10030328", "zalaria", "sleepteiner", "551549"]
PICTURE_FOLDER = "C:/Users/Эльф/Desktop/memess"
REACTION_EMOJIS = ['🛐','♿','🅿️','🇷','🇴']

def on_quit():
    print("Exiting...")
    os._exit(0)

def on_open(icon, item):
    hwnd = win32gui.FindWindow(None, "Bot")
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    style &= ~(win32con.WS_MINIMIZE | win32con.WS_DISABLED)
    style |= win32con.WS_EX_TOOLWINDOW
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

def create_tray_icon():
    # Create a tray icon
    image = Image.open("2.png")
    menu = pystray.Menu(pystray.MenuItem("Open", on_open), pystray.MenuItem("Exit", on_quit))
    icon = pystray.Icon("My App", image, "My App", menu)

    icon.run()

if __name__ == '__main__':
    # Start the tray icon in a separate thread

    # win32gui.SetWindowText(win32gui.GetForegroundWindow(), "Bot")
    # threading.Thread(target=create_tray_icon).start()
    # win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

    # Start the Discord bot in the main thread
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    async def my_background_task():
        await client.wait_until_ready()

        @client.event
        async def on_message(message):
            if message.author.id == 119502464398524418:
                for emoji in REACTION_EMOJIS:
                    await message.add_reaction(emoji)

            emote = client.get_emoji(1098984439083708436)
            if message.author.id == 975108471307526144:
                await message.add_reaction(emote)

            await check_for_virgo(message)
            await check_for_cygan(message)
            await on_pic(message)
            await ss_count(message)
            await on_based(message)

        async def check_for_virgo(message):
            if "я фанатка вірго" in message.content.lower() and message.author != client.user:
                response = "я фанатка вірго"
                await message.reply(response)

        async def check_for_cygan(message):
            if "циган" in message.content.lower():
                with open("cygan.jpg", "rb") as f:
                    picture = discord.File(f)
                    await message.reply(file=picture)

        async def on_pic(message):
            if message.content.startswith("!sendpicture"):
                files = os.listdir(PICTURE_FOLDER)
                random_file = random.choice(files)
                file_path = os.path.join(PICTURE_FOLDER, random_file)
                with open(file_path, "rb") as f:
                    picture = discord.File(f)
                    await message.reply(file=picture)

        async def on_based(message):
            if message.content.startswith("!picsecret"):
                words = message.content.split()
                if len(words) < 2:
                    response = "Please provide a tag."
                else:
                    tag = words[1]
                    bazatest = r34Py.random_post([tag])
                    url = bazatest.image # Replace with your image URL
                    response = requests.get(url)

                    with open('image.jpg', 'wb') as f:
                        f.write(response.content)

                    with open('image.jpg', 'rb') as f:
                        await message.reply(file=discord.File(f))

        async def ss_count(message):
            user_id = "5249196"
            grant_type = "client_credentials"
            scope = "public"
            # Send a request to the authorization server to obtain an access token
            response = requests.post(
                "https://osu.ppy.sh/oauth/token",
                data={
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "scope": scope,
                },
            )

            # Parse the response JSON to extract the access token
            access_token = response.json()["access_token"]
            # print(access_token)

            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "x-api-version": str(20220707),
            }
            if message.content.startswith("!ss"):
                words = message.content.split()
                if len(words) < 2:
                    response = "Please provide a user ID."
                else:
                    user_id = words[1]
                    response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
                    if response.ok:
                        user_data = response.json()
                        grade_counts = user_data["statistics"]['grade_counts']['ss']
                        grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                        username = user_data["username"]
                        sum = grade_counts + grade_counts1
                        response = f'The user with ID {username} has {sum} SS scores.'
                    else:
                        response = f'Request failed with status {response.status_code} and message: {response.text}'
                await message.reply(response)
    

    # async def osu_check():
    #     prev_grade_counts = {}
    #     prev_grade_counts1 = {}
    #     prev_global_rank = {}
    #     prev_pp = {}
    #     prev_ranked_score = {}
    #     prev_total_hits = {}
    #     channel = client.get_channel(1099409748543148142)

    #     grant_type = "client_credentials"
    #     scope = "public"

    #     while True:
    #         # Obtain access token
    #         response = requests.post(
    #             "https://osu.ppy.sh/oauth/token",
    #             data={
    #                 "client_id": client_id,
    #                 "client_secret": client_secret,
    #                 "grant_type": grant_type,
    #                 "scope": scope,
    #             },
    #         )
    #         access_token = response.json()["access_token"]

    #         headers = {
    #             "Authorization": f"Bearer {access_token}",
    #             "Content-Type": "application/json",
    #             "Accept": "application/json",
    #             "x-api-version": str(20220707),
    #         }

    #         for user_id in user_ids:
    #             # Check grade counts
    #             response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
    #             if response.ok:
    #                 user_data = response.json()
    #                 grade_counts = user_data["statistics"]['grade_counts']['ss']
    #                 grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
    #                 sum = grade_counts + grade_counts1
    #                 global_rank = user_data["statistics"]['global_rank']
    #                 pp = user_data["statistics"]['pp']
    #                 ranked_score = user_data["statistics"]['ranked_score']
    #                 total_hits = user_data["statistics"]['total_hits']
    #                 username = user_data["username"]

    #                 # Check if the values changed since the last call
    #                 if user_id in prev_grade_counts and prev_grade_counts[user_id] != grade_counts:
    #                     await channel.send(f"The ss count for user {username} changed from {prev_grade_counts[user_id]} to {grade_counts}")
    #                 if user_id in prev_grade_counts1 and prev_grade_counts1[user_id] != grade_counts1:
    #                     await channel.send(f"The ssh count for user {username} changed from {prev_grade_counts1[user_id]} to {grade_counts1}")

    #                 if user_id in prev_grade_counts or user_id in prev_grade_counts1:
    #                     if prev_grade_counts.get(user_id) != grade_counts or prev_grade_counts1.get(user_id) != grade_counts1:
    #                         await channel.send(f"The ss count for user {username} changed from {prev_grade_counts.get(user_id)} to {grade_counts}, and the ssh count changed from {prev_grade_counts1.get(user_id, 0)} to {grade_counts1}")

    #                 if user_id in prev_global_rank and prev_global_rank[user_id] != global_rank:
    #                     await channel.send(f"The global rank for user {username} changed from {prev_global_rank[user_id]} to {global_rank}")

    #                 if user_id in prev_pp and prev_pp[user_id] != pp:
    #                     await channel.send(f"The PP for user {username} changed from {prev_pp[user_id]} to {pp}")

    #                 if user_id in prev_ranked_score and prev_ranked_score[user_id] != ranked_score:
    #                     await channel.send(f"The ranked score for user {username} changed from {prev_ranked_score[user_id]} to {ranked_score}")

    #                 if user_id in prev_total_hits and prev_total_hits[user_id] != total_hits:
    #                     await channel.send(f"The total hits for user {username} changed from {prev_total_hits[user_id]} to {total_hits}")

    #                 # Update the previous values
    #                 prev_grade_counts[user_id] = grade_counts
    #                 prev_grade_counts1[user_id] = grade_counts1
    #                 prev_global_rank[user_id] = global_rank
    #                 prev_pp[user_id] = pp
    #                 prev_ranked_score[user_id] = ranked_score
    #                 prev_total_hits[user_id] = total_hits

    #         await asyncio.sleep(10)
    async def osu_check():
        prev_statistics = {}
        prev_grade_counts = {}
        prev_grade_counts1 = {}
        channel = client.get_channel(1099409748543148142)

        grant_type = "client_credentials"
        scope = "public"

        while True:
            # Obtain access token
            response = requests.post(
                "https://osu.ppy.sh/oauth/token",
                data={
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "scope": scope,
                },
            )
            access_token = response.json()["access_token"]

            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "x-api-version": str(20220707),
            }

            for user_id in user_ids:
                # Check statistics
                response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
                if response.ok:
                    user_data = response.json()
                    statistics = user_data["statistics"]
                    username = user_data["username"]

                    # Check if the values changed since the last call
                    if user_id in prev_statistics:
                        prev_stats = prev_statistics[user_id]
                        # if prev_stats['grade_counts']['ss'] != statistics['grade_counts']['ss'] or prev_stats['grade_counts']['ssh'] != statistics['grade_counts']['ssh']:
                        #     grade_counts = statistics['grade_counts']['ss'] + statistics['grade_counts']['ssh']
                        #     await channel.send(f"The grade counts for user {username} changed from {prev_stats['grade_counts']['ss']}/{prev_stats['grade_counts']['ssh']} to {statistics['grade_counts']['ss']}/{statistics['grade_counts']['ssh']}")
                        # if user_id in prev_grade_counts and prev_grade_counts[user_id] != statistics['grade_counts']['ss']:
                        #   print(f"The ss count for user {username} changed from {prev_grade_counts[user_id]} to {statistics['grade_counts']['ss']}")
                        #   await channel.send(f"The ss count for user {username} changed from {prev_grade_counts[user_id]} to {statistics['grade_counts']['ss']}")
                            
                        # if user_id in prev_grade_counts1 and prev_grade_counts1[user_id] != statistics['grade_counts']['ssh']:
                        #   print(f"The ssh count for user {username} changed from {prev_grade_counts1[user_id]} to {statistics['grade_counts']['ssh']}")
                        #   await channel.send(f"The ssh count for user {username} changed from {prev_grade_counts1[user_id]} to {statistics['grade_counts']['ssh']}")

                        if user_id in prev_grade_counts and (prev_grade_counts[user_id] != statistics['grade_counts']['ss'] or user_id in prev_grade_counts1 and prev_grade_counts1[user_id] != statistics['grade_counts']['ssh']):
                          ss_count = statistics['grade_counts']['ss']
                          ssh_count = statistics['grade_counts']['ssh']
                          total_count = ss_count + ssh_count
                          
                          message = f"The SS count for user {username} changed from {prev_grade_counts.get(user_id) + prev_grade_counts1.get(user_id)} to {total_count}\n"
                          
                          # print(message)
                          # await channel.send(message)
                          # embed = discord.Embed(title=f"Grade Counts change for {username}", color=0x00ff00)
                          # embed.add_field(name="Previous SS Count", value=prev_grade_counts.get(user_id, 0), inline=False)
                          # embed.add_field(name="Previous SSH Count", value=prev_grade_counts1.get(user_id, 0), inline=False)
                          # embed.add_field(name="New SS Count", value=ss_count, inline=False)
                          # embed.add_field(name="New SSH Count", value=ssh_count, inline=False)
                          # embed.add_field(name="Total Count", value=total_count, inline=False)
                          
                          # print(f"The SS count for user {username} changed from {prev_grade_counts.get(user_id, 0) + prev_grade_counts1.get(user_id, 0)} to {total_count}")
                          # await channel.send(embed=embed)
                          embed = discord.Embed(title="Stats Update", color=0x00ff00)
                          ss_count = statistics['grade_counts']['ss']
                          ssh_count = statistics['grade_counts']['ssh']
                          total_count = ss_count + ssh_count
                          embed.add_field(name="SS Count", value=f"{prev_grade_counts.get(user_id, 0) + prev_grade_counts1.get(user_id, 0)} -> {total_count}", inline=False)
                          country_code = user_data["country_code"].lower()
                          flag_url = f"https://flagcdn.com/48x36/{country_code}.png"
                          avatar_url = user_data["avatar_url"]
                          embed.set_thumbnail(url=flag_url)
                          embed.set_author(name=username, icon_url=avatar_url)
                          print(f"The SS count for user {username} changed from {prev_grade_counts.get(user_id, 0) + prev_grade_counts1.get(user_id, 0)} to {total_count}")
                          await channel.send(embed=embed)

                        if prev_stats['global_rank'] != statistics['global_rank']:
                            print(f"The global rank for user {username} changed from {prev_stats['global_rank']} to {statistics['global_rank']}")
                            # await channel.send(f"The global rank for user {username} changed from {prev_stats['global_rank']} to {statistics['global_rank']}")
                            embed = discord.Embed(title="Stats Update", color=0x00ff00)
                            embed.add_field(name="Global Rank", value=f"{prev_stats['global_rank']} -> {statistics['global_rank']}", inline=False)
                            country_code = user_data["country_code"].lower()
                            flag_url = f"https://flagcdn.com/48x36/{country_code}.png"
                            avatar_url = user_data["avatar_url"]
                            embed.set_thumbnail(url=flag_url)
                            embed.set_author(name=username, icon_url=avatar_url)
                            await channel.send(embed=embed)
                            
                        if prev_stats['pp'] != statistics['pp']:
                            # print(f"The PP for user {username} changed from {prev_stats['pp']} to {statistics['pp']}")
                            # # await channel.send(f"The PP for user {username} changed from {prev_stats['pp']} to {statistics['pp']}")
                            # pp_embed = discord.Embed(title=f"PP change for {username}", color=0x00ff00)
                            # pp_embed.add_field(name="Previous PP", value=prev_stats['pp'], inline=False)
                            # pp_embed.add_field(name="New PP", value=statistics['pp'], inline=False)
                            # print(f"The PP for user {username} changed from {prev_stats['pp']} to {statistics['pp']}")
                            # await channel.send(embed=pp_embed)
                            embed = discord.Embed(title="Stats Update", color=0x00ff00)
                            embed.add_field(name="PP", value=f"{prev_stats['pp']} -> {statistics['pp']}", inline=False)
                            country_code = user_data["country_code"].lower()
                            flag_url = f"https://flagcdn.com/48x36/{country_code}.png"
                            avatar_url = user_data["avatar_url"]
                            embed.set_thumbnail(url=flag_url)
                            embed.set_author(name=username, icon_url=avatar_url)
                            print(f"The PP for user {username} changed from {prev_stats['pp']} to {statistics['pp']}")
                            await channel.send(embed=embed)
                            
                        if prev_stats['ranked_score'] != statistics['ranked_score']:
                            # print(f"The ranked score for user {username} changed from {prev_stats['ranked_score']} to {statistics['ranked_score']}")
                            # await channel.send(f"The ranked score for user {username} changed from {prev_stats['ranked_score']} to {statistics['ranked_score']}")
                            embed = discord.Embed(title="Stats Update", color=0x00ff00)
                            embed.add_field(name="Ranked Score", value=f"{prev_stats['ranked_score']} -> {statistics['ranked_score']}", inline=False)
                            country_code = user_data["country_code"].lower()
                            flag_url = f"https://flagcdn.com/48x36/{country_code}.png"
                            avatar_url = user_data["avatar_url"]
                            embed.set_thumbnail(url=flag_url)
                            embed.set_author(name=username, icon_url=avatar_url)
                            print(f"The ranked score for user {username} changed from {prev_stats['ranked_score']} to {statistics['ranked_score']}")
                            await channel.send(embed=embed)
                            
                        if prev_stats['total_hits'] != statistics['total_hits']:
                            # print(f"The total hits for user {username} changed from {prev_stats['total_hits']} to {statistics['total_hits']}")
                            # await channel.send(f"The total hits for user {username} changed from {prev_stats['total_hits']} to {statistics['total_hits']}")
                            embed = discord.Embed(title="Stats Update", color=0x00ff00)
                            embed.add_field(name="Total Hits", value=f"{prev_stats['total_hits']} -> {statistics['total_hits']}", inline=False)
                            country_code = user_data["country_code"].lower()
                            flag_url = f"https://flagcdn.com/48x36/{country_code}.png"
                            avatar_url = user_data["avatar_url"]
                            embed.set_thumbnail(url=flag_url)
                            embed.set_author(name=username, icon_url=avatar_url)
                            print(f"The total hits for user {username} changed from {prev_stats['total_hits']} to {statistics['total_hits']}")
                            await channel.send(embed=embed)

                        if prev_stats['play_count'] != statistics['play_count']:
                            # await channel.send(f":video_game: **Play Count Alert** :video_game:\n\n{username}'s play count changed from **{prev_stats['play_count']}** to **{statistics['play_count']}**")
                            # embed = discord.Embed(title=f"{username}", description=f"The play count for user {username} changed from {prev_stats['play_count']} to {statistics['play_count']}", color=0xFF5733)
                            # embed.add_field(name="Rank", value=rank_info, inline=True)
                            embed = discord.Embed(title="Stats Update", color=0x00ff00)
                            embed.add_field(name="Play Count", value=f"{prev_stats['play_count']} -> {statistics['play_count']}", inline=False)
                            country_code = user_data["country_code"].lower()
                            flag_url = f"https://flagcdn.com/48x36/{country_code}.png"
                            avatar_url = user_data["avatar_url"]
                            embed.set_thumbnail(url=flag_url)
                            embed.set_author(name=username, icon_url=avatar_url)
                            await channel.send(embed=embed)
                    # Update the previous values
                    prev_statistics[user_id] = statistics
                    prev_grade_counts[user_id] = statistics['grade_counts']['ss']
                    prev_grade_counts1[user_id] = statistics['grade_counts']['ssh']

            await asyncio.sleep(30)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        print('Logged in as 'f'{client.user}')
        activity = discord.Activity(
        type=discord.ActivityType.watching,
        name=f"{len(client.guilds)} сервери")
        await client.change_presence(activity=activity)

        client.loop.create_task(my_background_task())
        client.loop.create_task(osu_check())
        

    client.run(TOKEN)