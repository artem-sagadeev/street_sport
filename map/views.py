from django.shortcuts import render
from grounds.models import Ground


def map(request):
    grounds = Ground.objects.all()
    coordinates = [[float(ground.coordinates.split()[0]), float(ground.coordinates.split()[1])]
                   for ground in grounds]
    return render(request, 'map/map.html', {'coordinates': coordinates})