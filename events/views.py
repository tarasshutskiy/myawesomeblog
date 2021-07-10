from .models import Event
from django.shortcuts import render


# Create your views here.


def home(request):
    events = Event.objects
    return render(request, "events/home.html" , {'events':events})