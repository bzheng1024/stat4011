# STAT4011-proj1
stat4011 course project 1


## Data Source
[Tracking the Pro](https://www.trackingthepros.com/bootcamp)

[OPGG](https://euw.op.gg)


## Requirement of Environment
`pip install -r requirement.txt`


## Players Data
1. run `python crawler/players.py` under this dir to generate:

    + `list_player.csv` including the players info
    + `games_player.csv` including all the games of players
    + `records_player.csv` including the win/lose records of players pair

2. use PivotTable in `games_player.csv` to generate: 

    + `records_noob.xlsx` including the win/lose records of player-noob pair

3. append `records_player.csv` and `records_noob.xlsx` together to generate:

    + `BT_ranking.xlsx` including all the win/lose records for our analysis


## Champions Data
**NOTE: we did not include the analysis of champions data in this report coz the page limits, but we have crawled the corresponding data, which could be used for further study.**

run `python crawler/champions.py` under this dir to generate:

+ `games_champion.csv` including all the games of champion
+ `records_champion.csv` including the win/lose records of champion pair


## Analysis
check `main.R` for more info

the result list generated: `result/rankinglist.csv`

## ELO
check `ELO.Rmd` for more info

