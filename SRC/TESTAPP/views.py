from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def home_view(request):
    return render(request,'homepage.html')


def health_view(request):
    return HttpResponse('SUCCESFUL')