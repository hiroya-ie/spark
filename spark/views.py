from django.shortcuts import render
from . import randomWords


def index(request):
    wordlist=randomWords.randomA()
    
    content = {
        'values': wordlist
        }
    return render(request, 'spark/index.html', content)


def index(request):
    ie_wordlist, trend_rensou_wordlist = randomWords.randomA()

    content = {
        'word_ie1': ie_wordlist[0],
        'word_ie2': ie_wordlist[1],
        'word_ie3': ie_wordlist[2],
        'word_ie4': ie_wordlist[3],
        'word_ie5': ie_wordlist[4],
        'word_ie6': ie_wordlist[5],
        'word_ie7': ie_wordlist[6],
        'word_ie8': ie_wordlist[7],
        'word_ie9': ie_wordlist[8],
        'word_rand1': trend_rensou_wordlist[0],
        'word_rand2': trend_rensou_wordlist[1],
        'word_rand3': trend_rensou_wordlist[2],
        'word_rand4': trend_rensou_wordlist[3],
        'word_rand5': trend_rensou_wordlist[4],
        'word_rand6': trend_rensou_wordlist[5],
        'word_rand7': trend_rensou_wordlist[6],
        'word_rand8': trend_rensou_wordlist[7],
        'word_rand9': trend_rensou_wordlist[8],
        'word_rand10': trend_rensou_wordlist[9],
        'word_rand11': trend_rensou_wordlist[10],
        'word_rand12': trend_rensou_wordlist[11],
        'word_rand13': trend_rensou_wordlist[12],
        'word_rand14': trend_rensou_wordlist[13],
        'word_rand15': trend_rensou_wordlist[14],
        'word_rand16': trend_rensou_wordlist[15],
        'word_rand17': trend_rensou_wordlist[16],
        'word_rand18': trend_rensou_wordlist[17],
        'word_rand19': trend_rensou_wordlist[18],
        'word_rand20': trend_rensou_wordlist[19],
        'word_rand21': trend_rensou_wordlist[20],
        'word_rand22': trend_rensou_wordlist[21],
        'word_rand23': trend_rensou_wordlist[22],
        'word_rand24': trend_rensou_wordlist[23],
        'word_rand25': trend_rensou_wordlist[24],
        'word_rand26': trend_rensou_wordlist[25],
        'word_rand27': trend_rensou_wordlist[26]

        }
    return render(request, 'spark/index.html', content)