import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import time
import csv
import re


# get all champions name in LOL
def get_champion_list():
    headers = {
        'referer': 'https://euw.op.gg/champion/statistics',
        'accept-language': 'zh,zh-TW',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    url = "https://euw.op.gg/champion/statistics"
    res = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(res)
    list = soup.find('div', class_='champion-index__champion-list').find_all('div', class_='champion-index__champion-item__name')
    champion_list = []
    for data in list:
        champion_list.append(data.text)
    return champion_list


# get players info list
def get_player_list():
    headers = {
        'referer': 'https://www.trackingthepros.com/bootcamp',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }
    url = "https://www.trackingthepros.com/d/list_bootcamp"
    list = requests.get(url=url, headers=headers).json()['data']
    player_list = []
    for data in list:

        role = data['role']

        # take away the coaches and substitude players
        if role[-1] == ')' or role[-1] == 'h':
            continue

        # get team name
        team_re = re.search(r'.*> (.*)<.*', data['team'])
        team = team_re.group(1)

        # get player id
        summoner = data['plug']

        # get link to rank records list on OPGG
        opgg_re = re.search(r'.*href=\'(.*)\' target.*', data['summoner'])
        opgg = opgg_re.group(1)

        player_list.append({'role': role, 'team': team, 'player': summoner, 'link': opgg})
    return player_list


current_time = int(time.time())
player_list = get_player_list()
champion_list = get_champion_list()

headers = {
    'referer': 'https://www.op.gg/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'accept-language': 'zh,zh-TW'
}

game_record = defaultdict(lambda: defaultdict(list))

for player_data in player_list:        
    url = player_data['link']
    res = requests.get(url, headers=headers).text
    time.sleep(0.1)
    soup = BeautifulSoup(res, 'lxml')
    
    summoner_id = soup.find('div', class_='GameListContainer')['data-summoner-id']
    start_time = current_time
    
    idx = 0

    # the website load rank records list iteratively by timestamp of start time
    while(int(start_time) > 1633017600): # data from 2021-10-01 00:00:00
        url = 'https://euw.op.gg/summoner/matches/ajax/averageAndList/startInfo=' + str(start_time) + '&summonerId=' + str(summoner_id)
        try:
            res = requests.get(url, headers=headers).json()['html']
        except:
            break
        time.sleep(0.1)
        soup = BeautifulSoup(res)
        game_list = soup.find_all('div', class_='GameItemWrap')

        for game in game_list:
            game = game.findChild('div', recursive=False)
            game_result = (game['data-game-result'] == 'win')
            game_id = game['data-game-id']
            game_time = game['data-game-time']
            game_type = game.find('div', class_='GameType')['title']

            start_time = game_time

            # game time before 2021-10-01 00:00:00
            if (int(start_time) <= 1633017600):
                break
            
            # game mode not ranked solo
            if (game_type != '单人排位'):
                continue

            # game has been saved in the game_record
            if game_id in game_record.keys():
                idx = idx + 1
                print(player_data['team'], player_data['role'], player_data['player'], idx, 'saved!')
                continue

            url = 'https://euw.op.gg/summoner/matches/ajax/detail/gameId='+str(game_id)+'&summonerId='+str(summoner_id)+'&gameTime='+str(game_time)
            res = requests.get(url, headers=headers).text
            time.sleep(0.1)
            soup = BeautifulSoup(res, 'lxml')

            try:
                win_list = soup.find('table', class_='GameDetailTable Result-WIN').find('tbody', class_='Content').find_all('tr')
                lose_list = soup.find('table', class_='GameDetailTable Result-LOSE').find('tbody', class_='Content').find_all('tr')
            except:
                continue

            idx = idx + 1

            # get all champion records and append the data into game_record
            for win_champion in win_list:
                win_champion_name = win_champion.find_all('div')[0]['title']
                game_record[game_id]['win'].append(win_champion_name)

            for lose_champion in lose_list:
                lose_champion_name = lose_champion.find_all('div')[0]['title']
                game_record[game_id]['lose'].append(lose_champion_name)
            
            print(player_data['team'], player_data['role'], player_data['player'], idx, 'success!')


# save the game records of champions
f_games = open('../data/games_champion.csv', 'wt', newline='', encoding='utf_8_sig')
w_games = csv.writer(f_games)
w_games.writerow(("gameid", "win1", "win2", "win3", "win4", "win5", "lose1", "lose2", "lose3", "lose4", "lose5"))
for gameid, record in game_record.items():
    win_list = record['win']
    lose_list = record['lose']
    w_games.writerow((gameid, win_list[0], win_list[1], win_list[2], win_list[3], win_list[4], lose_list[0], lose_list[1], lose_list[2], lose_list[3], lose_list[4]))
f_games.close()


# get the paired combination of champions
pair_list = [(champion_list[i],champion_list[j]) for i in range(len(champion_list)) for j in range(i+1, len(champion_list))]


# init the counter of paired combination to 0
result_dict = defaultdict(list)
for p1, p2 in pair_list:
	result_dict[(p1 ,p2)] = [0, 0]


for game_id, record in game_record.items():
	win_list = record['win']
	lose_list = record['lose']
	for winner in win_list:
		for loser in lose_list:
			if (winner, loser) in result_dict.keys():
				result_dict[(winner, loser)][0] += 1
			elif (loser, winner) in result_dict.keys():
				result_dict[(loser, winner)][1] += 1


# save the records of champions pair
f_records = open('../data/records_champion.csv', 'wt', newline='', encoding='utf_8_sig')
w_records = csv.writer(f_records)
w_records.writerow(("champion1", "champion2", "win1", "win2"))
for (champion1, champion2), res_list in result_dict.items():
    w_records.writerow((champion1, champion2, res_list[0], res_list[1]))
f_records.close()
