from config.constants import *
from api.nba_api import NBA_API
from api.cbb_api import CBB_API
from api.nfl_api import NFL_API
from csv_handler.csv_reader import CSVReader

import requests
import datetime
import json
# from menu.menu import menu
import matplotlib as mpl
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Create instances of each API league-specific object
    NBA_api = NBA_API(NBA_API_KEY, BASE_URL)
    NFL_api = NFL_API(NFL_API_KEY, BASE_URL)
    CBB_api = CBB_API(CBB_API_KEY, BASE_URL)

    nba_test = NBA_api.make_request(NBA_PLAYER_SEASON_STATS_ENDPOINT)
    for player in nba_test:
        player['Points'] = round(player['Points'])

    sorted_nba = sorted(nba_test, key=lambda team: team['Points'], reverse=True)
    NBA_api.display_nba_player_stats(sorted_nba)





