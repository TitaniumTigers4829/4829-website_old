from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('calendar/', views.calendar, name='calendar'),
    path('donations/', views.donations, name='donations'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('timeline/', views.timeline, name='timeline'),
    path('media/', views.media, name='media'),
    path('contact/', views.contact, name='contact'),
    path('chhs/', views.chhs, name='chhs'),
]
