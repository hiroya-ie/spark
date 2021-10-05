#テキストをランダムで表示する
import random
import lxml.html
from pytrends.request import TrendReq

def randomA():
    return random.choice(["リンゴ","ゴリラ","ラッパ","パンツ"])

#pytrends.trending_searches(pn='japan')