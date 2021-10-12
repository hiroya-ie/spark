#テキストをランダムで表示する
import random

# def randomA():
#     return random.choice(["リンゴ","ゴリラ","ラッパ","パンツ"])

def randomA():
    return random.choice(trend_words_list)


#pytrendからリスト作成
from pytrends.request import TrendReq
pytrend = TrendReq(hl='ja-jp',tz=540)
trend_words_list = pytrend.trending_searches(pn='japan')[0].to_list()




#連想語サイトからスクレイピングしてリスト作成





