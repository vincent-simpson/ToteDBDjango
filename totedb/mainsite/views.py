from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, template_name='mainsite/index.html')



# https://docs.djangoproject.com/en/2.2/intro/tutorial03/