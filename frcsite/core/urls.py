

from django.conf.urls import include, url
from . import views

# Create your views here.

urlpatterns = [
    url(r'^$', views.index, name='home'),

]
