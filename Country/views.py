from django.shortcuts import render_to_response, get_object_or_404
from .models import Country, Region
import json

# Create your views here.
def country_display(request):
    context = {}
    context['countries'] = Country.objects.all()
    return render_to_response("country_display.html", context)

def region_trend(request, country_pk=None):
    if country_pk is None:
        data = Region.objects.all()
    else:
        data = get_object_or_404(Region, pk=country_pk)

    dic = {}
    for item in data:
        temp = { \
            'year':item.year, \
            'num':item.migrant_num, \
            'region':item.region_name \
        }
        if str(item.country_name) in dic:
            dic[str(item.country_name)].append(temp)
        else:
            dic[str(item.country_name)] = [temp]
    return render_to_response("region_trend.html", {'trends': json.dumps(dic)})