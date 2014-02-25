from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import Car


class CarListView(ListView):

    model = Car
    fields = ['license_id', 'current_owner', 'car_model', 'maker']
    template_name = 'effectiveCar/cars/cars_list.html'


class CreateCarView(CreateView):

    model = Car
    fields = ['license_id',
              'classification',
              'car_model',
              'maker',
              'production_year',
              'date_of_purchase',
              'license_renewal_date',
              'insurance_renewal_date',
              'current_owner',
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
    fields = ['license_id',
              'classification',
              'car_model',
              'maker',
              'production_year',
              'date_of_purchase',
              'license_renewal_date',
              'insurance_renewal_date',
              'current_owner',
              ]
    template_name = 'effectiveCar/cars/edit_car.html'

    def get_success_url(self):
        return reverse('cars_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateCarView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_car',
                            kwargs={'pk': self.get_object().id})
        return context


class CarView(DetailView):

    model = Car
    template_name = 'effectiveCar/cars/car.html'
