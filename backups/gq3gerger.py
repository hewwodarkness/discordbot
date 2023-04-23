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
