# GLOBAL CONSTANT VARIABLES

# SPORTSDATA.IO
BASE_URL = 'http://api.sportsdata.io/v3'

# RAPID API
BASE_URL_2 = 'https://api-nba-v1.p.rapidapi.com'

# League specific keys
NBA_API_KEY = '51536294c400471ca1d2c6a67248662a'
NBA_API2_KEY = 'f1209231d1msh4921fffcfc193e2p13fa0bjsnaa6b8925a8eb'
NFL_API_KEY = 'e45c713d7b0a42c9b6dd28c25525b9bb'
CBB_API_KEY = '12e59c0e076d432b92eeb0f5de831dc5'


# SportsData.io NBA ENDPOINTS
NBA_SCORES_ENDPOINT = f"/nba/stats/json/BoxScores/2024-01-30?key={NBA_API_KEY}"
NBA_STANDINGS_ENDPOINT = f"/nba/scores/json/Standings/2024?key={NBA_API_KEY}"
NBA_PLAYER_SEASON_STATS_ENDPOINT = f"/nba/stats/json/PlayerSeasonStats/2023?key={NBA_API_KEY}"

# RapidAPI ENDPOINTS

NBA_IDS = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 38, 40, 41]

NBA_PLAYERS_ENDPOINT = "players"

# NBA FILE PATHS
NBA_GAMES_PATH = "assets/games.csv"
NBA_GAME_DETAILS_PATH = "assets/games_details.csv"
NBA_PLAYERS_PATH = "assets/players.csv"
NBA_RANKINGS_PATH = "assets/ranking.csv"
NBA_TEAMS_PATH = "assets/teams.csv"

# CBB ENDPOINTS
CBB_SCORES_ENDPOINT = f"/cbb/scores/json/ScoresBasic/2024-01-30?key={CBB_API_KEY}"

# NFL ENDPOINTS
NFL_SCORES_ENDPOINT = f"/nfl/scores/json/ScoresByDate/2024-01-28?key={NFL_API_KEY}"


# CSV FORMATS DEFINITIONS
# games.csv
GAMES_DATA_TYPES = {
    'TEAM_ID': int,
    'LEAGUE_ID': int,
    'SEASON_ID': int,
    'STANDINGSDATE': 'datetime64',
    'CONFERENCE': str,
    'TEAM': str,
    'G': int,
    'W': int,
    'L': int,
    'W_PCT': float,
    'HOME_RECORD': str,
    'ROAD_RECORD': str,
    'RETURNTOPLAY': str,
}

# game_details.csv
GAME_DETAILS_DATA_TYPES = {
    'GAME_ID': int,
    'TEAM_ID': int,
    'TEAM_ABBREVIATION': str,
    'TEAM_CITY': str,
    'PLAYER_ID': int,
    'PLAYER_NAME': str,
    'NICKNAME': str,
    'START_POSITION': str,
    'COMMENT': str,
    'MIN': str,
    'FGM': float,
    'FGA': float,
    'FG_PCT': float,
    'FG3M': float,
    'FG3A': float,
    'FG3_PCT': float,
    'FTM': float,
    'FTA': float,
    'FT_PCT': float,
    'OREB': float,
    'DREB': float,
    'REB': float,
    'AST': float,
    'STL': float,
    'BLK': float,
    'TO': float,
    'PF': float,
    'PTS': float,
    'PLUS_MINUS': float,
}

# players.csv
PLAYERS_DATA_TYPES = {
    'PLAYER_NAME': str,
    'TEAM_ID': int,
    'PLAYER_ID': int,
    'SEASON': int,
}

# rankings.csv
RANKINGS_DATA_TYPES = {
    'TEAM_ID': int,
    'LEAGUE_ID': int,
    'SEASON_ID': int,
    'STANDINGSDATE': str,
    'CONFERENCE': str,
    'TEAM': str,
    'G': int,
    'W': int,
    'L': int,
    'W_PCT': float,
    'HOME_RECORD': str,
    'ROAD_RECORD': str,
    'RETURNTOPLAY': str,
}


# teams.csv
TEAMS_DATA_TYPES = {
    'LEAGUE_ID': int,
    'TEAM_ID': int,
    'MIN_YEAR': int,
    'MAX_YEAR': int,
    'ABBREVIATION': str,
    'NICKNAME': str,
    'YEARFOUNDED': int,
    'CITY': str,
    'ARENA': str,
    'ARENACAPACITY': float,
    'OWNER': str,
    'GENERALMANAGER': str,
    'HEADCOACH': str,
    'DLEAGUEAFFILIATION': str,
}

