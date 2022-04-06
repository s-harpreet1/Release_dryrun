from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def entry(request):
    return HttpResponse("Ok Go ahead")
