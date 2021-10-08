import requests
from bs4 import BeautifulSoup
import time
import csv

fp = open('./data/douban_group.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("排名", "小组名称", "小组成员数", "刷新时间", "周总讨论", "人均讨论", "刷新增长"))

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

url = "http://123.56.30.233:8080/wp-data/"
res = requests.get(url, headers=headers, timeout=10)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'xml')
table = soup.find_all('tr')
if table:
    for row in table:
        data = row.find_all('td')
        if data:
            writer.writerow((data[0].text, data[1].text, data[2].text, data[3].text, data[4].text, data[5].text, data[6].text))
            print(data[1].text, "success!")
fp.close()

