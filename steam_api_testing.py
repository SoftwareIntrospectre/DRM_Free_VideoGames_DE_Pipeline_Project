# used to connect to Steam APIs
import requests

# used to parse the API data
import json

# used to import environment variables
import os

def get_steam_user_info(api_key, steam_id):
    # Construct the URL for Steam API summary endpoint
        # url = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}'
        url = f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json'

        # Make the GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
                # Parse the JSON response
            data = response.json()

            if "response" in data:
                 response_data = data["response"]

            for key in response_data.keys():
                 if "games" in response_data:
                      for game in response_data["games"]:
                           print(f"Game: {game}")

        else:
            print(f"Error: {response.status_code} - {response.text}")


# can connect app_id to this enpoint to get the game's name. Will use in a join later.
def get_steam_game_name(app_id):
    url = f'https://store.steampowered.com/api/appdetails?appids={app_id}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        app_details = data[str(app_id)]
        
        if app_details['success']:
            return app_details['data']['name']
        else:
            return f"Error retrieving details for app ID {app_id}"
    else:
        return f"Error: {response.status_code} - {response.text}"   

if __name__ == "__main__":
    
    STEAM_API_KEY = os.environ.get("STEAM_API_KEY")
    STEAM_USER_ID = os.environ.get("STEAM_USER_ID")
    get_steam_user_info(STEAM_API_KEY, STEAM_USER_ID)
    
    steam_game_id = 1888160  # example ID. Will be dynamic later
    steam_game_name = get_steam_game_name(steam_game_id)
    print(f"App Name for App ID '{steam_game_id}' is: '{steam_game_name}'")         