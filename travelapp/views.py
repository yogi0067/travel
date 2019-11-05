from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def home(request):
    destobj = Destination.objects.all()
    return render(request,'index.html', {'dest1': destobj})
