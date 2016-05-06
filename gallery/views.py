from django.shortcuts import render
from .models import Portfolio


def gallery(request):
    portfolio = Portfolio.objects.all()
    return render(request, 'gallery.html', {'portfolio': portfolio})
