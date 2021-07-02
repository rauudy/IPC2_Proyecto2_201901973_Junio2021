import xml
from django.shortcuts import render, redirect
import requests as req
import re

# Create your views here.

def index(request):
    return render(request, 'index.html')


