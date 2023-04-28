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
import time
from bs4 import BeautifulSoup
from ossapi import Ossapi, UserLookupKey, GameMode, RankingType, UserCompact, OssapiV1
from io import BytesIO
import win32api
from rule_check import rule_check
from sankaku_check import sankaku_check
r34Py = rule34Py()
user_ids = [
    '912627', '5249196'
    # , '11196666', '19381776'

    # ,"10030328", "SS is hard", "Namazu"

    # 'Zalaria', 'Sleepteiner', 'Przegrany', 'WiMpN', 'Virgo', 'EEEEEEEEEEEEEEE', 'Sure', 'WubWoofWolf'
    # ,'Alduric', 'TheShadowOfDark', 'SS or Quit', 'vasasu', 'Sevelik', 'WorldChallenge', 'Sayonara Sakura', 'Noercy','Louis Marble', 'eralfehT', 'Nitry', 'seven39', 'Hammer', 'Duskyui', 'phionebaby56', 'Marquez', 'Genki1000', 'Namazu', 'Sowisty', 'Suwako', 'ImMyyrh',
    # 'Autumn Brightness', 'P e n g u', '_starry', 'Salamat', 'Suome', 'Torveld', 'Yuzyu', 'Ringtext', 'Azukane', 'Musa', 'Koltay', 'I D S', 'STS2', 'wiuuuh', 'Maklovitz', 'shun2yu', 'Mithrane', 'Hranolka', 'novaaa', 'SS is hard', 'Evgas', '[-Griffin-]', 'Kilgar', 'aya_nico', 'Inoculum', 'Aikyuu-Chan', 'Serious07', 'Ma Yuyu', 'Amity-Senpai', 'Piro13', 'Emilily', 'boob enjoyer', 'Dakishimeru', 'iPhong',
    # 'Vernien', 'Tactic', 'auroraflow12','Lokra', 'hent2222', 'Swakz', 'fjw', 'amea', '290ms', 'MomoPrecil', 'Naren', 'LosingCrayon', 'Chaoslitz', 'Xeanex', 'FuzimiyaYuki', 'Yurukane', 'Sipsu', 'CyberSylver', 'sanghaaaa', 'MystExiStentia', 'mashihunter'

    # ,'10073635', '9830628', '9920144', '13705417', '4548264', '9820878', '9203015', '11653711', '14774230', '10096496', '16139008', '11794209', '7587763', '13331292', '11078815', '9249873', '12935582', '10394538', '6997572', '9919528', '11168760', '9588826', '14257184', '8068756', '7979597', '11107767', '1163931', '16473262', '7280649', '8821737', '10021516', '5249196', '3197720', '14899675', '7242804', '6749564', '7662338',
    # '7779302', '9819240', '3734954', '10291667', '27679241', '12346522', '10472893', '8364294', '11274086', '6549455', '20705797', '10179274', '9833677'

    # ,'12096642', '9221036', '11466354', '11804476', '11507955', '12292418', '14106178', '7449054', '7400290', '10344994', '11629570', '912627', '11275181', '12660895', '10643960', '14765820', '6627436', '14578826', '12743021', '13554804', '9762657', '12681959', '13288542', '6544807', '4809354', '9601607', '17459923', '11301847', '8028083', '10796788', '18179814', '16201107', '6338935', '6889400', '10771308', '7173453', '8568265',
    # '11701099', '6766278', '21225796', '12561480', '10910184', '7855006', '11731667', '18781432', '9613137', '17839714', '4855610', '496387', '9671924',

    # '2174403', '9947204', '7643728', '10273749', '13614447', '11894596', '15556878', '10238693', '3428396', '15521003', '9226415', '7364801', '8807110', '4989296', '15625177', '13872859', '4851835', '8046661',
    # '9739073', '11478380', '14135953', '8127948', '8906703', '21282552', '10113201', '8793110', '9503884', '13456984', '10411043', '11661929', '4382562', '13372905', '12703752', '19823568', '8685078', '5337025', '8801931', '11390112', '9399161', '7498628', '5869499', '14045182', '7233101', '12251165', '6860786', '10339839', '9027396', '14736743', '384003', '9625516',

    # '9730570', '6416790', '21251018', '7404253', '14226704', '21049273', '16713164', '7333988', '13983096', '3812874', '11396893', '5022536', '11121624', '8873826', '14644581', '7629976', '11348468', '11980473', '5026496', '6858123', '6359314', '6221637', '11057337', '11537088', '8466916', '7051066', '12820993', '12527217', '10020388', '12460150', '12772652', '8952169', '8625228', '19238927', '9634394', '1307553', '15436916',
    # '13017880', '12467855', '10480852', '5420543', '11164063', '9225814', '11274753', '15347449', '11351901', '10554771', '11296867', '11754046', '12488594',

    # '6448400', '11314398', '12421948', '16299020', '6337425', '15885344', '19870715', '21479205', '2608977', '6348581', '12178531', '7152873', '15516626', '6562416', '13119684', '11878788', '13991003', '15056040', '17620910', '14068542', '9578264', '11789398', '7133687', '9101624', '8662649', '17444658', '12406262', '8200703', '11130243', '13129738', '8184362', '4393327', '8645771', '8753394', '6950584', '7181226', '7156119',
    # '9628870', '13064058', '8133912', '17561841', '13200974', '9284210', '14702894', '13563907', '16955567', '11532890', '7793117', '10574233', '4928461'
]
user_id_batches = [user_ids[i:i+100] for i in range(0, len(user_ids), 100)]
PICTURE_FOLDER = "C:/Users/Эльф/Desktop/memess"
REACTION_EMOJIS = ['🛐', '♿', '🅿️', '🇷', '🇴']
REACTION_EMOJIS1 = ['🇴', '🇱', '🇪', '🇬']
api_call_counts = {}


