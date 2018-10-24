from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('calendar/', views.about, name='calendar'),
    path('donations/', views.about, name='donations'),
    path('sponsors/', views.about, name='sponsors'),
    path('timeline/', views.about, name='calendar'),
]
