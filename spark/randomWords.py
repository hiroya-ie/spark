#テキストをランダムで表示する
import random

# def randomA():
#     return random.choice(["リンゴ","ゴリラ","ラッパ","パンツ"])


def randomA():
    return random.choice(nwn_words_list)



#日本語ワードネットのデータベースからリスト作成
import sys, sqlite3
from collections import namedtuple
from pprint import pprint
conn = sqlite3.connect("./wnjpn.db")
cur = conn.execute("select * from word where lang = 'jpn' ORDER BY RANDOM() LIMIT 1000;")
nwn_words_list = [ record[2] for record in cur.fetchall()]



