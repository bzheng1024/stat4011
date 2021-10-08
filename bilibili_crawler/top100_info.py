import requests
from bs4 import BeautifulSoup
import csv
import time
from videozone import *
import re
from collections import Counter
import pandas as pd


def get_oid(aid):
    response = requests.get("https://www.bilibili.com/video/av" + str(aid), headers=headers)
    match = r'cid=(.*?)&aid'
    oid = re.search(match, response.text).group().replace('cid=', '').replace('&aid', '')
    return oid


danmaku = []
danmaku_zone = []
danmaku_time = []
danmaku_totaltime = []

fp = open('./data/top100_info.csv', 'wt', newline='', encoding='utf_8_sig')
info_writer = csv.writer(fp)
info_writer.writerow(
    ("name", "address", "view", "barrage", "like", "coin", "favorite", "share", "history_rank", "tag_name", "zone"))

headers = {
    'referer': 'https://www.bilibili.com/video/BV1QE411e7Ht/?spm_id_from=333.788.videocard.2',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
url = 'https://bilibili.com/v/popular/rank/all'
top_res = requests.get(url)
top_soup = BeautifulSoup(top_res.text, 'lxml')
top_list = top_soup.find_all('div', class_='info')
for i in top_list:
    name = i.a.text
    addr = i.find('a')['href'][2:]
    bv = addr[23:]
    stat_url = "https://api.bilibili.com/x/web-interface/view?cid=141553944&bvid=" + bv
    stat_res = requests.get(stat_url, headers=headers, timeout=6).json()
    time.sleep(0.5)
    data = stat_res['data']
    tid = data['tid']
    duration = data['duration']
    zone = video_zone(tid)
    stat = data['stat']
    aid = stat['aid']
    oid = get_oid(aid)
    view = stat['view']
    barrage = stat['danmaku']
    like = stat['like']
    coin = stat['coin']
    favorite = stat['favorite']
    share = stat['share']
    his_rank = stat['his_rank']

    tag_url = "https://api.bilibili.com/x/web-interface/view/detail/tag?aid=" + str(aid)
    tag_res = requests.get(tag_url, headers=headers, timeout=6).json()
    time.sleep(0.5)
    tag_data = tag_res['data']
    tag_name = []
    for tag in tag_data:
        tag_name.append(tag['tag_name'])

    danmaku_url = "http://comment.bilibili.com/" + str(oid) + ".xml"
    danmaku_res = requests.get(danmaku_url, headers=headers, timeout=6)
    danmaku_res.encoding = 'utf-8'
    danmaku_soup = BeautifulSoup(danmaku_res.text, 'xml')
    danmaku_list = danmaku_soup.find_all('d')
    for j in danmaku_list:
        danmaku.append(j.text)
        danmaku_zone.append(zone)
        danmaku_time.append(str(j).split(",")[0][6:])
        danmaku_totaltime.append(duration)
    info_writer.writerow((name, addr, view, barrage, like, coin, favorite, share, his_rank, tag_name, zone))
fp.close()

pd.DataFrame({'danmaku': danmaku, 'zone': danmaku_zone, 'time': danmaku_time, 'total_time': danmaku_totaltime}).to_csv(
    './data/top100_danmaku.csv', index=False, encoding='utf_8')

# danmaku = Counter(danmaku)
#
# with open('C:/Users/user/Desktop/git/bilibili_crawler/top100_danmaku.csv', 'wt', encoding='utf_8') as f:
#     danmaku_writer = csv.writer(f)
#     danmaku_writer.writerows(danmaku.items())
# pd.DataFrame(danmaku).to_csv('C:/Users/user/Desktop/git/bilibili_crawler/top100_danmaku.csv', index=False)
