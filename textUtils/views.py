# I have created this file - Rashmi

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    removeExtraSpace = request.GET.get('removeExtraSpace','off')
    charcount = request.GET.get('charcount', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if capitalize=='on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if removeExtraSpace=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
            params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
            djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if charcount == 'on':
        count = 0
        for i in djtext:
            count += 1
        params = {'purpose': 'Number of Characters',   'analyzed_text': count}

    if (removepunc != "on" and capitalize != "on" and removeExtraSpace != "on" and charcount != "on" and newlineremover != "on"):
        return HttpResponse("Please select any operation and try again")
    return render(request, 'analyze2.html', params)