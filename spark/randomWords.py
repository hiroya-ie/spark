#テキストをランダムで表示する
import random
import sqlite3
#import lxml.html
#from pytrends.request import TrendReq

conn = sqlite3.connect("wnjpn.db")
def randomA():
    return random.choice(["リンゴ","ゴリラ","ラッパ","パンツ"])

#pytrends.trending_searches(pn='japan')

#テスト