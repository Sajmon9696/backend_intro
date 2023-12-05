from django.contrib import admin
from django.urls import path, include
from links_app.views import first_view, second_view, third_view

app_name = "links_app"
urlpatterns = [
    path('first/', first_view, name='first_name'),
    path('second/', second_view,  name='second_name'),
    path('third/', third_view,  name='third_name'),
]