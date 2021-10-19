from django.shortcuts import render

#from django.http import HttpResponse

from . import randomWords

def index(request):
    ie_wordlist, trend_rensou_wordlist = randomWords.randomA()
    result = []
    #２つのワードを合体してresultリストに追加する
    for ie_word, trend_rensou_word in zip(ie_wordlist, trend_rensou_wordlist):
        result.append(ie_word +" × "+ trend_rensou_word)

    content = {
        'values': result
        }
    return render(request, 'spark/index.html', content)