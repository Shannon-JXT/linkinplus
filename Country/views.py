from django.shortcuts import render_to_response, get_object_or_404
from .models import Country

# Create your views here.
def country_display(request):
    context = {}
    context['countries'] = Country.objects.all()
    return render_to_response('country/country_display.html', context)

def country_detail(request, country_pk):
    context = {}
    context['country'] = get_object_or_404(Country, pk=country_pk)
    return render_to_response('country/country_detail.html', context)