from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hlo(request):
    return HttpResponse("<h1><marquee>This is my first <b>DJANGO</b> code</marquee></h1>")
def blo(request):
    return HttpResponse("<marquee><h1>Soumya Nayak Mandu <b>Annabela</b></h1></maquee>")