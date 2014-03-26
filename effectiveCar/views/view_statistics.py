import datetime
import json
import calendar
import random
from django.db.models import Q
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
    owners_list = Owner.objects.all().order_by('last_name')
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
    owners_list = Owner.objects.all().order_by('last_name')
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


def StatisticsClassification(request, pk):
    name = Classification.objects.get(id=pk).group
    cars_list = Car.objects.all().filter(classification=pk).\
        order_by('id')
    today = datetime.date.today()
    first = datetime.date(day=1, month=today.month, year=today.year)
    previous_month = (first - datetime.timedelta(days=1))
    last_month = previous_month.month
    this_year = previous_month.year
    context = dict(
        pk=pk,
        name=name,
        this_year=this_year,
        last_month=last_month,
        cars_list=cars_list,
    )
    return render(request, 'effectiveCar/statistics/classification.html',
                  context)


def StatisticsClassificationMonth_json(request, pk, year, month):
    context = []
    cars_list = Car.objects.all().filter(classification=pk).\
        order_by('id')
    year = int(year)
    month = int(month)
    cars = []
    url = []
    nis_per_km = []
    km_per_month = []
    cost_per_month = []
    liter_per_month = []
    # calendar.monthrange(year, month)[1] gives us the last day of the month
    ''' since kmread is reported randomly, this way we'll have as much
    information as possible. '''
    start_date = datetime.date(year, month-1,
                               calendar.monthrange(year, month-1)[1])
    end_date = datetime.date(year, month,
                             calendar.monthrange(year, month)[1])
    for c in cars_list:
        cars.append(c.license_id)
        try:
            cost = MonthlyRecord.objects.all().\
                filter(license_id=c.id).\
                filter(month=month).cost
        except:
            cost = 1000 * random.random()
        try:
            liter = MonthlyRecord.objects.all().\
                filter(license_id=c.id).\
                filter(month=month).fuel_consumed
        except:
            liter = 100.01 * random.random()
        try:
            km_values = KMRead.objects.filter(license_id=c.id).\
                filter(Q(reported_at__gte=start_date)
                       & Q(reported_at__lte=end_date)).\
                order_by('reported_at')
            km = km_values.latest('id').value-km_values[0].value
        except:
            km = 1000 * random.random()
        try:
            nis_per = cost / km
            nis_per = round(nis_per, 2)
        except:
            nis_per = 10000 * random.random()
            nis_per = round(nis_per, 2)
        liter = round(liter, 2)
        km = round(km, 2)
        cost = round(cost, 2)
        km_per_month.append(km)
        cost_per_month.append(cost)
        liter_per_month.append(liter)
        nis_per_km.append(nis_per)
        url = reverse('view_car', kwargs={'pk': c.id})
        dataset = dict(
            carID=c.id,
            url=url,
            car=c.license_id,
            km_per_month=km,
            cost_per_month=cost,
            liter_per_month=liter,
            nis_per_km=nis_per
        )
        context.append(dataset)
    # context = dict(
    #     cars=cars,
    #     cost_per_month=cost_per_month,
    #     liter_per_month=liter_per_month,
    #     km_per_month=km_per_month,
    #     nis_per_km=nis_per_km,
    # )
    # context = dict(
    #     classification=pk,
    #     year=year,
    #     month=month,
    #     dataset=dataset,
    # )
    return HttpResponse(json.dumps(context))
    # return render(request, 'effectiveCar/statistics/general.html', context)



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
