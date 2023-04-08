from django.shortcuts import render

# Create your views here.


def index(request):
    """view to return home app > index page """

    return render(request, 'home/index.html')


def ourstory(request):
    """view to return home app > ourstory """

    return render(request, 'home/ourstory.html')
