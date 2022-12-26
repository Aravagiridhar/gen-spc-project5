from django.urls import path
from app1.views import *
app_name='something'
urlpatterns =[
    path('hii/',hii,name='hii'),
    path('hello/',hello,name='hello'),
]
