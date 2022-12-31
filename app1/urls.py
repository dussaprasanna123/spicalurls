from django.urls import path
from app1.views import *
app_name='rrr'
urlpatterns=[

    path('vamsi/', vamsi,name='vamsi'),
    path('uma/',uma, name='uma'),
]