# CourtSide
Python web scraper to retrieve NCAA Men's Basketball Statistics

## Description
CourtSide is a web scraper which parses data returned from teamrankings.com in order to retrieve specific stats from specific teams from specific years. There are over 100 stats that are accessible through CourtSide

## Usage

Each NCAAMBB object function follows the same style. Each function takes two arguments: The team we want the stat for, and the last year of the season (for example the 2017-2018 season would be requested by specifying 2018). If the year is not specified, data for the most recent season will be returned.

~~~~
import CourtSide
myStats = NCAAMBB()
myStats.getPPG("Michigan St","2018")
> "80.2"
~~~~

## runner.py
The script runner.py provides a framework in which CourtSide is used to predict matchup results. 

#### Input file format
runner.py takes a file listing all the matchups to predict in the form:
~~~~
Duke
Virginia //Duke vs Virginia
Michigan St
Michigan //Michigan St vs Michigan
~~~~

#### Script functionality
The script will then verify that each team listed in the file can be found on teamrankings.com. Once this is complete, it will execute alg.calculateOffense(finder,team,opponent) against each matchup pair to determine a winner. The function alg.calculateOffense is determined by an import at the top of the runner.py script. By changing this import to a different file (algorithms.alg1 is used by default), different scoring prediction algorithms can be easily swapped out. 

#### Output file format
runner.py saves the results to winners.txt in the form:
~~~~
Duke
Michigan St
~~~~
This is useful because winners.txt could then be used as the matchup file for the next round of a tournament

## Features for the Future
- [X] Caching system to reduce redundant web calls
- [ ] Support for running an entire competition at once, not just a single round
- [ ] Complete function to search for a team

