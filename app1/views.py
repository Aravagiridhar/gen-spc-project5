from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hii(request):
    return HttpResponse('THIS IS APP1 FIRST VIEW')
def hello(request):
    return HttpResponse('THIS APP1 SECOND VIEW')
