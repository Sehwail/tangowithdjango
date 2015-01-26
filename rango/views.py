from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
	return HttpResponse("<p>Rango says here is the about page.<br>this tutorial has been put together by Majd Sehwail, 2096507</p> <br/> <a href='/rango'>Index</a>")
