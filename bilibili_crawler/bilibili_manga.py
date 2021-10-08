import requests
from bs4 import BeautifulSoup
import time
import csv

fp = open('./data/bilibili_manga.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("rank", "title", "author", "status", "tags", "月票数", "interact_value", "comments"))

headers = {
    'referer': 'https://manga.bilibili.com/ranking/ticket',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

rank_url = "https://manga.bilibili.com/twirp/comic.v1.Comic/HomeFans"
rank_post_data = {'device': 'pc', 'platform': 'web', 'type': 1, 'last_month_offset': 0, 'last_week_offset': 0}
rank_res = requests.post(rank_url, data=rank_post_data).json()
time.sleep(0.5)
rank_data_list = rank_res["data"]["comics"]
if rank_data_list:
    for i in range(0, 10):
        info = rank_data_list[i]
        title = info["title"]
        author = info["author"]
        id = info["comic_id"]
        fans = info["fans"]
        status = "完结" if info["is_finish"] else "连载中"

        tags_list = info["styles"]
        tags = []
        for tag in tags_list:
            tags.append(tag['name'])

        url = "https://manga.bilibili.com/twirp/comic.v1.Comic/ComicDetail"
        post_data = {'device': 'pc', 'platform': 'web', 'comic_id': str(id)}
        res = requests.post(url, data=post_data).json()
        time.sleep(1)
        interact_value = res["data"]["interact_value"]

        comments_url = "https://api.bilibili.com/x/v2/reply?type=22&oid=" + str(id)
        comments_res = requests.get(comments_url, headers).json()
        time.sleep(1)
        comments = comments_res["data"]["page"]["acount"]

        writer.writerow((i+1, title, author, status, tags, fans, interact_value, comments))
        print(title + " success!")

fp.close()

