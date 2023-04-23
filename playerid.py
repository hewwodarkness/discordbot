import requests
from bs4 import BeautifulSoup

url = 'https://osu.ppy.sh/rankings/osu/performance?country=UA&page=5#scores'

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print('Error:', e)
    exit()

html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

player_table = soup.find('table', class_='ranking-page-table')
if player_table is None:
    print('Error: table not found')
    exit()

user_ids = []
players = player_table.find_all('tr')
for player in players[1:]:  # Skip the first row (table header)
    player_link = player.find('a', class_='ranking-page-table__user-link-text')
    if player_link:
        player_id = player_link['href'].split('/')[-2]
        user_ids.append(player_id)
print('user_ids =', user_ids)
