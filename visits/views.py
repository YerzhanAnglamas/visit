from django.shortcuts import render
from .models import Visit


def index(request):
    list_visits = Visit.objects.all()
    return render(request, 'visits/show_visits.html', context={'list_visits': list_visits})

