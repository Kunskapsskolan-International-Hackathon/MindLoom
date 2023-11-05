from django.shortcuts import render

def IndexView(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return render(request, "index.html")   

def InformationView(request):
    if request.user.is_authenticated:
        return render(request, "information.html")
    else:
        return render(request, "index.html")   

def PuzzlesView(request):
    if request.user.is_authenticated:
        return render(request, "puzzles.html")
    else:
        return render(request, "index.html")   
    
def SimonMemorizeView(request):
    if request.user.is_authenticated:
        return render(request, "puzzles/simon.html")
    else:
        return render(request, "index.html")   

def PuzzleKidsView(request):
    if request.user.is_authenticated:
        return render(request, "puzzles/puzzlekids.html")
    else:
        return render(request, "index.html")   

def ColoringView(request):
    if request.user.is_authenticated:
        return render(request, "puzzles/coloringview.html")
    else:
        return render(request, "index.html")   


def PaintOnlineView(request):
    if request.user.is_authenticated:
        return render(request, "puzzles/paintonline.html")
    else:
        return render(request, "index.html")   