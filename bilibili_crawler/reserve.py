import requests
from bs4 import BeautifulSoup
import time
import csv


fp = open('./data/reserve.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("id", "name", "grade", "category", "tag_name", "book_num"))

headers = {
    'referer': 'https://game.bilibili.com/platform/discover/collection/131479460384860708?name=%E6%96%B0%E6%B8%B8%E9%A2%84%E7%BA%A6',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
for page_num in range(1, 15):
    url = "http://le3-api.game.bilibili.com/pc/game/discover/page_game_list?collection_id=131479460384860708&page_num="+str(page_num)+"&page_size=40"
    res = requests.get(url, headers=headers).json()
    time.sleep(0.5)
    data_list = res['data']
    if data_list:
        for i in range(len(data_list)):
            data = data_list[i]
            id = data['game_base_id']
            print("page_num = ", page_num, "; list_num = ", i)

            # get game tag
            tag_headers = {
                'referer': 'https://www.biligame.com/detail/?id='+str(id),
                'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            }
            tag_url = "http://line1-h5-pc-api.biligame.com/game/detail/content?game_base_id="+str(id)
            tag_res = requests.get(tag_url, headers=tag_headers).json()
            time.sleep(0.5)
            tag_data = tag_res['data']
            tag_list = tag_data['tag_list']
            tag_name = []
            for tag in tag_list:
                tag_name.append(tag['name'])
            print("get tag successfully!")

            # get book number
            book_num_url = "http://line1-h5-pc-api.biligame.com/game/detail/gameinfo?game_base_id="+str(id)
            book_num_res = requests.get(book_num_url, headers=tag_headers).json()
            time.sleep(0.5)
            book_num = book_num_res['data']['book_num']
            print("get book number successfully!")

            name = data['game_name']
            grade = data['grade']
            if 'category' in data:
                category = data['category']['name']
            else:
                category = None
            writer.writerow((id, name, grade, category, tag_name, book_num))
    else:
        break
fp.close()

