from django.urls import path
from app2.views import *
app_name='pspk'
urlpatterns=[
    path('sushma/',sushma,name='sushma'),
    path('parveen/',parveen,name='parveen'),
]