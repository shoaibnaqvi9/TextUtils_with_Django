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
    fulllows=request.GET.get('fulllows','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        djtext = ''.join(char for char in djtext if char not in punctuations)
    if fullcaps == "on":
        djtext = djtext.upper()
    if fulllows == "on":
        djtext = djtext.lower()
    if newlineremover == "on":
        djtext = djtext.replace("\n", "").replace("\r", "")
    if extraspaceremover == "on":
        djtext = ' '.join(djtext.split())
    params = {'purpose': 'Text Analyzed', 'analyzed_text': djtext}
    return render(request, 'index.html', params)