from django.shortcuts import render

from django.http import HttpResponse

from . models import *

# Create your views here.

def kost(request):
    kost = Kost.objects.all().order_by('-id')
    context = {'kost' : kost}
    return render(request, 'kost.html', context)

def detail(request, id):
    detail = Kost.objects.get(id=id)
    context = {'detail' : detail}
    return render(request, 'detail.html', context)