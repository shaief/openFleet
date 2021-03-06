from django.shortcuts import render  # , get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import Accident, Car

from django.db.models import Avg, Sum

from braces.views import LoginRequiredMixin

class AccidentsListView(ListView):

    model = Accident
    fields = ['license_id', 'driver', 'date', 'cost',
              'description', 'image']
    template_name = 'effectiveCar/accidents/accidents_list.html'


class CreateAccidentView(LoginRequiredMixin, CreateView):

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


class UpdateAccidentView(LoginRequiredMixin, UpdateView):

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


class DeleteAccidentView(LoginRequiredMixin, DeleteView):
    model = Accident
    success_url = reverse_lazy('accidents_list')


class AccidentView(DetailView):

    model = Accident
    template_name = 'effectiveCar/accidents/accident.html'


def AccidentsView(request, pk):
    accidents_list = Accident.objects.all().filter(license_id_id=pk).\
        order_by('-date')
    license_id = Car.objects.get(id=pk).license_id
    nickname = Car.objects.get(id=pk).nickname
    sum_cost = Accident.objects.\
        filter(license_id_id=pk).\
        aggregate(value_sum=Sum('cost'))
    context = dict(
        pk=pk,
        nickname=nickname,
        license_id=license_id,
        accidents_list=accidents_list,
        sum_cost=sum_cost['value_sum'],
    )
    return render(request, 'effectiveCar/accidents/accidents.html', context)
