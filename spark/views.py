from django.shortcuts import render
from . import randomWords


def index(request):
    wordlist=randomWords.randomA()
    
    content = {
        'w1': wordlist[0],
        'w2': wordlist[1],
        'w3': wordlist[2],
        'values': wordlist
        }
    return render(request, 'spark/index.html', content)