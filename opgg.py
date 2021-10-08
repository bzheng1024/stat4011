import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import time
import csv
import re
import time


ROLE2ROW = {'Top': 0, 'Jungle': 1, 'Mid': 2, 'ADC': 3, 'Support': 4}


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
        if role[-1] == ')' or role[-1] == 'h':
            continue
        team_re = re.search(r'.*> (.*)<.*', data['team'])
        team = team_re.group(1)
        summoner = data['plug']
        opgg_re = re.search(r'.*href=\'(.*)\' target.*', data['summoner'])
        opgg = opgg_re.group(1)
        player_list.append({'role': role, 'team': team, 'player': summoner, 'link': opgg})
    return player_list


current_time = int(time.time())
player_list = get_player_list()
player_name_list = []
for player in player_list:
    player_name_list.append(player['player'])


f_players = open('./data/players.csv', 'wt', newline='', encoding='utf_8_sig')
w_players = csv.writer(f_players)
w_players.writerow(("team", "role", "player", "id"))

game_record = defaultdict(lambda: defaultdict(list))


headers = {
    'referer': 'https://www.op.gg/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'accept-language': 'zh,zh-TW'
}

for player_data in player_list:
    url = player_data['link']
    res = requests.get(url, headers=headers).text
    time.sleep(0.1)
    soup = BeautifulSoup(res, 'lxml')
    summoner_name_re = re.search(r'.*userName=(.*)\Z', player_data['link'])
    summoner_name = summoner_name_re.group(1)
    summoner_id = soup.find('div', class_='GameListContainer')['data-summoner-id']
    start_time = current_time

    w_players.writerow((player_data['team'], player_data['role'], player_data['player'], summoner_name))
    
    idx = 0

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
            if (int(start_time) <= 1633017600):
                break
            
            if (game_type != '单人排位'):
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

            if game_result:
                if 'isRequester' not in win_list[ROLE2ROW[player_data['role']]].attrs['class']:
                    continue
            else:
                if 'isRequester' not in lose_list[ROLE2ROW[player_data['role']]].attrs['class']:
                    continue

            # requester_re = re.compile(r'.*isRequester.*')
            # row_requester = soup.find('tr', {'class': requester_re})
            # if row_requester is None:
            #     continue

            idx = idx + 1

            for win_player in win_list:
                win_player_name = win_player.find('td', class_='SummonerName Cell').find('a').text
                game_record[game_id]['win'].append(win_player_name)

            for lose_player in lose_list:
                lose_player_name = lose_player.find('td', class_='SummonerName Cell').find('a').text
                game_record[game_id]['lose'].append(lose_player_name)
            
            print(player_data['team'], player_data['role'], player_data['player'], idx, 'success!')

f_players.close()


f_records = open('./data/records.csv', 'wt', newline='', encoding='utf_8_sig')
w_records = csv.writer(f_records)
w_records.writerow(("game_id", "win1", "win2", "win3", "win4", "win5", "lose1", "lose2", "lose3", "lose4", "lose5"))

for game_id, record in game_record.items():
    win_list = record['win']
    lose_list = record['lose']
    for idx, name in enumerate(win_list):
        if name not in player_name_list:
            win_list[idx] = '__NOOB__'
    for idx, name in enumerate(lose_list):
        if name not in player_name_list:
            lose_list[idx] = '__NOOB__'
    w_records.writerow((game_id, win_list[0], win_list[1], win_list[2], win_list[3], win_list[4], lose_list[0], lose_list[1], lose_list[2], lose_list[3], lose_list[4]))

f_records.close()

print('debug')