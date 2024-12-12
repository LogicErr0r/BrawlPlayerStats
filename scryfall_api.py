import requests

def get_commander_color(commander_name):
    url = f"https://api.scryfall.com/cards/named?exact={commander_name}"
    response = requests.get(url)
    if response.status_code == 200:
        card_data = response.json()
        return card_data['color_identity']
    else:
        print(f"Error: {response.status_code}")
        print("Commander Not Found")
        return None

