import requests
from datetime import datetime
from tabulate import tabulate
from config.constants import *

class NBA_API2:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def players(self, team, season):
        url = "https://api-nba-v1.p.rapidapi.com/players"

        querystring = {"team": team, "season": season}

        headers = {
            "X-RapidAPI-Key": "f1209231d1msh4921fffcfc193e2p13fa0bjsnaa6b8925a8eb",
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }
        try:
            response = requests.get(url, headers=headers, params=querystring)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error {response.status_code}: {response.text}")
                return None

        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None


    def teams_by_id(self):
        import requests

        url = "https://api-nba-v1.p.rapidapi.com/players"

        querystring = {"name": 'Trae Young'}
        headers = {
            "X-RapidAPI-Key": "f1209231d1msh4921fffcfc193e2p13fa0bjsnaa6b8925a8eb",
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        response = response.json()

        print(response)
        count = 1

        for item in response['response']:
            if item["name"] == 'Trae Young':
                print(item["id"], item["name"])
