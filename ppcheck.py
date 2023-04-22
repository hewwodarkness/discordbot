import requests
from tokendiscord import TOKEN
from tokendiscord import client_id
from tokendiscord import client_secret

async def pp_check(message):
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
        
        response = requests.get(f"https://osu.ppy.sh/api/v2/users/{user_id}/osu", headers=headers)
        if response.ok:
            user_data = response.json()
            pp = user_data["statistics"]['global_rank']
            response = f'The user with ID {user_id} has {pp} SS scores.'
        chan = 1085597937255596082
        await message.chan.send(response)