import requests
from datetime import datetime
from tabulate import tabulate


class NFL_API:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

    def make_request(self, endpoint):
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}

        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.get(url, headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error {response.status_code}: {response.text}")
                return None

        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None

