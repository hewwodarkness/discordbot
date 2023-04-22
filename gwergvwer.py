  # async def ss_count(message):
        #     user_id = "5249196"
        #     grant_type = "client_credentials"
        #     scope = "public"
        #     # Send a request to the authorization server to obtain an access token
        #     response = requests.post(
        #         "https://osu.ppy.sh/oauth/token",
        #         data={
        #             "client_id": client_id,
        #             "client_secret": client_secret,
        #             "grant_type": grant_type,
        #             "scope": scope,
        #         },
        #     )

        #     # Parse the response JSON to extract the access token
        #     access_token = response.json()["access_token"]
        #     # print(access_token)

        #     headers = {
        #         "Authorization": f"Bearer {access_token}",
        #         "Content-Type": "application/json",
        #         "Accept": "application/json",
        #         "x-api-version": str(20220707),
        #     }
        #     if message.content.startswith("!ss"):
        #         words = message.content.split()
        #         if len(words) < 2:
        #             response = "Please provide a user ID."
        #         else:
        #             user_id = words[1]
        #             response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
        #             if response.ok:
        #                 user_data = response.json()
        #                 grade_counts = user_data["statistics"]['grade_counts']['ss']
        #                 grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
        #                 username = user_data["username"]
        #                 sum = grade_counts + grade_counts1
        #                 response = f'The user with ID {username} has {sum} SS scores.'
        #             else:
        #                 response = f'Request failed with status {response.status_code} and message: {response.text}'
        #             await message.reply(response)
    

    # async def ss_check():
    #     prev_grade_counts = None
    #     prev_grade_counts1 = None
    #     channel = client.get_channel(1085597937255596082)
    #     while True:
    #         user_id = "11196666"
    #         grant_type = "client_credentials"
    #         scope = "public"

    #         # Send a request to the authorization server to obtain an access token
    #         response = requests.post(
    #             "https://osu.ppy.sh/oauth/token",
    #             data={
    #                 "client_id": client_id,
    #                 "client_secret": client_secret,
    #                 "grant_type": grant_type,
    #                 "scope": scope,
    #             },
    #         )

    #         # Parse the response JSON to extract the access token
    #         access_token = response.json()["access_token"]
    #         # print(access_token)

    #         headers = {
    #             "Authorization": f"Bearer {access_token}",
    #             "Content-Type": "application/json",
    #             "Accept": "application/json",
    #             "x-api-version": str(20220707),
    #         }
            
    #         response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
    #         if response.ok:
    #             user_data = response.json()
    #             grade_counts = user_data["statistics"]['grade_counts']['ss']
    #             grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
    #             sum = grade_counts + grade_counts1
                
    #             # Check if the values changed since the last call
    #             if prev_grade_counts is not None and prev_grade_counts != grade_counts:
    #                 await channel.send(f"The ss count for user {user_id} changed from {prev_grade_counts} to {grade_counts}")
    #             if prev_grade_counts1 is not None and prev_grade_counts1 != grade_counts1:
    #                 await channel.send(f"The ssh count for user {user_id} changed from {prev_grade_counts1} to {grade_counts1}")
                
    #             # Update the previous values
    #             prev_grade_counts = grade_counts
    #             prev_grade_counts1 = grade_counts1


    #         await asyncio.sleep(1)
    async def ss_check():
        prev_grade_counts = {}
        prev_grade_counts1 = {}
        channel = client.get_channel(1085597937255596082)
        while True:
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

            for user_id in user_ids:
                response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
                if response.ok:
                    user_data = response.json()
                    grade_counts = user_data["statistics"]['grade_counts']['ss']
                    grade_counts1 = user_data["statistics"]['grade_counts']['ssh']
                    sum = grade_counts + grade_counts1
                    username = user_data["username"]
                    # Check if the values changed since the last call
                    if user_id in prev_grade_counts and prev_grade_counts[user_id] != grade_counts:
                        await channel.send(f"The ss count for user {username} changed from {prev_grade_counts[user_id]} to {grade_counts}")
                    if user_id in prev_grade_counts1 and prev_grade_counts1[user_id] != grade_counts1:
                        await channel.send(f"The ssh count for user {username} changed from {prev_grade_counts1[user_id]} to {grade_counts1}")

                    # Update the previous values
                    prev_grade_counts[user_id] = grade_counts
                    prev_grade_counts1[user_id] = grade_counts1

            await asyncio.sleep(1)

    async def rank_check():
        prev_global_rank = {}
        channel = client.get_channel(1085597937255596082)
        while True:
            for user_id in user_ids:
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

            await asyncio.sleep(1)

    async def pp_check():
        prev_pp = {}
        channel = client.get_channel(1085597937255596082)
        while True:
            for user_id in user_ids:
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

                response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
                if response.ok:
                    user_data = response.json()
                    pp = user_data["statistics"]['pp']
                    username = user_data["username"]

                    # Check if the value changed since the last call
                    if user_id in prev_pp and prev_pp[user_id] != pp:
                        await channel.send(f"The PP for user {username} changed from {prev_pp[user_id]} to {pp}")

                    # Update the previous value
                    prev_pp[user_id] = pp

            await asyncio.sleep(1)
