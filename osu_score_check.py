async def osu_score_check():
        api = Ossapi(client_id, client_secret)
        previous_activity = {}
        channel = client.get_channel(1103003732947501117)
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
        print(previous_activity)
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
                        previous_activity[user_id] = recent_activity[0]

                print("SCORE")
                print(user_id)
                print("SCORE checked")
        except IndexError:
            print(
                f"Recent activity is empty for user ID {user_id}. Skipping to next iteration.")
        print(previous_activity)
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
                                name='', value=f"**[{recent_activity[0].beatmapset.artist} - {recent_activity[0].beatmapset.title} [{recent_activity[0].beatmap.version}]]({recent_activity[0].beatmap.url})**", inline=False)

                            accuracy_str = '{:.2%}'.format(
                                recent_activity[0].accuracy)

                            created_at = recent_activity[0].created_at
                            # Convert the created_at attribute to a Unix timestamp
                            timestamp = int(created_at.timestamp())
                            # Convert the Unix timestamp to a datetime object
                            discord_time = datetime.fromtimestamp(timestamp)
                            # Format the datetime object as a Discord timestamp
                            discord_time_str = discord_time.strftime('<t:%s:R>' % timestamp)
                            # Add the formatted timestamp to the embed as a field
                            embed.add_field(name="",
                                            value=f"✦ +{recent_activity[0].mods} ✦ {accuracy_str} ✦ x{recent_activity[0].max_combo} ✦ {discord_time_str}", inline=False)
                            if (recent_activity[0].pp == None):
                                embed.add_field(name="",
                                                value=f"✦ {recent_activity[0].rank.name} rank ✦ 0 pp", inline=False)
                            else:
                                embed.add_field(name="",
                                            value=f"✦ {recent_activity[0].rank.name} rank ✦ {recent_activity[0].pp}pp", inline=False)

                            # embed.add_field(name="",
                            #                 value=f"✦ Played at: {discord_time_str}", inline=False)

                            # embed.add_field(
                            #     name="Mods", value=recent_activity[0].mods, inline=True)

                            # embed.set_author(name=f"{usernameosu} achieved score on {recent_activity[0].beatmapset.artist} - {recent_activity[0].beatmapset.title} [{recent_activity[0].beatmap.version}]", icon_url=recent_activity[0]._user.avatar_url)

                            thumbnail_url = f'https://b.ppy.sh/thumb/{recent_activity[0].beatmapset.id}l.jpg'
                            embed.set_thumbnail(url=thumbnail_url)

                            # embed.add_field(
                            #     name="PP", value=recent_activity[0].pp, inline=True)

                            # embed.add_field(
                            #     name="Difficulty", value=recent_activity[0].beatmap.difficulty_rating, inline=True)

                            # embed.add_field(
                            #     name="BPM", value=recent_activity[0].beatmap.bpm, inline=True)

                            # embed.add_field(
                            #     name="Combo", value=recent_activity[0].max_combo, inline=True)

                            # embed.add_field(
                            #     name="Grade", value=recent_activity[0].rank.name, inline=True)

                            # embed.add_field(
                            #     name="Passed", value=recent_activity[0].passed, inline=True)

                            # embed.add_field(
                            #     name="Played Date", value=recent_activity[0].created_at, inline=True)

                            beatmap_length = recent_activity[0].beatmap.total_length
                            minutes, seconds = divmod(beatmap_length, 60)
                            beatmap_length_str = f"{minutes:02d}:{seconds:02d}"
                            embed.add_field(name='Beatmap Information', value=f"{beatmap_length_str} ~ CS{recent_activity[0].beatmap.cs} AR{recent_activity[0].beatmap.ar} ~ BPM{recent_activity[0].beatmap.bpm} ~ {recent_activity[0].beatmap.difficulty_rating}★")
                            
                            mapperusername = api.user(recent_activity[0].beatmap.user_id, mode="osu").username
                            mapperuseravatarurl = api.user(recent_activity[0].beatmap.user_id, mode="osu").avatar_url

                            last_updated1 = recent_activity[0].beatmap.last_updated
                            timestamp1 = int(last_updated1.timestamp())
                            discord_time1 = datetime.fromtimestamp(timestamp1)
                            embed.set_footer(text=f"Mapped by {mapperusername} ✦ Ranked on {discord_time1}", icon_url=mapperuseravatarurl)

                            await channel.send(embed=embed)

                            previous_activity[user_id] = recent_activity[0]
                    print("SCORE")
                    print(user_id)
                    print("SCORE checked")
            except IndexError:
                print(
                    f"Recent activity is empty for user ID {user_id}. Skipping to next iteration.")
            await asyncio.sleep(20)