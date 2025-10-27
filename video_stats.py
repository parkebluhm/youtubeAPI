import os
import requests
import json

from dotenv import load_dotenv

load_dotenv(dotenv_path = "/Users/parkebluhm/data_projects/youtube_elt/.env")

API_KEY = os.getenv("API_KEY")

CHANNEL_HANDLE = "MrBeast"

#testing changes pushing to dev and merging to main

def get_playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        channel_items = data["items"][0]

        channel_playlist_id = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        print(channel_playlist_id)

        return channel_playlist_id
    
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "__main__":
    get_playlist_id()