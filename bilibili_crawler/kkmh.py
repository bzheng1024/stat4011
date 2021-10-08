import requests
from bs4 import BeautifulSoup
import time
import csv

fp = open('./data/kkmh.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("type", "rank", "title", "author", "tags", "description", "popularity", "likes", "follows", "comments"))

headers = {
    'referer': 'https://www.kuaikanmanhua.com/ranking/5',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

pop_rank_url = "https://www.kuaikanmanhua.com/v2/pweb/rank/topics?rank_id=9"
pop_rank_res = requests.get(pop_rank_url, headers).json()
time.sleep(0.5)
pop_data_list = pop_rank_res["data"]["rank_info"]["topics"]
if pop_data_list:
    for i in range(0, 10):
        info = pop_data_list[i]
        tags = info["tags"]
        title = info["title"]
        author = info["user"]["nickname"]
        description = info["description"]
        id = info["id"]

        url = "https://api.kkmh.com/v1/topics/" + str(id)
        res = requests.get(url, headers).json()
        time.sleep(1)
        follows = res["data"]["fav_count"]
        comments = res["data"]["comments_count"]
        likes = res["data"]["likes_count"]
        popularity = res["data"]["popularity_value"]

        writer.writerow(("人气榜", i+1, title, author, tags, description, popularity, likes, follows, comments))
        print(title + " success!")
    print("人气榜 finished!\n")


sale_rank_url = "https://www.kuaikanmanhua.com/v2/pweb/rank/topics?rank_id=4"
sale_rank_res = requests.get(sale_rank_url, headers).json()
time.sleep(0.5)
sale_data_list = sale_rank_res["data"]["rank_info"]["topics"]
if sale_data_list:
    for i in range(0, 10):
        info = sale_data_list[i]
        tags = info["tags"]
        title = info["title"]
        author = info["user"]["nickname"]
        description = info["description"]
        id = info["id"]

        url = "https://api.kkmh.com/v1/topics/" + str(id)
        res = requests.get(url, headers).json()
        time.sleep(1)
        follows = res["data"]["fav_count"]
        comments = res["data"]["comments_count"]
        likes = res["data"]["likes_count"]
        popularity = res["data"]["popularity_value"]

        writer.writerow(("畅销榜", i+1, title, author, tags, description, popularity, likes, follows, comments))
        print(title + " success!")
    print("畅销榜 finished!")
fp.close()

