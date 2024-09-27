# views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def removepunc(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #Analyze the text
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("Capatilize first")

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremove(request):
    return HttpResponse("Space Remove")

def charcount(request):
    return HttpResponse("Charactor count")
