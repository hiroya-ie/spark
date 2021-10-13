from django.shortcuts import render
from . import randomWords


def index(request):
    wordlist=randomWords.randomA()
    
    content = {
        'values': wordlist
        }
    return render(request, 'spark/index.html', content)