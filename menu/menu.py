# menu/__init__.py
import pandas as pd
from tabulate import tabulate
from config.constants import *
from api.nba_api import NBA_API
import matplotlib.pyplot as plt


class Menu:

    def __init__(self):
        self.df = None
        self.teams_df = None
        self.total_points = None

    def load_data(self):
        # Load your data and perform necessary operations
        self.df = pd.read_csv(NBA_GAMES_PATH)
        self.teams_df = pd.read_csv(NBA_TEAMS_PATH)

        # Format data for later use
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
        print("3. Display League Wide Scoring Trend Chart from 2004-2022")
        print("4. Display 3 Point Percentage by Year")
        print("5. Quit")

    def run(self):
        # Terminal loop to navigate through menu options
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                print("Please Select a View:")
                print("1: Terminal View")
                view_choice = input("2: Chart View")
                if view_choice == '1':
                    self.display_total_points()
                elif view_choice == '2':
                    self.display_chart()
                else:
                    print("Invalid choice. Please enter a valid option.")
                print("")
            elif choice == '2':
                self.display_current_rankings()
                print("")
            elif choice == '3':
                print("Please Select a View:")
                print("1: Yearly Trend")
                view_choice = input("2: Daily Trend")
                if view_choice == '1':
                    self.display_scoring_trend_year()
                elif view_choice == '2':
                    self.display_scoring_trend_day()
                else:
                    print("Invalid choice. Please enter a valid option.")
            elif choice == '4':
                self.display_fg3_pct_change_year()
                print("")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")
                print("")

    def display_total_points(self):
        print("\nTotal Points by Team:\n")
        # Grab pre-formatted data and display
        self.total_points['POINTS_HOME'] = self.total_points['POINTS_HOME'].astype(int)
        table = tabulate(self.total_points, headers='keys', tablefmt='pretty', showindex=False)
        print(table)

    def display_current_rankings(self):
        # Create instance of API Object
        NBA_api = NBA_API(NBA_API_KEY, BASE_URL)

        # Make request and format data
        nba_standings = NBA_api.format_nba_standings(NBA_api.make_request(NBA_STANDINGS_ENDPOINT))

        # Display Data
        NBA_api.display_nba_standings(nba_standings)

    def display_chart(self, save_path='charts_output/chart.png'):
        if self.total_points is not None:
            plt.figure(figsize=(12, 8))
            teams = self.total_points['TEAM_NAME']  # x
            points = self.total_points['POINTS_HOME']  # y
            plt.bar(teams, points, color='skyblue')
            plt.ylabel('Total Points')
            plt.title('Total Points by Team (2016 Season)')
            plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
            plt.tight_layout()  # Adjust layout to prevent clipping of labels

            # Save and display the chart
            plt.savefig(save_path)
            plt.show()
        else:
            print("Data not loaded. Please load data first.")

    def display_scoring_trend_day(self):
        df = pd.read_csv(NBA_GAMES_PATH)

        # Convert the 'GAME_DATE_EST' column to datetime format
        df['GAME_DATE_EST'] = pd.to_datetime(df['GAME_DATE_EST'])

        # Group by 'GAME_DATE_EST' and calculate the average points per game
        average_points_per_game = df.groupby('GAME_DATE_EST')['PTS_home'].mean()

        # Plot
        plt.figure(figsize=(12, 6))
        plt.plot(average_points_per_game.index, average_points_per_game, marker='o', linestyle='-')
        plt.title('Average Points per Game Over Time')
        plt.xlabel('Game Date')
        plt.ylabel('Average Points per Game')
        plt.grid(True)
        plt.show()

    def display_scoring_trend_year(self):
        df = pd.read_csv(NBA_GAMES_PATH)

        # Convert the 'GAME_DATE_EST' column to datetime format
        df['GAME_DATE_EST'] = pd.to_datetime(df['GAME_DATE_EST'])

        # Extract the year from the 'GAME_DATE_EST' column
        df['Year'] = df['GAME_DATE_EST'].dt.year

        # Group by 'Year' and calculate the average points per game
        average_points_per_year = df.groupby('Year')['PTS_home'].mean()

        # Plot
        plt.figure(figsize=(12, 6))
        plt.plot(average_points_per_year.index, average_points_per_year, marker='o', markersize=10, linestyle='solid',
                 color='red', linewidth=4)
        plt.title('Average Points per Game Over Time (Grouped by Year)')
        plt.xlabel('Year')
        plt.ylabel('Average Points per Game')
        plt.grid(True)
        plt.show()

    def display_fg3_pct_change_year(self):
        df = pd.read_csv(NBA_GAMES_PATH)

        # Convert the 'GAME_DATE_EST' column to datetime format
        df['GAME_DATE_EST'] = pd.to_datetime(df['GAME_DATE_EST'])

        # Extract the year from the 'GAME_DATE_EST' column
        df['Year'] = df['GAME_DATE_EST'].dt.year

        # Group by 'Year' and calculate the average three-point percentage per year
        avg_fg3_pct_per_year = df.groupby('Year')['FG3_PCT_home'].mean()

        # Plot the change in three-point percentage over time
        plt.figure(figsize=(12, 6))
        plt.plot(avg_fg3_pct_per_year.index, avg_fg3_pct_per_year, marker='o', linestyle='-', markersize=8)
        plt.title('Change in Three-Point Percentage per Year')
        plt.xlabel('Year')
        plt.ylabel('Average Three-Point Percentage')
        plt.ylim(.25, .45)  # Set y-axis limit to (0, 1) for percentage
        plt.grid(True)
        plt.show()
