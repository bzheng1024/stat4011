import requests
from bs4 import BeautifulSoup
import time
import csv

fp = open('./data/chinese.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("name", "points", "views", "danmakus", "rating_score", "rating_num", "follows", "share", "reply", "tags"))

headers = {
    'referer': 'https://www.bilibili.com/v/popular/rank/guochan',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

tags_headers = {
    'referer': 'https://www.bilibili.com/bangumi/media/md28232073/?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

rank_url = "https://api.bilibili.com/pgc/season/rank/web/list?day=3&season_type=4"
rank_res = requests.get(rank_url, headers).json()
time.sleep(0.5)
rank_data_list = rank_res["data"]["list"]
if rank_data_list:
    for i in range(0, 10):
        info = rank_data_list[i]
        season_id = info["season_id"]
        points = info["pts"]
        follows = info["stat"]["follow"]

        season_url = "http://api.bilibili.com/pgc/view/web/season?season_id=" + str(season_id)
        season_res = requests.get(season_url, headers).json()
        time.sleep(3)
        md_id = season_res["result"]["media_id"]
        name = season_res["result"]["season_title"]
        rating_num = season_res["result"]["rating"]["count"]
        rating_score = season_res["result"]["rating"]["score"]
        data = season_res["result"]["stat"]
        views = data["views"]
        danmakus = data["danmakus"]
        share = data["share"]
        reply = data["reply"]

        tags_url = "https://www.bilibili.com/bangumi/media/md" + str(md_id)
        tags_res = requests.get(tags_url, tags_headers)
        tags_soup = BeautifulSoup(tags_res.text, 'lxml')
        tags_list = tags_soup.find_all('span', class_='media-tag')
        tags = []
        for j in tags_list:
            tags.append(j.text)

        writer.writerow((name, points, views, danmakus, rating_score, rating_num, follows, share, reply, tags))
        print(name + " success!")
fp.close()

