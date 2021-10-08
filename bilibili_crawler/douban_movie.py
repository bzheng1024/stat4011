import requests
from bs4 import BeautifulSoup
import re
import time
import csv

fp = open('./data/douban_movie.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("rank", "title", "rate", "casts", "tags", "region", "launched_date", "introduction", "duration",
                 "year", "rating_num", "rating_per", "interests", "seen", "comments", "short_comments"))

headers = {
    'referer': 'https://movie.douban.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

movie_rank_url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=10&page_start=0"
movie_rank_res = requests.get(movie_rank_url, headers=headers).json()
time.sleep(0.5)
movie_rank_list = movie_rank_res["subjects"]
if movie_rank_list:
    for i in range(0, 10):
        info = movie_rank_list[i]
        rate = info["rate"]
        title = info["title"]
        movie_url = info["url"]

        movie_res = requests.get(movie_url, headers=headers, timeout=10)
        time.sleep(1)
        movie_res.encoding = 'utf-8'
        movie_soup = BeautifulSoup(movie_res.text, 'xml')
        year = movie_soup.find('span', class_='year').text[1:5]
        rating_num = movie_soup.find('span', property='v:votes').text
        intro = movie_soup.find('span', property='v:summary').text

        try:
            interests_list = movie_soup.find('div', class_='subject-others-interests-ft').find_all('a')
            seen = interests_list[0].text[0:-3]
            interests = interests_list[1].text[0:-3]
        except:
            print(title + " interests list error!")
            seen = None
            interests = None

        comments = movie_soup.find_all('span', class_='pl')[-2].find('a').text[3:-2]
        short_comments = movie_soup.find_all('span', class_='pl')[-4].find('a').text[3:-2]

        tags_list = movie_soup.find_all('span', property='v:genre')
        tags = []
        for tag in tags_list:
            tags.append(tag.text)

        rating_per_list = movie_soup.find_all('span', class_='rating_per')
        rating_per = []
        for rating in rating_per_list:
            rating_per.append(rating.text)

        movie_info = movie_soup.find('div', id='info')
        region_re = re.search(r'.*\u5236\u7247\u56fd\u5bb6\u002f\u5730\u533a.{2}(.*)\n.*', movie_info.text)
        if region_re:
            region = region_re.group(1)
        else:
            region = None

        launched_date_re = re.search(r'.*\u4e0a\u6620\u65e5\u671f.{2}(.*)\n?.*', movie_info.text)
        if launched_date_re:
            launched_date = launched_date_re.group(1)
        else:
            launched_date = None

        duration_re = re.search(r'.*\u7247\u957f.{2}(.*)\n?.*', movie_info.text)
        if duration_re:
            duration = duration_re.group(1)
        else:
            duration = None

        cast_list = movie_soup.find_all('li', class_='celebrity')
        casts = {}
        for cast in cast_list[0:4]:
            name = cast.find('a')['title']
            cast_url = cast.find('a')['href']
            cast_res = requests.get(cast_url, headers=headers, timeout=10)
            time.sleep(1)
            cast_res.encoding = 'utf-8'
            cast_soup = BeautifulSoup(cast_res.text, 'xml')
            cast_bd = cast_soup.find_all('div', class_='bd')[1].text
            cast_intro = re.search(r'.*\u3000\u3000(.*)\n.*', cast_bd).group(1)
            casts[name] = cast_intro

        writer.writerow((i+1, title, rate, casts, tags, region, launched_date, intro, duration,
                 year, rating_num, rating_per, interests, seen, comments, short_comments))
        print(title + " success!")

fp.close()

