# CourtSide
NCAA Mens Basketball Stats API

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


## Checklist
[ ] Complete function to search for a team

