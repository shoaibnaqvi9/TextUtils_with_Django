from django.shortcuts import render,redirect
def index(request):
    djtext = request.GET.get('text', '')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    firstcaps=request.GET.get('firstcaps','off')
    fulllows=request.GET.get('fulllows','off')
    newlineremover=request.GET.get('newlineremover','off')
    extraspaceremover=request.GET.get('extraspaceremover','off')
    deletetext=request.GET.get('deletetext','off')
    boldtext=request.GET.get('boldtext','off')
    italictext=request.GET.get('italictext','off')
    underlinetext=request.GET.get('underlinetext','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        djtext = ''.join(char for char in djtext if char not in punctuations)
    if fullcaps == "on":
        djtext = djtext.upper()
    if firstcaps == "on":
        djtext = djtext.title()
    if fulllows == "on":
        djtext = djtext.lower()
    if newlineremover == "on":
        djtext = djtext.replace("\n", "").replace("\r", "")
    if extraspaceremover == "on":
        djtext = ' '.join(djtext.split())
    if deletetext == "on":
        djtext = ""
    if boldtext == "on":
        djtext = "<b>" + djtext + "</b>"
    if italictext == "on":
        djtext = "<i>" + djtext + "</i>"
    if underlinetext == "on":
        djtext = "<u>" + djtext + "</u>"
    params = {'analyzed_text': djtext}
    return render(request , "index.html" , params)

def contact(request):
    return render(request , "contact.html")

def about(request):
    return render(request , "about.html")
