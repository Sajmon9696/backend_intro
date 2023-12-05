from django.shortcuts import render

# Create your views here.

def first_view(request):
    return render(request, 'links_app/first.html')

def second_view(request):
    return render(request, 'links_app/second.html')

def third_view(request):
    return render(request, 'links_app/third.html')

