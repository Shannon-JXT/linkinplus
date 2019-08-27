from django.urls import path
from . import views

urlpatterns = [
    path('culture/', views.country_display, name='country_display'),
    path('trend/', views.region_trend, name='region_trend'),
]
#http://localhost:8000/country/