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

    year1996 = {'time': 1996}
    year2001 = {'time': 2001}
    year2006 = {'time': 2006}
    year2011 = {'time': 2011}
    year2016 = {'time': 2016}
    for item in data:
        name = change_country_name(str(item.country_name))
        if int(item.year) == 1996:
            year1996[name] = item.migrant_num
        if int(item.year) == 2001:
            year2001[name] = item.migrant_num
        if int(item.year) == 2006:
            year2006[name] = item.migrant_num
        if int(item.year) == 2011:
            year2011[name] = item.migrant_num
        if int(item.year) == 2016:
            year2016[name] = item.migrant_num

    dic = {1996: year1996, 2001: year2001, 2006: year2006, 2011: year2011, 2016: year2016}
    return render_to_response("region_trend.html", {'trends': json.dumps(dic)})

def change_country_name(name):
    if name == 'China':
        return 'cn'
    if name == 'New Zealand':
        return 'nz'
    if name == 'India':
        return 'india'
    if name == 'United Kingdom':
        return 'en'
    if name == 'Vietnam':
        return 'vn'