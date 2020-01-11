from django.shortcuts import render
from django.http import HttpResponse
from . models import Palettes
from django.contrib.auth.decorators import login_required

# Create your views here.

# Dummy data


def home(request):
    """Home page view for palettes app"""

    # Import data from database and pass to palettes/home.html
    context = {
        'palettes_content' : Palettes.objects.all()
    }
    return render(request, 'palettes/home.html', context)

def about(request):
    """ About page view for palettes app """
    return render(request, 'palettes/about.html', {'title':'about'})

# Login required because only registered member can create palette
@login_required 
def create_palette(request):
    """ Create palette view """
    return render(request, 'palettes/create_palette.html')