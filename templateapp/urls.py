from django.urls import path, include
from templateapp.views import isitknewyear, template_view


urlpatterns = [
    path('isitknewyear', isitknewyear),
    path('', template_view),
]
