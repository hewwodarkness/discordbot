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
from discord.ext import commands
import random
import requests
from rule34Py import rule34Py
import io
import aiohttp

r34Py = rule34Py()
user_ids = ["blednak", "Virgo", "SS is hard", "P e n g u", "Inoculum", "rikka", "wimpn", "Sure", "Hammer", "noercy", "worldchallenge", "10030328", "zalaria", "sleepteiner"]
GLOBALSS = ''
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
    

    async def ss_check():
        prev_grade_counts = {}
        prev_grade_counts1 = {}
        channel = client.get_channel(1099409748543148142)

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

        # Define headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-version": str(20220707),
        }

        while True:
            for user_id in user_ids:
                response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
                if response.ok:
                    user_data = response.json()
                    grade_counts = user_data["statistics"]['grade_counts']['ss']
                    grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                    sum = grade_counts + grade_counts1
                    username = user_data["username"]

                    # Check if the values changed since the last call
                    if user_id in prev_grade_counts or user_id in prev_grade_counts1:
                        if prev_grade_counts.get(user_id) != grade_counts or prev_grade_counts1.get(user_id) != grade_counts1:
                            await channel.send(f"The ss count for user {username} changed from {prev_grade_counts.get(user_id, 0)} to {grade_counts}, and the ssh count changed from {prev_grade_counts1.get(user_id, 0)} to {grade_counts1}")

                    # Update the previous values
                    prev_grade_counts[user_id] = grade_counts
                    prev_grade_counts1[user_id] = grade_counts1

            await asyncio.sleep(60)



    async def rank_check():
        prev_global_rank = {}
        channel = client.get_channel(1099409748543148142)

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

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-version": str(20220707),
        }

        while True:
            for user_id in user_ids:
                response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
                if response.ok:
                    user_data = response.json()
                    global_rank = user_data["statistics"]['global_rank']
                    username = user_data["username"]
                    # Check if the value changed since the last call
                    if user_id in prev_global_rank and prev_global_rank[user_id] != global_rank:
                        await channel.send(f"The global rank for user {username} changed from {prev_global_rank[user_id]} to {global_rank}")

                    # Update the previous value
                    prev_global_rank[user_id] = global_rank

            await asyncio.sleep(60)

    async def pp_check():
        prev_pp = {}
        channel = client.get_channel(1099409748543148142)
        while True:
            for user_id in user_ids:
                grant_type = "client_credentials"
                scope = "public"

                # Send a request to the authorization server to obtain an access token
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        "https://osu.ppy.sh/oauth/token",
                        data={
                            "client_id": client_id,
                            "client_secret": client_secret,
                            "grant_type": grant_type,
                            "scope": scope,
                        },
                    ) as response:
                        # Parse the response JSON to extract the access token
                        access_token = (await response.json())["access_token"]

                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                    "x-api-version": str(20220707),
                }

                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers) as response:
                        if response.status == 200:
                            user_data = await response.json()
                            pp = user_data["statistics"]['pp']
                            username = user_data["username"]

                            # Check if the value changed since the last call
                            if user_id in prev_pp and prev_pp[user_id] != pp:
                                await channel.send(f"The PP for user {username} changed from {prev_pp[user_id]} to {pp}")

                            # Update the previous value
                            prev_pp[user_id] = pp

            await asyncio.sleep(60)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        print('Logged in as 'f'{client.user}')
        activity = discord.Activity(
        type=discord.ActivityType.watching,
        name=f"{len(client.guilds)} сервери")
        await client.change_presence(activity=activity)

        client.loop.create_task(my_background_task())
        client.loop.create_task(ss_check())
        client.loop.create_task(rank_check())
        client.loop.create_task(pp_check())
        

    client.run(TOKEN)