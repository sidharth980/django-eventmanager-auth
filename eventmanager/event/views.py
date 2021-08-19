from django.shortcuts import render
from .models import Event

def eventPage(request):
    lis = Event.objects.all()
    return render(request,'eventpage.html',{"lis" :lis})