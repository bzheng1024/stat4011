import requests
from bs4 import BeautifulSoup
import time
import csv

fp = open('./data/iqiyi.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("name", "meta", "hotIndex", "tags", "description", "id", "score"))

headers = {
    'referer': 'https://www.iqiyi.com/ranks/rise',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


url = "https://pcw-api.iqiyi.com/strategy/pcw/data/topReboBlock?cid=4&dim=hour&type=rise&len=25&pageNumber=1"
res = requests.get(url, headers).json()
time.sleep(0.5)
data_list = res["data"]["formatData"]["list"]
if data_list:
    for i in range(0, 10):
        info = data_list[i]
        aid = info["aid"]
        hotIndex = info["hotIndex"]
        meta = info["meta"]
        name = info["name"]

        get_vid_url = "https://pcw-api.iqiyi.com/albums/album/avlistinfo?aid=" + str(aid) + "&page=1"
        get_vid_res = requests.get(get_vid_url, headers).json()
        time.sleep(1)
        vid = get_vid_res["data"]["epsodelist"][0]["tvId"]

        vid_url = "https://qiquancdn.if.iqiyi.com/video/v2?id=" + str(vid)
        vid_res = requests.get(vid_url, headers).json()
        time.sleep(1)
        tags = vid_res["items"]["info"]["data"]["category"]
        score = vid_res["items"]["info"]["data"]["score"]
        description = vid_res["items"]["info"]["data"]["description"]
        id = vid_res["items"]["info"]["data"]["id"]

        writer.writerow((name, meta, hotIndex, tags, description, id, score))
        print(name + " success!")
fp.close()

