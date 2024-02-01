import requests
from datetime import datetime
from tabulate import tabulate


class CBB_API:
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

    def display_cbb_scores(self, scores):
        if scores:
            formatted_nba_scores = self.format_cbb_game(scores)
            if formatted_nba_scores:
                for game in formatted_nba_scores:
                    print("Date:", datetime.strptime(game["Date"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d"))
                    print("Home Team:", game["HomeTeam"], "Score:", game["HomeScore"])
                    print("Away Team:", game["AwayTeam"], "Score:", game["AwayScore"])
                    print("-" * 30)

    def format_cbb_game(self, data):
        formatted_game = {}
        try:
            formatted_game = {
                "GameID": data.get("GameID"),
                "Season": data.get("Season"),
                "SeasonType": data.get("SeasonType"),
                "Status": data.get("Status"),
                "Date": data.get("Day"),
                "DateTime": data.get("DateTime"),
                "AwayTeam": data.get("AwayTeam"),
                "HomeTeam": data.get("HomeTeam"),
                "AwayTeamID": data.get("AwayTeamID"),
                "HomeTeamID": data.get("HomeTeamID"),
                "Updated": data.get("Updated"),
                "TournamentID": data.get("TournamentID"),
                "Bracket": data.get("Bracket"),
                "Round": data.get("Round"),
                "AwayTeamSeed": data.get("AwayTeamSeed"),
                "HomeTeamSeed": data.get("HomeTeamSeed"),
                "IsClosed": data.get("IsClosed"),
                "GameEndDateTime": data.get("GameEndDateTime"),
                "NeutralVenue": data.get("NeutralVenue"),
                "DateTimeUTC": data.get("DateTimeUTC"),
                "AwayTeamScore": data.get("AwayTeamScore"),
                "HomeTeamScore": data.get("HomeTeamScore"),
            }
            return formatted_game

        except ValueError as e:
            print(f"Error parsing JSON: {e}")
            return None
