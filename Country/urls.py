from django.urls import path
from . import views

urlpatterns = [
    path('', views.country_display, name='country display'),
    path('<int:country_pk>', views.country_detail, name='country detail'),
]
#http://localhost:8000/country/