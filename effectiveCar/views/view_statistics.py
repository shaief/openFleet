import datetime
import json
import calendar
import random
from django.db.models import Q
from django.http import HttpResponse

from django.shortcuts import render  # , get_object_or_404

# from django.db.models import Avg

from django.core.urlresolvers import reverse
from django.core import serializers

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
    today = datetime.date.today()
    year = today.year
    context = dict(
        cars_list=cars_list,
        owners_list=owners_list,
        classifications_list=classifications_list,
        months_list=months_list,
        year=year,
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


def StatisticsClassification(request, pk):
    name = Classification.objects.get(id=pk).group
    # months_list = MonthlyRecord.objects.all().
    cars_list = Car.objects.all().filter(classification=pk).\
        order_by('id')
    today = datetime.date.today()
    first_of_this_month = datetime.date(day=1,
                                        month=today.month,
                                        year=today.year)
    previous_month_date = (first_of_this_month - datetime.timedelta(days=1))
    previous_month = previous_month_date.month
    previous_month_year = previous_month_date.year
    context = dict(
        pk=pk,
        name=name,
        previous_month_year=previous_month_year,
        previous_month=previous_month,
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
    start_date = datetime.date(year, month, 1)
    end_date = datetime.date(year, month,
                             calendar.monthrange(year, month)[1])
    end_date = (end_date + datetime.timedelta(days=1))
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
    return HttpResponse(json.dumps(context))


def StatisticsCar(request, pk, year):
    car = Car.objects.get(id=pk)
    months_list = MonthlyRecord.objects.all().filter(license_id=car)
    years_list = MonthlyRecord.objects.all().\
        filter(license_id=car).values('year').distinct()
    cars_list = Car.objects.all().filter(classification=car.classification).\
        order_by('id')
    context = dict(
        pk=pk,
        year=year,
        years_list=years_list,
        car=car,
        months_list=months_list,
        cars_list=cars_list,
    )
    return render(request, 'effectiveCar/statistics/car.html', context)


def StatisticsCar_json(request, pk, year):
    car = Car.objects.get(id=pk)
    months_list = MonthlyRecord.objects.all().\
        filter(license_id=car.id).filter(year=year)
    id = []
    context = []
    months = []
    years = []
    year_month = []
    url = []
    nis_per_km = []
    km_per_month = []
    cost_per_month = []
    liter_per_month = []
    for mo in months_list:
        id = "%04d%02d" % (mo.year, mo.month)
        months.append(mo.month)
        years.append(mo.year)
        year_month.append(str(mo.month) + "/" + str(mo.year))
        # ''' since kmread is reported randomly, this way we'll have as much
        # information as possible. '''
        start_date = datetime.date(mo.year, mo.month, 1)
        # calendar.monthrange(year, month)[1] gives us the last day of the
        # month
        end_date = datetime.date(mo.year, mo.month,
                                 calendar.monthrange(mo.year, mo.month)[1])
        end_date = (end_date + datetime.timedelta(days=1))
        try:
            cost = mo.cost
        except:
            cost = 1000 * random.random()
        try:
            liter = mo.fuel_consumed
        except:
            liter = 100.01 * random.random()
        try:
            km_values = KMRead.objects.filter(license_id=car).\
                filter(Q(reported_at__gte=start_date)
                       & Q(reported_at__lte=end_date)).\
                order_by('reported_at')
            km = km_values.latest('id').value-km_values[0].value
        except:
            km = 1000 * random.random()
        try:
            nis_per = cost / km
        except:
            nis_per = 10000 * random.random()
        liter = round(liter, 2)
        km = round(km, 2)
        cost = round(cost, 2)
        nis_per = round(nis_per, 2)
        km_per_month.append(km)
        cost_per_month.append(cost)
        liter_per_month.append(liter)
        nis_per_km.append(nis_per)
        url = reverse('view_car', kwargs={'pk': car.id})
        dataset = dict(
            id=id,
            year_month=str(mo.month) + "/" + str(mo.year),
            url=url,
            car=car.license_id,
            km_per_month=km,
            cost_per_month=cost,
            liter_per_month=liter,
            nis_per_km=nis_per
        )
        context.append(dataset)
    return HttpResponse(json.dumps(context))
