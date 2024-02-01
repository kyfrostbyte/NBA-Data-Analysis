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
- 
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
