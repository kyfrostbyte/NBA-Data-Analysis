import requests
import datetime
import json
# from menu.menu import menu
import matplotlib as mpl
import matplotlib.pyplot as plt
from api.nba_api import NBA_API
from api.cbb_api import CBB_API
from api.nfl_api import NFL_API
from api.nba_api2 import NBA_API2
from csv_handler.csv_reader import CSVReader
from data_analyzer.analyzer import DataAnalyzer
from config.constants import *

if __name__ == '__main__':
    analyzer = DataAnalyzer(NBA_GAMES_PATH, NBA_GAME_DETAILS_PATH, NBA_PLAYERS_PATH, NBA_RANKINGS_PATH, NBA_TEAMS_PATH)

    # Rank players by consistency
    ranked_players = analyzer.rank_players_by_consistency()
