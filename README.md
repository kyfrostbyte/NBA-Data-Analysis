# Overview

{Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}

{Provide a description of the data set that you are analyzing.  Include the link of where you obtained the data.}

{Describe your purpose for writing this software to analyze the data.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

{List the questions and the answers you found by doing this analysis.}

# Development Environment
- imported: tabulate
- pip install pandas matplotlib seaborn
- mpld3
{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](http://url.link.goes.here)
* [Web Site Name](http://url.link.goes.here)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1
* Item 2
* Item 3



Finished things:

Requests, formats and displays the current NBA Standings
nba_standings = NBA_api.format_nba_standings(NBA_api.make_request(NBA_STANDINGS_ENDPOINT))
NBA_api.display_nba_standings(nba_standings)


Create instance of CSVReader, read and print data
csv_reader = CSVReader(NBA_SALARIES_CSV_PATH)
csv_reader.read_csv()
data = csv_reader.get_data()
for x in data:
    print(x)


 # Modifying data (for example, adding a new game)
    new_game = {"Date": "2024-02-10", "TeamA": "Team1", "TeamB": "Team2", "Result": "Team1 Wins"}
    games.append(new_game)

    # Writing back to CSV
    csv_reader.write_csv(NBA_GAMES_CSV_PATH, games)


  Create instances of each API league-specific object
    NBA_api = NBA_API(NBA_API_KEY, BASE_URL)
    NFL_api = NFL_API(NFL_API_KEY, BASE_URL)
    CBB_api = CBB_API(CBB_API_KEY, BASE_URL)
    NBA_api2 = NBA_API2(NBA_API2_KEY, BASE_URL_2)

    player_data = NBA_api2.players(1, 2023)
    team = NBA_api2.teams_by_id()

    print("")

    nba_standings = NBA_api.format_nba_standings(NBA_api.make_request(NBA_STANDINGS_ENDPOINT))
    NBA_api.display_nba_standings(nba_standings)

