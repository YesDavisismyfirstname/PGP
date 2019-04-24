from django.shortcuts import render

def gamewindow(request):
    return render(request, 'game_window/render.html')
