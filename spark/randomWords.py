#テキストをランダムで表示する
import random

from pytrends.request import TrendReq

from bs4 import BeautifulSoup
from urllib.request import urlopen

#l = ["リンゴ","ゴリラ","ラッパ","パンツ"]


def randomA():
    result = []
    trend_wl = pytrend()
    rensou_wl = rensou()
    result.extend(trend_wl)
    result.extend(rensou_wl)
    return random.sample(result, 8)


#pytrendからリスト作成
def pytrend():
    pytrend = TrendReq(hl='ja-jp',tz=540)
    trend_words_list = pytrend.trending_searches(pn='japan')[0].to_list()

    return trend_words_list


#連想語サイトからスクレイピングしてリスト作成
def rensou():
    wlist=[]
    for i in range(5):
        html = urlopen("https://renso-ruigo.com")
        data = html.read()
        html = data.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all("a")
        rensou_words_list=[a.text for a in links]
        del rensou_words_list[:4]
        del rensou_words_list[-55:]
        wlist.extend(rensou_words_list)

    return wlist