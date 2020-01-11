from django.shortcuts import render
from django.http import HttpResponse
from . models import Palettes

# Create your views here.

# Dummy data


def home(request):
    """Home page view for palettes app"""

    # Import dummy data
    context = {
        'palettes_content' : Palettes.objects.all()
    }
    return render(request, 'palettes/home.html', context)

def about(request):
    """ About page view for palettes app """
    return render(request, 'palettes/about.html', {'title':'about'})