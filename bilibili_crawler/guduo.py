import requests
from bs4 import BeautifulSoup
import time
import csv

fp = open('./data/guduo.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("rank", "name", "release_date", "douban_rating", "baidu_index", "comment", "play_count", "global_hot", "platforms"))

headers = {
    'referer': 'http://data.guduodata.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

rank_url = "http://data.guduodata.com/show/datalist?type=DAILY&category=DRAMA&date=2021-03-17&t=1616396512931"
rank_res = requests.get(rank_url, headers).json()
time.sleep(0.5)
rank_data_list = rank_res["data"]
if rank_data_list:
    for i in range(0, 10):
        info = rank_data_list[i]
        name = info["name"]
        release_date = info["release_date"]
        douban_rating = info["douban"]
        baidu_index = info["baidu_index"]
        comment = info["comment"]
        play_count = info["play_count"]
        hot = info["gdi"]
        platforms = info["platforms"]

        writer.writerow((i+1, name, release_date, douban_rating, baidu_index, comment, play_count, hot, platforms))

fp.close()

