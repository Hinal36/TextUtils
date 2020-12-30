# I have created this File
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcounter', 'off')

    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyze_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Convert To UpperCase', 'analyze_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""

        for char in djtext:
            if not(char == "\n" or char == "\r"):
                print(djtext)
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyze_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyze_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Character Counter', 'analyze_text': analyzed}


    return render(request, 'analyze.html', params)
