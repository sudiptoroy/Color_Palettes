from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Dummy data
palettes = [
    {
        'author' : 'Sudipto Roy',
        'title' : 'Gray Accent',
        'content' : 'Colors',
        'date_posted' : 'January 11, Saterday'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Red Accent',
        'content' : 'Colors',
        'date_posted' : 'January 11, Saterday'
    } 
]

def home(request):
    """Home page view for palettes app"""

    # Import dummy data
    context = {
        'palettes_content' : palettes
    }
    return render(request, 'palettes/home.html', context)

def about(request):
    """ About page view for palettes app """
    return render(request, 'palettes/about.html', {'title':'about'})