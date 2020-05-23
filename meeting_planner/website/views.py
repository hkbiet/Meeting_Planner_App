from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting
# Create your views here.

def base(request):
    return HttpResponse("THIS IS BASE PAGE")

def welcome(request):
    return render(request,'website/welcome.html', {'num_meetings':Meeting.objects.count()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))
