from django.urls import path
from app2.views import *
app_name='something'
urlpatterns =[
    path('giri/',giri,name='giri'),
    path('dq/',dq,name='dq'),
]
