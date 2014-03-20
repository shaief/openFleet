from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.db.models import (
    # Avg,
    Sum,
)

from effectiveCar.models import (
    Car,
    KMRead,
    Accident,
    MonthlyRecord,
    Treatment,
)
import datetime
# import json
# import time
# import itertools


class CarListView(ListView):

    model = Car
    fields = ['nickname', 'license_id', 'current_owner', 'car_model', 'maker']
    template_name = 'effectiveCar/cars/cars_list.html'


class CreateCarView(CreateView):

    model = Car
    fields = ['nickname',
              'license_id',
              'classification',
              'car_model',
              'maker',
              'color',
              'production_year',
              'date_of_purchase',
              'km_read_at_purchase',
              'license_renewal_date',
              'insurance_renewal_date',
              'current_owner',
              'status',
              ]
    template_name = 'effectiveCar/cars/edit_car.html'

    def get_success_url(self):
        return reverse('cars_list')

    def get_context_data(self, **kwargs):
        context = super(CreateCarView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_car')

        return context


class UpdateCarView(UpdateView):

    model = Car
    fields = ['nickname',
              'license_id',
              'classification',
              'car_model',
              'maker',
              'color',
              'production_year',
              'date_of_purchase',
              'km_read_at_purchase',
              'license_renewal_date',
              'insurance_renewal_date',
              'current_owner',
              'status',
              ]
    template_name = 'effectiveCar/cars/edit_car.html'

    def get_success_url(self):
        return reverse('cars_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateCarView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_car',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteCarView(DeleteView):
    model = Car
    success_url = reverse_lazy('cars_list')


class CarView(DetailView):

    model = Car
    template_name = 'effectiveCar/cars/car.html'


def view_car(request, pk):
    today = datetime.datetime.today()
    next_week = datetime.date.today()+datetime.timedelta(days=7)
    next_month = datetime.date.today()+datetime.timedelta(days=31)
    # next license renewals:
    car = Car.objects.get(id=pk)
    if car.license_renewal_date < next_week:
        license_renewal = 1
    elif car.license_renewal_date < next_month:
        license_renewal = 2
    else:
        license_renewal = 3
    # next insurance renewals:
    if car.insurance_renewal_date < next_week:
        insurance_renewal = 1
    elif car.insurance_renewal_date < next_month:
        insurance_renewal = 2
    else:
        insurance_renewal = 3
    try:
        km = KMRead.objects.filter(license_id=car.id).\
            latest('timestamp').value
    except:
        km = "No km Data!"
    accidents_cost = Accident.objects.\
        filter(license_id_id=pk).\
        aggregate(value_sum=Sum('cost'))
    try:
        monthly_record = MonthlyRecord.objects.filter(license_id=car.id).\
            latest('id')
    except:
        monthly_record = "No Data!"
    try:
        treatment = Treatment.objects.filter(license_id=car.id).\
            latest('id')
        if (km - treatment.km_read < 1000):
            km1000 = True
        else:
            km1000 = False
    except:
        treatment = "No Data!"
        km1000 = False
    try:
        next_car = Car.objects.get(pk=pk+1)
    except:
        next_car = None
    try:
        previous_car = Car.objects.get(pk=pk-1)
    except:
        previous_car = None
    context = dict(
        car=car,
        today=today,
        license_renewal=license_renewal,
        insurance_renewal=insurance_renewal,
        km=km,
        km1000=km1000,
        monthly_record=monthly_record,
        treatment=treatment,
        accidents_cost=accidents_cost['value_sum'],
        next_car=next_car,
        previous_car=previous_car,
    )
    return render(request, 'effectiveCar/cars/view_car.html', context)
