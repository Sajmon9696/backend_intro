from datetime import datetime

from django.shortcuts import render


# Create your views here.

def isitknewyear(request):
    now = datetime.now()
    if now.month == 1 and now.day == 1:
        result = True
    else:
        result = False
    return render(request, "is_it_knew_year.html", context={'result': result})

def template_view(request):
    fruits = [
        'apple', 'banana', 'orange'
    ]
    return render(request, 'templates.html', context={'fruits': fruits})

