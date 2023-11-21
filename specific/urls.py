from django.urls import path
from specific.views import *

app_name='specific'
urlpatterns=[
    path('afrid/',afrid,name='afrid'),
    path('nagendra/',nagendra,name='nagendra'),
]