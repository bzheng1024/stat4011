import requests
from bs4 import BeautifulSoup
import time
import json
import csv
import execjs

fp = open('./data/endata.csv', 'wt', newline='', encoding='utf_8_sig')
writer = csv.writer(fp)
writer.writerow(("排名", "名称", "类型", "播映指数", "用户热度", "媒体热度", "观看度", "好评度"))

header = {
  'Origin': 'https://www.endata.com.cn',
  'Pragma': 'no-cache',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'Accept': 'text/plain, */*; q=0.01',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'no-cache',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Host': 'www.endata.com.cn'
}

post_data = 'tvType=2&MethodName=BoxOffice_GetTvData_PlayIndexRank'

res = requests.post('https://www.endata.com.cn/API/GetData.ashx', headers=header, data=post_data).text
with open('decoder.js', 'r', encoding='utf-8') as f:
    x = execjs.compile(f.read())
meta = x.eval('webInstace.shell("%s")' % res)
data = json.loads(meta)
data_list = data['Data']['Table']
if data_list:
  for info in data_list:
    rank = info['Irank']
    name = info['TvName']
    genres = info['Genres']
    play_index = info['PlayIndex']
    user_hot = info['UserHot']
    media_hot = info['MediaHot']
    play_hot = info['PlayHot']
    answer_hot = info['AnswerHot']
    writer.writerow((rank, name, genres, play_index, user_hot, media_hot, play_hot, answer_hot))
    print(name, "success!")
fp.close()


