from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from effectiveCar.models import Car, Owner, Classification
import datetime
import json
import time
import itertools

from django.db.models import Avg
from django.db.models import Q

# Create your views here.

# def home(request):
    # return render(request, 'effectiveCar/index.html')


def home(request):
    today = datetime.datetime.now()
    next_week = datetime.datetime.now()+datetime.timedelta(days=7)
    next_month = datetime.datetime.now()+datetime.timedelta(days=31)
    next_year = datetime.datetime.now()+datetime.timedelta(days=365)
    # next license renewals:
    license_next_week = Car.objects.all().\
        filter(license_renewal_date__lte=next_week).\
        order_by('license_renewal_date')
    license_next_month = Car.objects.all().\
        filter(license_renewal_date__lte=next_month).\
        filter(license_renewal_date__gte=next_week).\
        order_by('license_renewal_date')
    license_next_year = Car.objects.all().\
        filter(license_renewal_date__lte=next_year).\
        filter(license_renewal_date__gte=next_month).\
        order_by('license_renewal_date')
    # next insurance renewals:
    insurance_next_week = Car.objects.all().\
        filter(insurance_renewal_date__lte=next_week).\
        order_by('license_renewal_date')
    insurance_next_month = Car.objects.all().\
        filter(insurance_renewal_date__lte=next_month).\
        filter(insurance_renewal_date__gte=next_week).\
        order_by('license_renewal_date')
    insurance_next_year = Car.objects.all().\
        filter(insurance_renewal_date__lte=next_year).\
        filter(insurance_renewal_date__gte=next_month).\
        order_by('license_renewal_date')
    # next routine treatment:
    # cars = Car.objects.all()
    # next_treatment_1e3 = []
    # next_treatment_more = []
    # next_treatment_nodata = []
    # for c in cars:
    #     c_km = c.kmread_set.order_by('-timestamp')
    #     try:
    #         c_km[1]
    #         if c_km[0]-c_km[1] > 9000:
    #             next_treatment_1e3.append(c.license_id)
    #         else:
    #             next_treatment_more.append(c.license_id)
    #     except:
    #         next_treatment_nodata.append(c.license_id)
    context = dict(
        today=today,
        license_next_week=license_next_week,
        license_next_month=license_next_month,
        license_next_year=license_next_year,
        insurance_next_week=insurance_next_week,
        insurance_next_month=insurance_next_month,
        insurance_next_year=insurance_next_year,
        # next_treatment=next_treatment_1e3,
        # next_treatment_car=next_treatment_more,
        # next_treatment_nodata=next_treatment_nodata,
    )
    return render(request, 'effectiveCar/index.html', context)


def search_car(request):
    query = request.GET.get('q', '')
    if(len(query) > 0):
        print "searching for {}".format(query)
        results = Car.objects.filter(license_id__contains=query)
        result_list = []
        for item in results:
            result_list.append(item.license_id)
    else:
        result_list = []

    response_text = json.dumps(result_list, separators=(',', ':'))
    return HttpResponse(response_text, content_type="application/json")


def license_ids(request):
    results = Car.objects.all().order_by('license_id')
    result_list = []
    for item in results:
        result_list.append(item.license_id)
    response_text = json.dumps(result_list, separators=(',', ':'))
    return HttpResponse(response_text, content_type="application/json")
