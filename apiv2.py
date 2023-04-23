import requests

# Set the necessary parameters
user_id = "1"
include_fails = "0"
mode = "osu"
limit = "8"
offset = "1"

# Set the API endpoint URL
url = f"https://osu.ppy.sh/api/v2/users/{user_id}/scores/best?include_fails={include_fails}&mode={mode}&limit={limit}&offset={offset}"

# Set the headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "x-api-version": str(20220707),
}

# Send the GET request with the headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response JSON
    print(response.json())
else:
    # Print the error message
    print(f"Error: {response.status_code} - {response.json()['error']['message']}")
