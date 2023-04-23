if user_id in prev_grade_counts and (prev_grade_counts[user_id] != statistics['grade_counts']['ss'] or user_id in prev_grade_counts1 and prev_grade_counts1[user_id] != statistics['grade_counts']['ssh']):
                                ss_count = statistics['grade_counts']['ss']
                                ssh_count = statistics['grade_counts']['ssh']
                                total_count = ss_count + ssh_count
 
                                embed = discord.Embed(color=0x00ff00)
                                # embed.add_field(name=field_name.capitalize(), value=field_value, inline=False)
                                country_code = user_data["country_code"].lower()
                                # flag_url = f"https://flagcdn.com/48x36/{country_code}.png"
                                avatar_url = user_data["avatar_url"]
                                embed.set_thumbnail(url=avatar_url)
                                embed.set_author(name=(username + " - " + str(statistics['pp']) + "pp (#" + str(statistics['global_rank']) + ") (" + str(user_data["country_code"]) + "#" + str(statistics['country_rank']) + ")"), url=f"https://osu.ppy.sh/users/{user_data['id']}", icon_url=avatar_url)
                                
                                formatted_score = '{:.1f} bln'.format(float(statistics['ranked_score']) / 10**9)
                                embed.add_field(name="Ranked Score", value=formatted_score, inline=True)

                                formatted_score = '{:.1f} bln'.format(float(statistics['total_score']) / 10**9)
                                embed.add_field(name="Total Score", value=formatted_score, inline=True)

                                embed.add_field(name="Play Count", value=statistics['play_count'], inline=True)

                                embed.add_field(name="Play Time", value=(str(round(statistics['play_time'] / 60 / 60, 2))) + " hours", inline=True)
                                embed.add_field(name="Level", value=(str(statistics['level']['current']) + "." + str(statistics['level']['progress'])), inline=True)
                                embed.add_field(name="Hit Accuracy", value=round(statistics['hit_accuracy'],2), inline=True)

                                grade_counts = user_data["statistics"]['grade_counts']['ss']
                                grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                                sum = grade_counts + grade_counts1

                                embed.add_field(name="SS Amount", value=sum, inline=True)
                                embed.add_field(name="Hit Count", value=statistics["total_hits"], inline=True)
                                embed.add_field(name="Followers", value=user_data["follower_count"], inline=True)

                                embed.add_field(name="SS Count", value=f"{prev_grade_counts.get(user_id, 0) + prev_grade_counts1.get(user_id, 0)} -> {total_count}", inline=False)
                                print("SS changed")
                                await channel.send(embed=embed)