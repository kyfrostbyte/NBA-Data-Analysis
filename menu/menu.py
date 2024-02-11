# menu/__init__.py
import pandas as pd
from tabulate import tabulate
from config.constants import *
from api.nba_api2 import NBA_API2
from api.nba_api import NBA_API

class Menu:

    def __init__(self):
        self.df = None
        self.teams_df = None
        self.total_points = None

    def load_data(self):
        # Load your data and perform necessary operations
        self.df = pd.read_csv(NBA_GAMES_PATH)
        self.teams_df = pd.read_csv(NBA_TEAMS_PATH)

        self.df['GAME_DATE_EST'] = pd.to_datetime(self.df['GAME_DATE_EST'])
        df_2016 = self.df[self.df['SEASON'] == 2016]
        points_df = df_2016[['TEAM_ID_home', 'PTS_home', 'TEAM_ID_away', 'PTS_away']]
        points_df.columns = ['TEAM_ID', 'POINTS_HOME', 'OPPONENT_TEAM_ID', 'POINTS_AWAY']
        self.total_points = pd.concat([points_df[['TEAM_ID', 'POINTS_HOME']],
                                       points_df[['OPPONENT_TEAM_ID', 'POINTS_AWAY']].rename(
                                           columns={'OPPONENT_TEAM_ID': 'TEAM_ID', 'POINTS_AWAY': 'POINTS_HOME'})])
        self.total_points = self.total_points.groupby('TEAM_ID')['POINTS_HOME'].sum().reset_index()
        self.total_points = self.total_points.merge(self.teams_df[['TEAM_ID', 'CITY', 'NICKNAME']], on='TEAM_ID',
                                                    how='left')
        self.total_points['TEAM_NAME'] = self.total_points['CITY'] + ' ' + self.total_points['NICKNAME']
        self.total_points = self.total_points[['TEAM_NAME', 'POINTS_HOME']]
        self.total_points = self.total_points.sort_values(by='POINTS_HOME', ascending=False)
        self.total_points = self.total_points.reset_index(drop=True)

    def display_menu(self):
        print("\n======= NBA Data Menu =======")
        print("1. Display Total Points by Team (2016 Season - CSV Based)")
        print("2. Display Current NBA Standings (API Based)")
        print("3. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-2): ")

            if choice == '1':
                self.display_total_points()
                print("")
            elif choice == '2':
                self.display_current_rankings()
                print("")
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
                print("")

    def display_total_points(self):
        print("\nTotal Points by Team:\n")
        table = tabulate(self.total_points, headers='keys', tablefmt='pretty', showindex=False)
        print(table)

    def display_current_rankings(self):
        NBA_api = NBA_API(NBA_API_KEY, BASE_URL)
        nba_standings = NBA_api.format_nba_standings(NBA_api.make_request(NBA_STANDINGS_ENDPOINT))
        NBA_api.display_nba_standings(nba_standings)
