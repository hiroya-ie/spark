from django.shortcuts import render

#from django.http import HttpResponse

from . import randomWords

def index(request):
    ie_wordlist, trend_rensou_wordlist = randomWords.randomA()
    #２つのワードを合体してwordlistリストに追加する
    wordlist = [""+ie_word +" × "+ trend_rensou_word for ie_word, trend_rensou_word in zip(ie_wordlist, trend_rensou_wordlist)]

    content = {
        'values': wordlist
        }
    return render(request, 'spark/index.html', content)