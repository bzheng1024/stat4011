import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import json

def myfun(tag):

    return tag.is_empty_element

headers = {
    'referer': 'https://movie.douban.com/tv/#!type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

tv_res = requests.get("https://movie.douban.com/subject/30228394/?tag=%E7%83%AD%E9%97%A8&from=gaia_video", headers=headers, timeout=10)
time.sleep(1)
tv_res.encoding = 'utf-8'
tv_soup = BeautifulSoup(tv_res.text, 'xml')
# tags_list = movie_soup.find_all('span', property_='v:genre')
# tags = []
# for tag in tags_list:
#     tags.append(tag.text)
# movie_info = movie_soup.find('div', id='info')
# span = info.find_all('span')
# for i in span:
#     i.replace_with("")
# region = movie_soup.find('div', id='info').find_all(myfun)
# region = movie_soup.find(text="美国")

# print(span)
try:
    interests_list = tv_soup.find('div', class_='subject-others-interests-ft').find_all('a')
    seen = interests_list[1].text[0:-3]
    interests = interests_list[2].text[0:-3]
except:
    print("interests list error!")
    seen = None
    interests = None
# intro = movie_soup.find('span', property='v:summary').text

print(seen, interests)

# b = json.dumps(rank_res)
#
# f2 = open('test.json', 'wt')
# f2.write(b)
# f2.close()