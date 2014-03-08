from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from effectiveCar.models import Car, Owner, Classification
import datetime
import json
import time
import itertools

from django.db.models import Avg

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
    treament_in_less_than_1e3 = Car.objects.all().\
        filter(insurance_renewal_date__lte=next_year).\
        order_by('license_renewal_date')    

    context = dict(
        today=today,
        license_next_week=license_next_week,
        license_next_month=license_next_month,
        license_next_year=license_next_year,
        insurance_next_week=insurance_next_week,
        insurance_next_month=insurance_next_month,
        insurance_next_year=insurance_next_year,
    )
    return render(request, 'effectiveCar/index.html', context)
