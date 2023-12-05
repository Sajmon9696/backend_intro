from hello.views import hello_view, hello_eva, hello_adam, hello_name, hello_template, hello_template2
from django.urls import path, include

urlpatterns = [
    path('', hello_view),
    path('eva/', hello_eva),
    path('adam/', hello_adam),
    path('<name>/', hello_name),
    path('templates/<name>/', hello_template),
    path('template2/<name>/', hello_template2),

]
