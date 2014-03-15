from django.core.urlresolvers import reverse, reverse_lazy
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
