from hello.views import hello_view
from django.urls import path, include

urlpatterns = [
    path('', hello_view)
]
