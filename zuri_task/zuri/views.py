from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("<h1 style='display:flex; justify-content:center; align-items:center; height:100vh; font-size:12em;'> Hello Zuri </h1>")
