from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[

    path('balaji/',balaji,name='balaji'),
    path('roshni/',roshni,name='roshni'),
]