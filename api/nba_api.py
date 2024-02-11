import requests
from datetime import datetime
from tabulate import tabulate

class NBA_API:


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

    def format_nba_standings(self, data):
        formatted_nba_standings = []
        for team in data:
            formatted_game = {
                "Season": team['Season'],
                "SeasonType": team["SeasonType"],
                "TeamID": team["TeamID"],
                "Key": team["Key"],
                "City": team["City"],
                "Name": team["Name"],
                "Conference": team["Conference"],
                "Division": team["Division"],
                "Wins": team["Wins"],
                "Losses": team["Losses"],
                "Percentage": team["Percentage"],
                "ConferenceWins": team["ConferenceWins"],
                "ConferenceLosses": team["ConferenceLosses"],
                "DivisionWins": team["DivisionWins"],
                "DivisionLosses": team["DivisionLosses"],
                "HomeWins": team["HomeWins"],
                "HomeLosses": team["HomeLosses"],
                "AwayWins": team["AwayWins"],
                "AwayLosses": team["AwayLosses"],
                "LastTenWins": team["LastTenWins"],
                "LastTenLosses": team["LastTenLosses"],
                "PointsPerGameFor": team["PointsPerGameFor"],
                "PointsPerGameAgainst": team["PointsPerGameAgainst"],
                "Streak": team["Streak"],
                "GamesBack": team["GamesBack"],
                "StreakDescription": team["StreakDescription"]}
            formatted_nba_standings.append(formatted_game)
        return formatted_nba_standings

    def display_nba_standings(self, nba_standings):
        eastern_standings = [team for team in nba_standings if team["Conference"] == "Eastern"]
        western_standings = [team for team in nba_standings if team["Conference"] == "Western"]

        # Sort standings for both conferences based on Wins
        sorted_eastern_standings = sorted(eastern_standings, key=lambda team: team['Wins'], reverse=True)
        sorted_western_standings = sorted(western_standings, key=lambda team: team['Wins'], reverse=True)

        max_teams = max(len(sorted_eastern_standings), len(sorted_western_standings))
        print(f"{'Eastern':^48}|{'Western':^45}")
        print("-" * 90)
        print(f"{'Team':<25}{'Wins':<10}{'Losses':<12} | {'Team':<25}{'Wins':<10}{'Losses':<10}")

        for i in range(max_teams):
            eastern_team = sorted_eastern_standings[i] if i < len(sorted_eastern_standings) else {}
            western_team = sorted_western_standings[i] if i < len(sorted_western_standings) else {}

            # Truncate long names
            eastern_team_name = f"{eastern_team.get('City', '')} {eastern_team.get('Name', ''):<25}"[:25]
            eastern_wins = f"{eastern_team.get('Wins', ''):<10}"
            eastern_losses = f"{eastern_team.get('Losses', ''):<10}"

            western_team_name = f"{western_team.get('City', '')} {western_team.get('Name', ''):<25}"[:25]
            western_wins = f"{western_team.get('Wins', ''):<10}"
            western_losses = f"{western_team.get('Losses', ''):<10}"


            print(f"{eastern_team_name} {eastern_wins} {eastern_losses} | {western_team_name} {western_wins} {western_losses}")

    def format_game_data(self, data):
        formatted_games = []
        try:
            # Assuming data is a list of games
            for game in data:
                game_info = game.get("Game")  # Access the nested "Game" dictionary

                if game_info:
                    formatted_game = {
                        "Date": game_info.get("Day"),
                        "HomeTeam": game_info.get("HomeTeam"),
                        "AwayTeam": game_info.get("AwayTeam"),
                        "HomeScore": game_info.get("HomeTeamScore"),
                        "AwayScore": game_info.get("AwayTeamScore"),
                    }
                    formatted_games.append(formatted_game)
                else:
                    print("Error: 'Game' key not found in data")

            return formatted_games

        except ValueError as e:
            print(f"Error parsing JSON: {e}")
            return None

    def get_scores_by_date(self, date):
        endpoint = f"scores/json/ScoresBasic/{date}"
        return self.make_request(endpoint)

    # Add more methods for other API endpoints as needed

    # Usage
    def display_scores(self, scores):
        if scores:
            formatted_nba_scores = self.format_game_data(scores)
            if formatted_nba_scores:
                for game in formatted_nba_scores:
                    print("Date:", datetime.strptime(game["Date"], "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d"))
                    print("Home Team:", game["HomeTeam"], "Score:", game["HomeScore"])
                    print("Away Team:", game["AwayTeam"], "Score:", game["AwayScore"])
                    print("-" * 30)


    def display_nba_player_stats(self, data):
        for player in data:
            print(player["Name"], player["Points"])