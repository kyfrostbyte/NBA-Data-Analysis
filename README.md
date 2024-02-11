# Overview
This is a program that analyses NBA data in a few different ways. The data comes from either an API or CSV, depending on the users input. Between the two data sources, there is a 
pretty vast amount of data. Just one of the CSV files alone as over 26 thousand rows. My purpose for choosing the data set was to see what information could be gleaned from
an activity that is incredibly inconsistent at times. With basketball nothing is certain. Any shot could be made or missed, so I was interested to see how things have changed over time 
in spite of that. I also wanted to see what niche statistics I could come up with

I wanted to get more familiar to parsing large amounts of data. I have done a lot of projects revolving around APIS recently, and wanted to practice more on CSVs. 
By doing this project I was able to practice handling large amounts of data from multiple sources and making them work together. It also gave me an opportunity to learn how 
structure slightly more complex python files that require more classes and directories to stay organized. This was actually my first time uses classes in pythons, so I was
interested to see how it differs from languages like c# and c++.

Here are the links to my data sources:

[Sports.Io API](https://sportsdata.io/developers/api-documentation/nba)

[Rapid API: api-nba](https://rapidapi.com/api-sports/api/api-nba/)

[CSV Files](https://www.kaggle.com/datasets/nathanlauga/nba-games?resource=download)

<br/>

## Software Demo
[Demo Link](http://youtube.link.goes.here)

# Data Analysis Results

### What were the best scoring teams in the in a given year? 
- The top 5 teams were the Golden State Warriors, Cleveland Cavaliers, Boston Celtics, Houston Rockets, and Washington Wizards<br/>

### What are the current NBA rankings?
- Top 3 in East: Boston Celtics, Cleveland Cavaliers, Milwaukee Bucks
- Top 3 in West: Minnesota Timberwolves, Denver Nuggets, Oklahoma City Thunder <br/>

### How has scoring changed over the last 20 years? 
- In 2003 the league average was just over 90 PPG. In 2022 that was up to almost 114 PPG. So in 20 years the league scores 24 more PPG on average <br/>

### Has the average NBA player gotten better at shooting 3s over time?
- Somewhat, but not enough to account for the 24 more PPG. In 2003, the average NBA player shot about 34% from 3, and in 2022 it was up to almost 36%<br/>

# Development Environment
- IDE: PyCharm <br/>
- Language: Python <br/>

### Library list:
* Pandas
* Requests
* Tabulate
* Matplotlib



# Useful Websites

* [Basketball Reference](https://www.basketball-reference.com/teams/GSW/2016_games.html)
* [MatPlotLib](https://matplotlib.org/stable/)
* [Pandas Youtube Tutorial Series](https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&ab_channel=CoreySchafer)

# Future Work

* Implement all the data I was able to including the CBB and NFL API, as well as the players, rankings, and game_details CSV. Learn how to get them to merge without breaking.
* Create function to show trend of 3pt FG Attempt, and see if that accounts for scoring increase
* Analyse fouls over time. See if the refs really are a larger factor today
* Look at standard deviation of shooting percentage by player. Find the most consistent shooters in the league
* Look for correlations between defensive/offensive statistics, see which one is a bigger factor in win/loss ration
* Get charts to overlay properly. Like show the monthly and yearly trends at the same time
* Get NBA names to work on chart preview
* Implement better system for handling all the API endpoints
* Figure out how to format data easier. Come up with a one size fits all method for each API?
