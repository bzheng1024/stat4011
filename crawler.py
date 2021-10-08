import requests
from bs4 import BeautifulSoup
import time
import csv

# fp = open('./data/anime.csv', 'wt', newline='', encoding='utf_8_sig')
# writer = csv.writer(fp)
# writer.writerow(("name", "points", "views", "danmakus", "rating_score", "rating_num", "follows", "share", "reply", "tags"))

headers = {
    'content-type': 'application/json',
    'origin': 'https://probuildstats.com',
    'referer': 'https://probuildstats.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

url = "https://u.gg/api"

payload = '{"operationName":"ChampionMatchList","variables":{"opponentChampionId":null,"isWorlds":true,"pageNumber":1},"query":"query ChampionMatchList($championId: Int, $league: String, $recommendedFirst: Boolean, $role: String, $victoryOnly: Boolean, $opponentChampionId: Int, $leagueBlocklist: [String], $teamBlocklist: [String], $proBlocklist: [String], $pageNumber: Int, $isWorlds: Boolean, $proTeam: String) {\n  getProChampionMatchList(\n    championId: $championId\n    league: $league\n    recommendedFirst: $recommendedFirst\n    role: $role\n    victoryOnly: $victoryOnly\n    opponentChampionId: $opponentChampionId\n    leagueBlocklist: $leagueBlocklist\n    teamBlocklist: $teamBlocklist\n    proBlocklist: $proBlocklist\n    pageNumber: $pageNumber\n    isWorlds: $isWorlds\n    proTeam: $proTeam\n  ) {\n    matchList {\n      calculatedRole\n      championId\n      cs\n      completedItems\n      currentTeam\n      finalBuild\n      gold\n      itemPath {\n        itemId\n        timestamp\n        type\n        __typename\n      }\n      jungleCs\n      killParticipation\n      matchDuration\n      matchId\n      isWorlds\n      matchTimestamp\n      normalizedName\n      proInfo {\n        league\n        currentTeam\n        officialName\n        tags\n        __typename\n      }\n      opponentChampionId\n      proLeague\n      regionId\n      runes {\n        perk0\n        perk1\n        perk2\n        perk3\n        perk4\n        perk5\n        primaryStyle\n        subStyle\n        __typename\n      }\n      statShards\n      seasonId\n      skillEvolveOrders\n      skillOrders\n      summonerSpells\n      teamId\n      totalAssists\n      totalDeaths\n      totalKills\n      version\n      win\n      __typename\n    }\n    mostPopularItems {\n      itemId\n      pickRate\n      __typename\n    }\n    mostPopularBoots {\n      itemId\n      pickRate\n      __typename\n    }\n    __typename\n  }\n}\n"}'
pro_payload = '{"operationName":"ProMatch","variables":{"matchId":5495056272,"regionId":"euw1","version":"11_20"},"query":"query ProMatch($matchId: Int!, $regionId: String!, $version: String!) {\n  getProMatch(matchId: $matchId, regionId: $regionId, version: $version) {\n    teams {\n      teamId\n      win\n      participants {\n        assists\n        calculatedRole\n        championId\n        cs\n        damage\n        deaths\n        finalBuild\n        jungleCs\n        kills\n        officialName\n        rank {\n          lastUpdatedAt\n          losses\n          lp\n          promoProgress\n          queueType\n          rank\n          role\n          seasonId\n          tier\n          wins\n          __typename\n        }\n        runes {\n          perk0\n          perk1\n          perk2\n          perk3\n          perk4\n          perk5\n          primaryStyle\n          subStyle\n          __typename\n        }\n        statShards\n        summonerName\n        summonerSpells\n        wardsPlaced\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}'
pro_list_payload = '{"operationName":"ProMatchList","variables":{"proNormalizedName":"ruler","pageNumber":0},"query":"query ProMatchList($proNormalizedName: String, $recommendedFirst: Boolean, $role: String, $victoryOnly: Boolean, $pageNumber: Int) {\n  getProMatchList(\n    proNormalizedName: $proNormalizedName\n    recommendedFirst: $recommendedFirst\n    role: $role\n    victoryOnly: $victoryOnly\n    pageNumber: $pageNumber\n  ) {\n    calculatedRole\n    championId\n    cs\n    completedItems\n    currentTeam\n    finalBuild\n    gold\n    itemPath {\n      itemId\n      timestamp\n      type\n      __typename\n    }\n    jungleCs\n    killParticipation\n    matchDuration\n    matchId\n    isWorlds\n    matchTimestamp\n    normalizedName\n    proInfo {\n      league\n      currentTeam\n      officialName\n      tags\n      __typename\n    }\n    opponentChampionId\n    proLeague\n    regionId\n    runes {\n      perk0\n      perk1\n      perk2\n      perk3\n      perk4\n      perk5\n      primaryStyle\n      subStyle\n      __typename\n    }\n    statShards\n    seasonId\n    skillEvolveOrders\n    skillOrders\n    summonerSpells\n    teamId\n    totalAssists\n    totalDeaths\n    totalKills\n    version\n    win\n    __typename\n  }\n}\n"}'
home_page_payload = '{"operationName": "LiveGameFeed","variables": {"isWorlds": true,"role": null,"proLeague": null},"query": "query LiveGameFeed($isWorlds: Boolean, $proLeague: String, $role: String) {\n  getLatestWorldsMatchList(isWorlds: $isWorlds, league: $proLeague, role: $role) {\n    calculatedRole\n    championId\n    cs\n    completedItems\n    currentTeam\n    finalBuild\n    gold\n    itemPath {\n      itemId\n      timestamp\n      type\n      __typename\n    }\n    jungleCs\n    killParticipation\n    matchDuration\n    matchId\n    isWorlds\n    matchTimestamp\n    normalizedName\n    proInfo {\n      league\n      currentTeam\n      officialName\n      tags\n      __typename\n    }\n    opponentChampionId\n    proLeague\n    regionId\n    runes {\n      perk0\n      perk1\n      perk2\n      perk3\n      perk4\n      perk5\n      primaryStyle\n      subStyle\n      __typename\n    }\n    statShards\n    seasonId\n    skillEvolveOrders\n    skillOrders\n    summonerSpells\n    teamId\n    totalAssists\n    totalDeaths\n    totalKills\n    version\n    win\n    __typename\n  }\n}\n"}'

result = requests.post(url=url, headers=headers, data=pro_list_payload).json()
print(result)
time.sleep(0.5)

# writer.writerow((name, points, views, danmakus, rating_score, rating_num, follows, share, reply, tags))
# print(name + " success!")
# fp.close()
