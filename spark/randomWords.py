#テキストをランダムで表示する
import random

# def randomA():
#     return random.choice(["リンゴ","ゴリラ","ラッパ","パンツ"])


def randomA():
    return random.choice(rensou_words_list)





#連想語サイトからスクレイピングしてリスト作成
from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://renso-ruigo.com")
data = html.read()
html = data.decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
links = soup.find_all("a")
rensou_words_list=[]

for a in links:
    text = a.text
    rensou_words_list.append(text)

del rensou_words_list[:4]
del rensou_words_list[-55:]
