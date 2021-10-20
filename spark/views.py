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
        'word_ie': ie_wordlist,
        'word_rand': trend_rensou_wordlist
        }
    return render(request, 'spark/index.html', content)