from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , "index.html")

def contact(request):
    return render(request , "contact.html")

def about(request):
    return render(request , "about.html")
def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')

    if removepunc == "on" and fullcaps=="on" and newlineremover=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations and char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()
        params = {'purpose': 'All procedures applied', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extraspaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)