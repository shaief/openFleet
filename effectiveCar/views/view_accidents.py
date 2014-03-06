from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import Accident


class AccidentsListView(ListView):

    model = Accident
    fields = ['license_id', 'driver', 'date', 'cost',
              'description', 'image']
    template_name = 'effectiveCar/accidents/accidents_list.html'


class CreateAccidentView(CreateView):

    model = Accident
    fields = ['license_id', 'driver', 'date', 'cost',
              'description', 'image']
    template_name = 'effectiveCar/accidents/edit_accident.html'

    def get_success_url(self):
        return reverse('accidents_list')

    def get_context_data(self, **kwargs):
        context = super(CreateAccidentView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_accident')

        return context


class UpdateAccidentView(UpdateView):

    model = Accident
    fields = ['license_id', 'driver', 'date', 'cost',
              'description', 'image']
    template_name = 'effectiveCar/accidents/edit_accident.html'

    def get_success_url(self):
        return reverse('accidents_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateAccidentView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_accident',
                                    kwargs={'pk': self.get_object().id})
        return context


class AccidentView(DetailView):

    model = Accident
    template_name = 'effectiveCar/accidents/accident.html'
