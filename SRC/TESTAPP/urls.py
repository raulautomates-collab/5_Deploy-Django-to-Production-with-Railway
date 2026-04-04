from django.urls import path
from .views import *

urlpatterns=[
    path('',view=home_view,name='home_page_view'),
    path('success',view=health_view,name='health_check_view'),
    path('fun/',view=funview,name='funview'),
]
