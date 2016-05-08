from django.shortcuts import render
from .models import Service, ServicesImage
from displays.models import DisplayImage
from gallery.models import Portfolio


def home(request):
    slider =  DisplayImage.objects.all()
    services = Service.objects.all()
    images = ServicesImage.objects.all()
    portfolio = Portfolio.objects.all()

    context = {"slider": slider,
               'services': services,
               'images': images,
               'portfolio': portfolio,
               }
    return render(request, 'home.html', context)

def services(request):
    services = Service.objects.all()
    images = ServicesImage.objects.all()
    slider = DisplayImage.objects.all()
    context = {
        'services': services,
        'images': images,
        'slider':slider
    }
    return render(request, 'services.html', context)

def about(request):
    slider = DisplayImage.objects.all()

    return render(request, 'about.html', {"slider":slider})

def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    image = ServicesImage.objects.all()
    context = {
        'service': service,
        'image': image,
    }
    return render(request, 'service_detail.html', context)
