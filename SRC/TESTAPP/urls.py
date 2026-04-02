from django.urls import path
from .views import *

urlpatterns=[
    path('',view=home_view,name='home_page_view')
]
