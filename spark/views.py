from django.shortcuts import render

#from django.http import HttpResponse

from . import randomWords

def index(request):
    wordlist=randomWords.randomA()
    content = {
        'w1': wordlist[0],
        'w2': wordlist[1],
        'w3': wordlist[2]
        }
    return render(request, 'spark/index.html', content)