async def send_stats_update(channel, username, user_data, prev_stats, statistics, field_name, prev_field_value):
    embed = discord.Embed(color=0x00ff00)
    country_code = user_data["country_code"].lower()
    avatar_url = user_data["avatar_url"]
    embed.set_thumbnail(url=avatar_url)
    embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(
        user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

    if prev_stats['ranked_score'] != statistics['ranked_score']:
        change = statistics['ranked_score'] - prev_stats['ranked_score']
        sign = "+" if change >= 0 else ""
        field_value = f"{statistics['ranked_score'] / 10**9:.1f} bln {sign} {abs(change) / 10**6:.1f} mln"
    else:
        field_value = f"{statistics['ranked_score'] / 10**9:.1f} bln"

    embed.add_field(name="Ranked Score", value=field_value, inline=True)

    if prev_stats['total_score'] != statistics['total_score']:
        change = statistics['total_score'] - prev_stats['total_score']
        sign = "+" if change >= 0 else ""
        field_value = f"{statistics['total_score'] / 10**9:.1f} bln {sign} {abs(change) / 10**6:.1f} mln"
    else:
        field_value = f"{statistics['total_score'] / 10**9:.1f} bln"

    embed.add_field(name="Total Score", value=field_value, inline=True)

    if prev_stats['play_count'] != statistics['play_count']:
        change = statistics['play_count'] - prev_stats['play_count']
        sign = "+" if change >= 0 else ""
        field_value = f"{statistics['play_count']} {sign} {abs(change)}"
    else:
        field_value = str(statistics['play_count'])

    embed.add_field(name="Play Count", value=field_value, inline=True)

    if prev_stats['play_time'] != statistics['play_time']:
        change = statistics['play_time'] - prev_stats['play_time']
        sign = "+" if change >= 0 else ""
        field_value = f"{round(statistics['play_time'] / 60 / 60, 2)} hours {sign} {round(abs(change) / 60 / 60, 2)} hours"
    else:
        field_value = f"{round(statistics['play_time'] / 60 / 60, 2)} hours"

    embed.add_field(name="Play Time", value=field_value, inline=True)

    if prev_stats['level']['current'] != statistics['level']['current'] or prev_stats['level']['progress'] != statistics['level']['progress']:
        field_value = f"{statistics['level']['current']}.{statistics['level']['progress']}"
    else:
        field_value = f"{prev_stats['level']['current']}.{prev_stats['level']['progress']}"

    embed.add_field(name="Level", value=field_value, inline=True)

    if prev_stats['hit_accuracy'] != statistics['hit_accuracy']:
        change = statistics['hit_accuracy'] - prev_stats['hit_accuracy']
        sign = "+" if change >= 0 else ""
        field_value = f"{round(statistics['hit_accuracy'], 2)}% {sign} {round(abs(change), 2)}%"
    else:
        field_value = f"{round(statistics['hit_accuracy'], 2)}%"

    embed.add_field(name="Hit Accuracy", value=field_value, inline=True)

    if prev_stats["grade_counts"]["ss"] != statistics["grade_counts"]["ss"] or prev_stats["grade_counts"]["ssh"] != statistics["grade_counts"]["ssh"]:
        change = statistics["grade_counts"]["ss"] + statistics["grade_counts"]["ssh"] - \
            prev_stats["grade_counts"]["ss"] - \
            prev_stats["grade_counts"]["ssh"]
        sum = statistics["grade_counts"]["ss"] + \
            statistics["grade_counts"]["ssh"]
        sign = "+" if change >= 0 else ""
        field_value = f"{sum} ({sign}{abs(change)})"
    else:
        sum = prev_stats["grade_counts"]["ss"] + \
            prev_stats["grade_counts"]["ssh"]
        field_value = f"{sum}"

    embed.add_field(name="SS Amount", value=field_value, inline=True)

    if prev_stats['total_hits'] != statistics['total_hits']:
        change = statistics['total_hits'] - prev_stats['total_hits']
        sign = "+" if change >= 0 else ""
        field_value = f"{statistics['total_hits']} {sign} {abs(change)}"
    else:
        field_value = f"{statistics['total_hits']}"

    embed.add_field(name="Hit Count", value=field_value, inline=True)
    embed.add_field(name="Followers",
                    value=user_data["follower_count"], inline=True)

    if prev_stats['pp'] != statistics['pp']:
        change = statistics['pp'] - prev_stats['pp']
        sign = "+" if change >= 0 else ""
        field_value = f"{statistics['pp']}pp {sign}{abs(change)}"
    else:
        field_value = f"{statistics['pp']}pp"

    embed.add_field(name="PP", value=field_value, inline=False)

    print("smth changed idk")
    await channel.send(embed=embed)


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

    # Hide the window when it is minimized
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)


