from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def pazzesca(request):
    return HttpResponse("Pazzesca quest'app.")

def luna(request):
    return HttpResponse("Guarda che luna.")