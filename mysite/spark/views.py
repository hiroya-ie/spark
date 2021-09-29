from django.shortcuts import render

#from django.http import HttpResponse

from . import randomWords

def index(request):
    #out = randomWords.randomA()
    #return HttpResponse(out)
    content = {'message': 'こんにちは！Djangoテンプレート！'}
    return render(request, 'spark/index.html', content)