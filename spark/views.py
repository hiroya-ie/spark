from django.shortcuts import render

#from django.http import HttpResponse

from . import randomWords

def index(request):
    content = {
        'w1': randomWords.randomA(),
        'w2': randomWords.randomA(),
        'w3': randomWords.randomA()
        }
    return render(request, 'spark/index.html', content)