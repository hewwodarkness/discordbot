import discord
from discord import Intents

import threading

import asyncio

from ossapi import Ossapi

from tokendiscord import TOKEN
from tokendiscord import client_id
from tokendiscord import client_secret

import requests

intents = Intents.default()
intents.members = True
client = discord.Client(intents=intents)

user_idsss = ['10073635', '9830628', '9920144', '13705417', '4548264', '9820878', '9203015', '11653711', '14774230', '10096496', '16139008', '11794209', '7587763']

user_idsua = ['9739073', '11478380', '14135953', '8127948', '8906703', '21282552', '10113201', '8793110', '9503884', '13456984', '10411043', '11661929', '4382562']

async def osu_check():
    prev_statistics = {}
    prev_grade_counts = {}
    prev_grade_counts1 = {}
    channel = client.get_channel(1101777746968969307)

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


        for user_id in user_idsss:
            # Check statistics
            response = requests.get(
                f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
            if response.ok:
                user_data = response.json()
                statistics = user_data["statistics"]
                username = user_data["username"]
                avatar_url = user_data["avatar_url"]
                # Check if the values changed since the last call
                if user_id in prev_statistics:
                    prev_stats = prev_statistics[user_id]

                    if user_id in prev_grade_counts and (prev_grade_counts[user_id] != statistics['grade_counts']['ss'] or user_id in prev_grade_counts1 and prev_grade_counts1[user_id] != statistics['grade_counts']['ssh']):
                        ss_count = statistics['grade_counts']['ss']
                        ssh_count = statistics['grade_counts']['ssh']
                        total_count = ss_count + ssh_count

                        message = f"The SS count for user {username} changed from {prev_grade_counts.get(user_id) + prev_grade_counts1.get(user_id)} to {total_count}\n"
                        print(
                            f"The SS count for user {username} changed from {prev_grade_counts.get(user_id, 0) + prev_grade_counts1.get(user_id, 0)} to {total_count}")
                        embed = discord.Embed(color=0x00ff00)
                        embed.set_thumbnail(url=avatar_url)
                        embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                            user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['ranked_score']) / 10**9)
                        embed.add_field(
                            name="Ranked Score", value=formatted_score, inline=True)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['total_score']) / 10**9)
                        embed.add_field(
                            name="Total Score", value=formatted_score, inline=True)

                        embed.add_field(
                            name="Play Count", value=statistics['play_count'], inline=True)

                        embed.add_field(name="Play Time", value=(
                            str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                        embed.add_field(name="Level", value=(str(
                            statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                        embed.add_field(name="Hit Accuracy", value=round(
                            statistics['hit_accuracy'], 2), inline=True)

                        grade_counts = user_data["statistics"]['grade_counts']['ss']
                        grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                        sum = grade_counts + grade_counts1

                        embed.add_field(
                            name="SS Amount", value=sum, inline=True)
                        embed.add_field(
                            name="Hit Count", value=statistics["total_hits"], inline=True)
                        embed.add_field(
                            name="Followers", value=user_data["follower_count"], inline=True)

                        embed.add_field(
                            name="SS Amount", value=f"{prev_grade_counts.get(user_id, 0) + prev_grade_counts1.get(user_id, 0)} -> {total_count}", inline=False)
                        await channel.send(embed=embed)

                    if prev_stats['global_rank'] != statistics['global_rank']:
                        print(
                            f"The global rank for user {username} changed from {prev_stats['global_rank']} to {statistics['global_rank']}")
                        embed = discord.Embed(color=0x00ff00)
                        embed.set_thumbnail(url=avatar_url)
                        embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                            user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['ranked_score']) / 10**9)
                        embed.add_field(
                            name="Ranked Score", value=formatted_score, inline=True)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['total_score']) / 10**9)
                        embed.add_field(
                            name="Total Score", value=formatted_score, inline=True)

                        embed.add_field(
                            name="Play Count", value=statistics['play_count'], inline=True)

                        embed.add_field(name="Play Time", value=(
                            str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                        embed.add_field(name="Level", value=(str(
                            statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                        embed.add_field(name="Hit Accuracy", value=round(
                            statistics['hit_accuracy'], 2), inline=True)

                        grade_counts = user_data["statistics"]['grade_counts']['ss']
                        grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                        sum = grade_counts + grade_counts1

                        embed.add_field(
                            name="SS Amount", value=sum, inline=True)
                        embed.add_field(
                            name="Hit Count", value=statistics["total_hits"], inline=True)
                        embed.add_field(
                            name="Followers", value=user_data["follower_count"], inline=True)

                        embed.add_field(
                            name="Global Rank", value=f"{prev_stats['global_rank']} -> {statistics['global_rank']}", inline=False)
                        await channel.send(embed=embed)

                    if prev_stats['pp'] != statistics['pp']:
                        embed = discord.Embed(color=0x00ff00)
                        embed.set_thumbnail(url=avatar_url)
                        embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                            user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['ranked_score']) / 10**9)
                        embed.add_field(
                            name="Ranked Score", value=formatted_score, inline=True)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['total_score']) / 10**9)
                        embed.add_field(
                            name="Total Score", value=formatted_score, inline=True)

                        embed.add_field(
                            name="Play Count", value=statistics['play_count'], inline=True)

                        embed.add_field(name="Play Time", value=(
                            str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                        embed.add_field(name="Level", value=(str(
                            statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                        embed.add_field(name="Hit Accuracy", value=round(
                            statistics['hit_accuracy'], 2), inline=True)

                        grade_counts = user_data["statistics"]['grade_counts']['ss']
                        grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                        sum = grade_counts + grade_counts1

                        embed.add_field(
                            name="SS Amount", value=sum, inline=True)
                        embed.add_field(
                            name="Hit Count", value=statistics["total_hits"], inline=True)
                        embed.add_field(
                            name="Followers", value=user_data["follower_count"], inline=True)

                        embed.add_field(
                            name="PP", value=f"{prev_stats['pp']} -> {statistics['pp']}", inline=False)
                        await channel.send(embed=embed)

                prev_statistics[user_id] = statistics
                prev_grade_counts[user_id] = statistics['grade_counts']['ss']
                prev_grade_counts1[user_id] = statistics['grade_counts']['ssh']
                print(username + " SS checked")
        await asyncio.sleep(5)


async def osu_score_check():
    api = Ossapi(client_id, client_secret)
    previous_activity = {}
    channel = client.get_channel(1101777746968969307)
    # Obtain access token

    grant_type = "client_credentials"
    scope = "public"
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

    while True:
        try:
            for user_id in user_idsss:
                response = requests.get(
                    f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)

                if response.ok:
                    user_data = response.json()
                    statistics = user_data["statistics"]
                    username = user_data["username"]
                    avatar_url = user_data["avatar_url"]
                recent_activity = api.user_scores(
                    user_id=user_id, limit=1, offset=0, type='recent')

                if recent_activity:
                    recent_activity_id = recent_activity[0].id
                    print(recent_activity[0])
                    if user_id not in previous_activity or recent_activity_id != previous_activity[user_id].id:

                        usernameosu = api.user(
                            user_id, mode="osu").username
                        embed = discord.Embed(color=0x00ff00)

                        embed.set_thumbnail(url=avatar_url)
                        embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                            user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)
                        embed.add_field(
                            name='Map', value=f"{recent_activity[0].beatmapset.artist} - {recent_activity[0].beatmapset.title} [{recent_activity[0].beatmap.version}]", inline=False)

                        accuracy_str = '{:.2%}'.format(
                            recent_activity[0].accuracy)
                        embed.add_field(name="Accuracy",
                                        value=accuracy_str, inline=True)

                        embed.add_field(
                            name="Mods", value=recent_activity[0].mods, inline=True)

                        # embed.set_author(name=f"{usernameosu} achieved score on {recent_activity[0].beatmapset.artist} - {recent_activity[0].beatmapset.title} [{recent_activity[0].beatmap.version}]", icon_url=recent_activity[0]._user.avatar_url)

                        thumbnail_url = f'https://b.ppy.sh/thumb/{recent_activity[0].beatmapset.id}l.jpg'
                        embed.set_thumbnail(url=thumbnail_url)

                        embed.add_field(
                            name="PP", value=recent_activity[0].pp, inline=True)

                        embed.add_field(
                            name="Difficulty", value=recent_activity[0].beatmap.difficulty_rating, inline=True)

                        embed.add_field(
                            name="BPM", value=recent_activity[0].beatmap.bpm, inline=True)

                        embed.add_field(
                            name="Combo", value=recent_activity[0].max_combo, inline=True)

                        embed.add_field(
                            name="Grade", value=recent_activity[0].rank.name, inline=True)

                        embed.add_field(
                            name="Passed", value=recent_activity[0].passed, inline=True)

                        embed.add_field(
                            name="Played Date", value=recent_activity[0].created_at, inline=True)

                        embed.set_footer(
                            text="Bot made by Virgo#4146 with a big GPT help | Version 1.0")

                        await channel.send(embed=embed)

                        previous_activity[user_id] = recent_activity[0]
                print(user_id)
                print("SS SCORE checked")
        except IndexError:
            print(
                f"Recent activity is empty for user ID {user_id}. Skipping to next iteration.")
        await asyncio.sleep(5)


async def osu_checkua():
    prev_statistics = {}
    prev_grade_counts = {}
    prev_grade_counts1 = {}
    channel = client.get_channel(1101777746968969307)

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


        for user_id in user_idsua:
            # Check statistics
            response = requests.get(
                f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
            if response.ok:
                user_data = response.json()
                statistics = user_data["statistics"]
                username = user_data["username"]
                avatar_url = user_data["avatar_url"]
                # Check if the values changed since the last call
                if user_id in prev_statistics:
                    prev_stats = prev_statistics[user_id]

                    if user_id in prev_grade_counts and (prev_grade_counts[user_id] != statistics['grade_counts']['ss'] or user_id in prev_grade_counts1 and prev_grade_counts1[user_id] != statistics['grade_counts']['ssh']):
                        ss_count = statistics['grade_counts']['ss']
                        ssh_count = statistics['grade_counts']['ssh']
                        total_count = ss_count + ssh_count

                        message = f"The SS count for user {username} changed from {prev_grade_counts.get(user_id) + prev_grade_counts1.get(user_id)} to {total_count}\n"
                        print(
                            f"The SS count for user {username} changed from {prev_grade_counts.get(user_id, 0) + prev_grade_counts1.get(user_id, 0)} to {total_count}")
                        embed = discord.Embed(color=0x00ff00)
                        embed.set_thumbnail(url=avatar_url)
                        embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                            user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['ranked_score']) / 10**9)
                        embed.add_field(
                            name="Ranked Score", value=formatted_score, inline=True)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['total_score']) / 10**9)
                        embed.add_field(
                            name="Total Score", value=formatted_score, inline=True)

                        embed.add_field(
                            name="Play Count", value=statistics['play_count'], inline=True)

                        embed.add_field(name="Play Time", value=(
                            str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                        embed.add_field(name="Level", value=(str(
                            statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                        embed.add_field(name="Hit Accuracy", value=round(
                            statistics['hit_accuracy'], 2), inline=True)

                        grade_counts = user_data["statistics"]['grade_counts']['ss']
                        grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                        sum = grade_counts + grade_counts1

                        embed.add_field(
                            name="SS Amount", value=sum, inline=True)
                        embed.add_field(
                            name="Hit Count", value=statistics["total_hits"], inline=True)
                        embed.add_field(
                            name="Followers", value=user_data["follower_count"], inline=True)

                        embed.add_field(
                            name="SS Amount", value=f"{prev_grade_counts.get(user_id, 0) + prev_grade_counts1.get(user_id, 0)} -> {total_count}", inline=False)
                        await channel.send(embed=embed)

                    if prev_stats['global_rank'] != statistics['global_rank']:
                        print(
                            f"The global rank for user {username} changed from {prev_stats['global_rank']} to {statistics['global_rank']}")
                        embed = discord.Embed(color=0x00ff00)
                        embed.set_thumbnail(url=avatar_url)
                        embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                            user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['ranked_score']) / 10**9)
                        embed.add_field(
                            name="Ranked Score", value=formatted_score, inline=True)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['total_score']) / 10**9)
                        embed.add_field(
                            name="Total Score", value=formatted_score, inline=True)

                        embed.add_field(
                            name="Play Count", value=statistics['play_count'], inline=True)

                        embed.add_field(name="Play Time", value=(
                            str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                        embed.add_field(name="Level", value=(str(
                            statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                        embed.add_field(name="Hit Accuracy", value=round(
                            statistics['hit_accuracy'], 2), inline=True)

                        grade_counts = user_data["statistics"]['grade_counts']['ss']
                        grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                        sum = grade_counts + grade_counts1

                        embed.add_field(
                            name="SS Amount", value=sum, inline=True)
                        embed.add_field(
                            name="Hit Count", value=statistics["total_hits"], inline=True)
                        embed.add_field(
                            name="Followers", value=user_data["follower_count"], inline=True)

                        embed.add_field(
                            name="Global Rank", value=f"{prev_stats['global_rank']} -> {statistics['global_rank']}", inline=False)
                        await channel.send(embed=embed)

                    if prev_stats['pp'] != statistics['pp']:
                        embed = discord.Embed(color=0x00ff00)
                        embed.set_thumbnail(url=avatar_url)
                        embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                            user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['ranked_score']) / 10**9)
                        embed.add_field(
                            name="Ranked Score", value=formatted_score, inline=True)

                        formatted_score = '{:.1f} bln'.format(
                            float(statistics['total_score']) / 10**9)
                        embed.add_field(
                            name="Total Score", value=formatted_score, inline=True)

                        embed.add_field(
                            name="Play Count", value=statistics['play_count'], inline=True)

                        embed.add_field(name="Play Time", value=(
                            str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                        embed.add_field(name="Level", value=(str(
                            statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                        embed.add_field(name="Hit Accuracy", value=round(
                            statistics['hit_accuracy'], 2), inline=True)

                        grade_counts = user_data["statistics"]['grade_counts']['ss']
                        grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                        sum = grade_counts + grade_counts1

                        embed.add_field(
                            name="SS Amount", value=sum, inline=True)
                        embed.add_field(
                            name="Hit Count", value=statistics["total_hits"], inline=True)
                        embed.add_field(
                            name="Followers", value=user_data["follower_count"], inline=True)

                        embed.add_field(
                            name="PP", value=f"{prev_stats['pp']} -> {statistics['pp']}", inline=False)
                        await channel.send(embed=embed)

                prev_statistics[user_id] = statistics
                prev_grade_counts[user_id] = statistics['grade_counts']['ss']
                prev_grade_counts1[user_id] = statistics['grade_counts']['ssh']
                print(username + " UA checked")
        await asyncio.sleep(5)


async def osu_score_checkua():
    api = Ossapi(client_id, client_secret)
    previous_activity = {}
    channel = client.get_channel(1101777746968969307)
    # Obtain access token

    grant_type = "client_credentials"
    scope = "public"
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

    while True:
        try:
            for user_id in user_idsua:
                response = requests.get(
                    f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)

                if response.ok:
                    user_data = response.json()
                    statistics = user_data["statistics"]
                    username = user_data["username"]
                    avatar_url = user_data["avatar_url"]
                recent_activity = api.user_scores(
                    user_id=user_id, limit=1, offset=0, type='recent')

                if recent_activity:
                    recent_activity_id = recent_activity[0].id
                    print(recent_activity[0])
                    if user_id not in previous_activity or recent_activity_id != previous_activity[user_id].id:

                        usernameosu = api.user(
                            user_id, mode="osu").username
                        embed = discord.Embed(color=0x00ff00)

                        embed.set_thumbnail(url=avatar_url)
                        embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
                            user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)
                        embed.add_field(
                            name='Map', value=f"{recent_activity[0].beatmapset.artist} - {recent_activity[0].beatmapset.title} [{recent_activity[0].beatmap.version}]", inline=False)

                        accuracy_str = '{:.2%}'.format(
                            recent_activity[0].accuracy)
                        embed.add_field(name="Accuracy",
                                        value=accuracy_str, inline=True)

                        embed.add_field(
                            name="Mods", value=recent_activity[0].mods, inline=True)

                        # embed.set_author(name=f"{usernameosu} achieved score on {recent_activity[0].beatmapset.artist} - {recent_activity[0].beatmapset.title} [{recent_activity[0].beatmap.version}]", icon_url=recent_activity[0]._user.avatar_url)

                        thumbnail_url = f'https://b.ppy.sh/thumb/{recent_activity[0].beatmapset.id}l.jpg'
                        embed.set_thumbnail(url=thumbnail_url)

                        embed.add_field(
                            name="PP", value=recent_activity[0].pp, inline=True)

                        embed.add_field(
                            name="Difficulty", value=recent_activity[0].beatmap.difficulty_rating, inline=True)

                        embed.add_field(
                            name="BPM", value=recent_activity[0].beatmap.bpm, inline=True)

                        embed.add_field(
                            name="Combo", value=recent_activity[0].max_combo, inline=True)

                        embed.add_field(
                            name="Grade", value=recent_activity[0].rank.name, inline=True)

                        embed.add_field(
                            name="Passed", value=recent_activity[0].passed, inline=True)

                        embed.add_field(
                            name="Played Date", value=recent_activity[0].created_at, inline=True)

                        embed.set_footer(
                            text="Bot made by Virgo#4146 with a big GPT help | Version 1.0")

                        await channel.send(embed=embed)

                        previous_activity[user_id] = recent_activity[0]
                print(user_id)
                print("UA SCORE checked")
        except IndexError:
            print(
                f"Recent activity is empty for user ID {user_id}. Skipping to next iteration.")
        await asyncio.sleep(5)


@client.event
async def on_ready():
    # Start both functions in separate tasks when the bot is ready
    client.loop.create_task(osu_check())
    client.loop.create_task(osu_score_check())
    print('Bot is ready.')

client.run(TOKEN)
