# import requests

# api_url = "https://api.gog.com/v2/games"

# # Include your API key in the headers
# headers = {
#     "Authorization": "Bearer YOUR_API_KEY_HERE",
# }

# # Make a GET request to the games endpoint
# response = requests.get(api_url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     # Process the data as needed for your pipeline
# else:
#     print(f"Error: {response.status_code}")



# # import requests

# # def fetch_games(api_key):
# #     api_url = "https://api.gog.com/v2/games"

# #     headers = {
# #         "Authorization": f"Bearer {api_key}",
# #     }

# #     response = requests.get(api_url, headers=headers)

# #     if response.status_code == 200:
# #         print(response.json().get("products", []))
# #         return response.json().get("products", [])
# #     else:
# #         print(f"Error: {response.status_code}")
# #         return []

# # def parse_game_data(game_data):
# #     parsed_data = []
# #     for game in game_data:
# #         game_info = {
# #             "title": game.get("title", "N/A"),
# #             "release_date": game.get("release_date", "N/A"),
# #             "price": game.get("price", {}).get("final_amount", "N/A"),
# #             # Add more fields as needed
# #         }
# #         parsed_data.append(game_info)
# #         print(parsed_data)
# #     return parsed_data

# # def main():
# #     api_key = "YOUR_API_KEY_HERE"
    
# #     # Fetch games from the GOG API
# #     games_data = fetch_games(api_key)

# #     # Parse the game data
# #     parsed_data = parse_game_data(games_data)

# #     # Process the parsed data (e.g., store in a database, analyze, etc.)
# #     for game_info in parsed_data:
# #         print(game_info)

# # if __name__ == "__main__":
# #     main()


from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/gog/games', methods=['GET'])
def get_gog_games():
    api_key = "YOUR_GOG_API_KEY"  # Replace with your actual GOG API key

    api_url = "https://api.gog.com/v2/games"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    # Make a GET request to the GOG API
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response from the GOG API
        games_data = response.json().get("products", [])
        
        # Return the parsed data as JSON using Flask's jsonify
        return jsonify(games_data)
    else:
        # Handle errors, return an appropriate JSON response
        error_message = f"Error: {response.status_code}"
        return jsonify({"error": error_message})

if __name__ == '__main__':
    app.run(debug=True)