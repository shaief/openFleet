import datetime
import json
import random
import time
import itertools

from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from django.db.models import Avg

from django.core.urlresolvers import reverse
from django.core import serializers

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import (
    Car,
    Owner,
    Classification,
    MonthlyRecord,
    KMRead,
)

def StatisticsGeneral(request):
    cars_list = Car.objects.all().order_by('license_id')
    owners_list = Owner.objects.all().order_by('name')
    classifications_list = Classification.objects.all().order_by('group')
    months_list = MonthlyRecord.objects.all().order_by('month').distinct()

    context = dict(
        cars_list=cars_list,
        owners_list=owners_list,
        classifications_list=classifications_list,
        months_list=months_list,

    )

    return render(request, 'effectiveCar/statistics/general.html', context)


def StatisticsGeneral_json(request):
    cars_list = Car.objects.all().order_by('license_id')
    owners_list = Owner.objects.all().order_by('name')
    classifications_list = Classification.objects.all().order_by('group')
    months_list = MonthlyRecord.objects.all().order_by('month').distinct()

    car_data = []
    for car in cars_list:
        car_data = serializers.serialize('json', car.monthlyrecord_set.all())
#        mr = list(car.monthlyrecord_set.all())
#        car_data.append(
#            dict(
#                license_id=mr.license_id,
#                year=mr.year,
#                moth=mr.month,
#                fuel=mr.fuel_consumed,
#                cost=mr.cost,
#                km=mr.km,
#                km2liter=(mr.km/mr.fuel_consumed),
#                km2nis=(mr.km/mr.cost),
#            )
#        )
    return HttpResponse(json.dumps(car_data))

# def stationmapparam(request, url_id, abbr):
#     s = get_object_or_404(Station, url_id=url_id)
#     zone_list = Zone.objects.all().order_by('name')
#     station_list = Station.objects.all().order_by('name')
#     lastupdate = s.record_set.latest('id').timestamp
#     abbr_id = Parameter.objects.get(abbr=abbr).id
#     total_average_value = Record.objects.\
#         filter(parameter=abbr_id).aggregate(Avg('value'))
#     station_params = Parameter.objects.\
#         filter(record__station__url_id=url_id).distinct()
#     context = dict(
#         station=s,
#         abbr=abbr,
#         station_list=station_list,
#         station_params=station_params,
#         lastupdate=lastupdate,
#         zone_list=zone_list,
#         total_average_value=total_average_value['value__avg']
#     )
#     return render(request, 'records/stationmapparam.html', context)

def stationmap_param_json(request, url_id, abbr):
    s = get_object_or_404(Station, url_id=url_id)
    records = []
    point = [s.lon, s.lat]
    number_of_values = 0
    sum_values = 0
    for r in s.record_set.all().filter(parameter__abbr=abbr).order_by('-timestamp')[:24]:
        if (r.parameter.abbr == abbr):
            number_of_values += 1
            sum_values += r.value
            records.append(
                dict(
                    value=r.value,
                    timestamp=r.timestamp.isoformat(),
                    day=r.timestamp.day,
                    month=r.timestamp.month,
                    year=r.timestamp.year,
                    hour=r.timestamp.hour,
                    minutes=r.timestamp.minute
                )
            )
    if number_of_values > 0:
        average_value = sum_values / number_of_values
    else:
        average_value = 'No measurements for ' + abbr
    data = dict(
        point=point,
        records=records,
        average_value=average_value
    )
    return HttpResponse(json.dumps(data))


def StatisticsCar(request, url_id, abbr):
    s = get_object_or_404(Station, url_id=url_id)
    zone_list = Zone.objects.all().order_by('name')
    station_list = Station.objects.all().order_by('name')
    lastupdate = s.record_set.latest('id').timestamp
    abbr_id = Parameter.objects.get(abbr=abbr).id
    total_average_value = Record.objects.\
        filter(parameter=abbr_id).aggregate(Avg('value'))
    station_params = Parameter.objects.\
        filter(record__station__url_id=url_id).distinct()
    context = dict(
        station=s,
        abbr=abbr,
        station_list=station_list,
        station_params=station_params,
        lastupdate=lastupdate,
        zone_list=zone_list,
        total_average_value=total_average_value['value__avg']
    )
    return render(request, 'records/stationmapparam.html', context)


# def StatisticsGeneral(request, url_id, abbr):
#     s = get_object_or_404(Station, url_id=url_id)
#     zone_list = Zone.objects.all().order_by('name')
#     station_list = Station.objects.all().order_by('name')
#     lastupdate = s.record_set.latest('id').timestamp
#     abbr_id = Parameter.objects.get(abbr=abbr).id
#     total_average_value = Record.objects.\
#         filter(parameter=abbr_id).aggregate(Avg('value'))
#     station_params = Parameter.objects.\
#         filter(record__station__url_id=url_id).distinct()
#     context = dict(
#         station=s,
#         abbr=abbr,
#         station_list=station_list,
#         station_params=station_params,
#         lastupdate=lastupdate,
#         zone_list=zone_list,
#         total_average_value=total_average_value['value__avg']
#     )
#     return render(request, 'records/stationmapparam.html', context)
