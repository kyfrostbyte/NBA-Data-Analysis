# GLOBAL CONSTANT VARIABLES

# Base URL for all APIs
BASE_URL = 'http://api.sportsdata.io/v3'

# League specific keys
NBA_API_KEY = '51536294c400471ca1d2c6a67248662a'
NFL_API_KEY = 'e45c713d7b0a42c9b6dd28c25525b9bb'
CBB_API_KEY = '12e59c0e076d432b92eeb0f5de831dc5'


# NBA ENDPOINTS
NBA_SCORES_ENDPOINT = f"/nba/stats/json/BoxScores/2024-01-30?key={NBA_API_KEY}"
NBA_STANDINGS_ENDPOINT = f"/nba/scores/json/Standings/2024?key={NBA_API_KEY}"
NBA_PLAYER_SEASON_STATS_ENDPOINT = f"/nba/stats/json/PlayerSeasonStats/2023?key={NBA_API_KEY}"
# NBA FILE PATHS
NBA_SALARIES_CSV_PATH = "assets/nba_salaries.csv"

# CBB ENDPOINTS
CBB_SCORES_ENDPOINT = f"/cbb/scores/json/ScoresBasic/2024-01-30?key={CBB_API_KEY}"

# NFL ENDPOINTS
NFL_SCORES_ENDPOINT = f"/nfl/scores/json/ScoresByDate/2024-01-28?key={NFL_API_KEY}"

