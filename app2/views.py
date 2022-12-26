from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def giri(request):
    return HttpResponse('THIS IS GIRIDHAR VIEW')
def dq(request):
    return HttpResponse('THIS IS DQ VIEW')