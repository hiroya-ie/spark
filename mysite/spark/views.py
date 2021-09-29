from django.shortcuts import render

#from django.http import HttpResponse

from . import randomWords

def index(request):
    content = {'message': randomWords.randomA()}
    return render(request, 'spark/index.html', content)