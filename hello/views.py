from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_view(request):
    return HttpResponse("Hello world")

def hello_eva(request):
    return HttpResponse("Hello, eva!")


def hello_adam(request):
    return HttpResponse("Hello, adam!")

def hello_name(request, name):
    return HttpResponse(f"Hello, {name}!")

def hello_template(request, name):
    return HttpResponse(f"<h1>Hello, {name}!</h1>")



def hello_template2(request, name):
    return render(request, 'name_template.html', context={'name':name})



