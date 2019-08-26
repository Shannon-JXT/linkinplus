from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_display, name='country_display'),
]
#http://localhost:8000/country/