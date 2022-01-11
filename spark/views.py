from django.shortcuts import render
from . import randomWords
from django.http import JsonResponse



def index(request):
    ie_wordlist, trend_rensou_wordlist, wiki = randomWords.randomC()

    content = {
        'word_ie1': ie_wordlist[0],
        'word_ie2': ie_wordlist[1],
        'word_ie3': ie_wordlist[2],
        'word_rand1': trend_rensou_wordlist[0],
        'word_rand2': trend_rensou_wordlist[1],
        'word_rand3': trend_rensou_wordlist[2],
        'word_rand4': trend_rensou_wordlist[3],
        'word_rand5': trend_rensou_wordlist[4],
        'word_rand6': trend_rensou_wordlist[5],
        'word_rand7': trend_rensou_wordlist[6],
        'word_rand8': trend_rensou_wordlist[7],
        'word_rand9': trend_rensou_wordlist[8],
        'wiki':wiki

        }
    return render(request, 'spark/index.html', content)


def ajax_wiki(request):
    ie_wordlist, trend_rensou_wordlist, wiki = randomWords.randomC()
    
    content = {
        'word_ie1': ie_wordlist[0],
        'word_ie2': ie_wordlist[1],
        'word_ie3': ie_wordlist[2],
        'word_rand1': trend_rensou_wordlist[0],
        'word_rand2': trend_rensou_wordlist[1],
        'word_rand3': trend_rensou_wordlist[2],
        'word_rand4': trend_rensou_wordlist[3],
        'word_rand5': trend_rensou_wordlist[4],
        'word_rand6': trend_rensou_wordlist[5],
        'word_rand7': trend_rensou_wordlist[6],
        'word_rand8': trend_rensou_wordlist[7],
        'word_rand9': trend_rensou_wordlist[8],
        'wiki': wiki
    
        }
    return JsonResponse(content)
