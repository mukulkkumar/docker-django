from django.urls import path, include
from music_app import views

urlpatterns = [
    path('music/', views.home),
]
