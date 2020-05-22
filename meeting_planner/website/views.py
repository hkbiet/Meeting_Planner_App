from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def base(request):
    return HttpResponse("THIS IS BASE PAGE")

def welcome(request):
    return HttpResponse("THIS IS THE WELCOME PAGE")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))
