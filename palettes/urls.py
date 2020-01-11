""" palettes url configuration """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='palettes-home'),
    path('about/', views.about, name='palettes-about'),
]