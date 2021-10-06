#テキストをランダムで表示する

import random

# def randomA():
#     return random.choice(["リンゴ","ゴリラ","ラッパ","パンツ"])



conn = sqlite3.connect("wnjpn.db")
def randomA():

    return random.choice(word_list)



#日本語ワードネットのデータベースからリスト作成
import sys, sqlite3
from collections import namedtuple
from pprint import pprint
conn = sqlite3.connect("./spark/wnjpn.dbのコピー")
cur = conn.execute("select * from word where lang = 'jpn' ORDER BY RANDOM() LIMIT 1000;")
wordlist = [ record[2] for record in cur.fetchall()]



#pytrendからリスト作成
from pytrends.request import TrendReq
pytrend = TrendReq(hl='ja-jp',tz=540)
trend_words_list = pytrend.trending_searches(pn='japan')[0].to_list()





#連想語サイトからスクレイピングしてリスト作成
from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://renso-ruigo.com")
data = html.read()
html = data.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all("a")
word_list=[]

for a in links:
    text = a.text
    word_list.append(text)

del word_list[:4]
del word_list[-55:]








