from django.shortcuts import render_to_response, get_object_or_404
from .models import Country, Region
import json

# Create your views here.
def country_display(request):
    context = {}
    context['countries'] = Country.objects.all()
    return render_to_response("country_display.html", context)


def region_trend(request):
    context = {}
    context['numbers'] = Region.objects.all()
    dataset = []
    for item in context['numbers']:
        obj = {}
        obj["region"] = item.state_name
        obj["number"] = item.migrant_num
        obj["year"] = item.year
        obj["country"] = item.country_name
        dataset.append(obj)
    #context['state'] = get_object_or_404(State, pk=state_pk)
    return render_to_response("region_trend.html", {
        'dataset': json.dumps(dataset)
    })