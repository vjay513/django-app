from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me':'Hello I am from the view.py'}
    return render(request, 'index.html', context=my_dict)
    ##
    # return HttpResponse("Hello, world. You're at the polls index.")