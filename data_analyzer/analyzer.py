import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config.constants import *

class DataAnalyzer:
    def __init__(self, games_path, game_details_path, players_path, rankings_path, teams_path):
        self.games = pd.DataFrame(self._read_csv(games_path, GAMES_DATA_TYPES))
        self.game_details = pd.DataFrame(self._read_csv(game_details_path, GAME_DETAILS_DATA_TYPES))
        self.players = self._read_csv(players_path, PLAYERS_DATA_TYPES)
        self.rankings = self._read_csv(rankings_path, RANKINGS_DATA_TYPES, parse_dates=['STANDINGSDATE'])
        self.teams = self._read_csv(teams_path, TEAMS_DATA_TYPES)

    def _read_csv(self, file_path, column_data_types=None, parse_dates=None):
        try:
            return pd.read_csv(file_path, dtype=column_data_types, parse_dates=parse_dates, low_memory=False)
        except Exception as e:
            print(f"Error reading CSV file {file_path}: {e}")
            raise

    def get_team_id_from_abv(self, abv):
        team = self.teams[self.teams['ABBREVIATION'] == abv]

        if not team.empty:
            return team.iloc[0]['TEAM_ID']
        else:
            return None

    # analyzer.py

    def rank_players_by_consistency(self):
        df = self.game_details.head(20)
        name = df['PLAYER_NAME']
        id = df['PLAYER_ID']
        print(f"PLAYER_NAME, PLAYER_ID")

        for i in name, id:
            print(f"{name} : {id}")




