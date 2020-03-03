from django.shortcuts import render
from .models import Coord


def plotView(request):
    coords = Coord.objects.all()
    context = {
        "coords": coords
    }
    return render(request, 'mtsp/index.html', context)