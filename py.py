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
import discord
from discord.ext import commands

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

    # Start the main event loop
    icon.run()

    win32gui.SetWindowText(win32gui.GetForegroundWindow(), "Bot")

if __name__ == '__main__':
    # Start the tray icon in a separate thread
    win32gui.SetWindowText(win32gui.GetForegroundWindow(), "Bot")
    threading.Thread(target=create_tray_icon).start()
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

    # Start the Discord bot in the main thread
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    REACTION_EMOJIS = ['🛐','♿','🅿️','🇷','🇴']

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

        async def check_for_virgo(message):
            if "я фанатка вірго" in message.content.lower() and message.author != client.user:
                response = "я фанатка вірго"
                await message.reply(response)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        print('Logged in as')
        print(client.user.name)

        activity = discord.Activity(
        type=discord.ActivityType.watching,
        name=f"{len(client.guilds)} сервери")
        await client.change_presence(activity=activity)


        client.loop.create_task(my_background_task())

    client.run(TOKEN)