def create_tray_icon():
    # Create a tray icon
    image = Image.open("2.png")
    menu = pystray.Menu(pystray.MenuItem("Open", on_open),
                        pystray.MenuItem("Exit", on_quit))
    icon = pystray.Icon("My App", image, "My App", menu)

    icon.run()


if __name__ == '__main__':
    # Start the tray icon in a separate thread

    win32gui.SetWindowText(win32gui.GetForegroundWindow(), "Bot")
    threading.Thread(target=create_tray_icon).start()
    win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_HIDE)

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

            if message.author.id == 317702705743396864:
                for emoji1 in REACTION_EMOJIS1:
                    await message.add_reaction(emoji1)

            await check_for_virgo(message)
            await check_for_cygan(message)
            await on_pic(message)
            await ss_count(message)
            await on_based(message)
            await send_stats_update1(message)
            await check_for_helpss(message)

        async def check_for_virgo(message):
            if "я фанатка вірго" in message.content.lower() and message.author != client.user:
                response = "я фанатка вірго"
                await message.reply(response)

        async def check_for_cygan(message):
            if "циган" in message.content.lower():
                with open("cygan.jpg", "rb") as f:
                    picture = discord.File(f)
                    await message.reply(file=picture)

        async def check_for_helpss(message):
            if "!helpss" in message.content.lower():
                embed = discord.Embed(title=":information_source: Help Message",
                                      description="Here are some commands you can use:", color=0xFFDAB9)
                embed.add_field(name=":camera_with_flash: !picsecret",
                                value="Displays an image matching the provided tags.\nExample: `!picsecret rating:safe 1girl`", inline=False)
                embed.add_field(
                    name=":virgo: !ss", value="Displays the amount of SS a player has on their account.\nExample: `!ss Virgo`", inline=False)
                embed.add_field(name=":question: ти шо циган",
                                value="Asks the bot a question.\nExample: `ти шо циган`", inline=False)
                embed.add_field(name=":star_struck: я фанатка вірго",
                                value="Expresses your admiration for a certain person.\nExample: `я фанатка вірго`", inline=False)
                embed.set_footer(
                    text="Bot made by Virgo#4146 with a big GPT help | Version 1.0")
                await message.reply(embed=embed)

        async def send_stats_update1(message):
            channel = client.get_channel(1099409748543148142)
            field_name = "hyila"
            username = "Virgo"
            if "!test" in message.content.lower():
                embed = discord.Embed(title="Stats Update", color=0x90EE90)
                embed.add_field(name=field_name.capitalize(),
                                value="POggers", inline=False)
                flag_url = f"https://flagcdn.com/48x36/ua.png"
                avatar_url = f"https://a.ppy.sh/5249196?1680950015.jpeg"
                embed.set_thumbnail(url=avatar_url)
                embed.set_author(
                    name=username, url="https://osu.ppy.sh/users/" + username, icon_url=flag_url)
                print(f"The SS for user Virgo changed from 11211 to 11113")
                await channel.send(embed=embed)

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
                    response = "Please provide at least one tag."
                else:
                    tags = words[1:]
                    bazatest = r34Py.random_post(tags)
                    url = bazatest.image  # Replace with your image URL
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
                    response = requests.get(
                        f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
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
            current_minute = time.strftime('%Y-%m-%d %H:%M')
            if current_minute in api_call_counts:
                api_call_counts[current_minute] += 1
            else:
                api_call_counts[current_minute] = 1
            for batch in user_id_batches:
                for user_id in batch:
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

                            # if prev_stats['ranked_score'] != statistics['ranked_score']:
                            #     embed = discord.Embed(color=0x00ff00)
                            #     embed.set_thumbnail(url=avatar_url)
                            #     embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                            #     formatted_score = '{:.1f} bln'.format(float(statistics['ranked_score']) / 10**9)
                            #     embed.add_field(name="Ranked Score", value=formatted_score, inline=True)

                            #     formatted_score = '{:.1f} bln'.format(float(statistics['total_score']) / 10**9)
                            #     embed.add_field(name="Total Score", value=formatted_score, inline=True)

                            #     embed.add_field(name="Play Count", value=statistics['play_count'], inline=True)

                            #     embed.add_field(name="Play Time", value=(str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                            #     embed.add_field(name="Level", value=(str(statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                            #     embed.add_field(name="Hit Accuracy", value=round(statistics['hit_accuracy'],2), inline=True)

                            #     grade_counts = user_data["statistics"]['grade_counts']['ss']
                            #     grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                            #     sum = grade_counts + grade_counts1

                            #     embed.add_field(name="SS Amount", value=sum, inline=True)
                            #     embed.add_field(name="Hit Count", value=statistics["total_hits"], inline=True)
                            #     embed.add_field(name="Followers", value=user_data["follower_count"], inline=True)

                            #     embed.add_field(name="Ranked Score", value=f"{prev_stats['ranked_score']} -> {statistics['ranked_score']}", inline=False)
                            #     await channel.send(embed=embed)

                            # if prev_stats['total_hits'] != statistics['total_hits']:
                            #     embed = discord.Embed(color=0x00ff00)
                            #     embed.set_thumbnail(url=avatar_url)
                            #     embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                            #     formatted_score = '{:.1f} bln'.format(float(statistics['ranked_score']) / 10**9)
                            #     embed.add_field(name="Ranked Score", value=formatted_score, inline=True)

                            #     formatted_score = '{:.1f} bln'.format(float(statistics['total_score']) / 10**9)
                            #     embed.add_field(name="Total Score", value=formatted_score, inline=True)

                            #     embed.add_field(name="Play Count", value=statistics['play_count'], inline=True)

                            #     embed.add_field(name="Play Time", value=(str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                            #     embed.add_field(name="Level", value=(str(statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                            #     embed.add_field(name="Hit Accuracy", value=round(statistics['hit_accuracy'],2), inline=True)

                            #     grade_counts = user_data["statistics"]['grade_counts']['ss']
                            #     grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                            #     sum = grade_counts + grade_counts1

                            #     embed.add_field(name="SS Amount", value=sum, inline=True)
                            #     embed.add_field(name="Hit Count", value=statistics["total_hits"], inline=True)
                            #     embed.add_field(name="Followers", value=user_data["follower_count"], inline=True)

                            #     embed.add_field(name="Total Hits", value=f"{prev_stats['total_hits']} -> {statistics['total_hits']}", inline=False)
                            #     await channel.send(embed=embed)

                            # if prev_stats['play_count'] != statistics['play_count']:
                            #     embed = discord.Embed(color=0x00ff00)
                            #     embed.set_thumbnail(url=avatar_url)
                            #     embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)

                            #     formatted_score = '{:.1f} bln'.format(float(statistics['ranked_score']) / 10**9)
                            #     embed.add_field(name="Ranked Score", value=formatted_score, inline=True)

                            #     formatted_score = '{:.1f} bln'.format(float(statistics['total_score']) / 10**9)
                            #     embed.add_field(name="Total Score", value=formatted_score, inline=True)

                            #     embed.add_field(name="Play Count", value=statistics['play_count'], inline=True)

                            #     embed.add_field(name="Play Time", value=(str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                            #     embed.add_field(name="Level", value=(str(statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                            #     embed.add_field(name="Hit Accuracy", value=round(statistics['hit_accuracy'],2), inline=True)

                            #     grade_counts = user_data["statistics"]['grade_counts']['ss']
                            #     grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                            #     sum = grade_counts + grade_counts1

                            #     embed.add_field(name="SS Amount", value=sum, inline=True)
                            #     embed.add_field(name="Hit Count", value=statistics["total_hits"], inline=True)
                            #     embed.add_field(name="Followers", value=user_data["follower_count"], inline=True)

                            #     embed.add_field(name="Play Count", value=f"{prev_stats['total_hits']} -> {statistics['total_hits']}", inline=False)
                            #     await channel.send(embed=embed)

                        # Update the previous values
                        prev_statistics[user_id] = statistics
                        prev_grade_counts[user_id] = statistics['grade_counts']['ss']
                        prev_grade_counts1[user_id] = statistics['grade_counts']['ssh']
                        print(username + " checked")
            await asyncio.sleep(100)

    async def osu_score_check():
        api = Ossapi(client_id, client_secret)
        previous_activity = {}
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

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-version": str(20220707),
        }

        while True:
            try:
                for user_id in user_ids:
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
                    print("SCORE")
                    print(user_id)
                    print("SCORE checked")
            except IndexError:
                print(
                    f"Recent activity is empty for user ID {user_id}. Skipping to next iteration.")
            await asyncio.sleep(60)

    async def update_presence(client):
        channel_count = 0
        for guild in client.guilds:
            channel_count += len(guild.text_channels)

        activity_names = [
            lambda: f"{len(client.guilds)} сервери",
            "Використай !helpss",
            lambda: f"{channel_count} текст. каналів",
        ]

        current_index = 0
        while True:
            activity_name = activity_names[current_index % len(activity_names)]
            if callable(activity_name):
                activity = discord.Activity(
                    type=discord.ActivityType.watching,
                    name=activity_name())
            else:
                activity = discord.Activity(
                    type=discord.ActivityType.playing,
                    name=activity_name)
            await client.change_presence(activity=activity)
            current_index += 1
            await asyncio.sleep(15)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        print('Logged in as 'f'{client.user}')

        client.loop.create_task(update_presence(client))
        client.loop.create_task(my_background_task())
        client.loop.create_task(osu_check())
        client.loop.create_task(osu_score_check())
        client.loop.create_task(rule_check(client))
        # client.loop.create_task(sankaku_check(client))

    client.run(TOKEN)
