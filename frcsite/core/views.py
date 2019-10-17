from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def about(request):
    return render(request, 'core/about.html')
def calendar(request):
    return render(request, 'core/calendar.html')
def donations(request):
    return render(request, 'core/donations.html')
def sponsors(request):
    return render(request, 'core/sponsors.html')
def timeline(request):
    return render(request, 'core/timeline.html')
def media(request):
    return render(request, 'core/media.html')
def contact(request):
    return render(request, 'core/contact.html')
def chhs(request):
    return render(request, 'core/chhs.html')
