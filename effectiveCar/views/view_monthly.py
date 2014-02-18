from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import MonthlyRecord


class MonthlyListView(ListView):
    """docstring for TemplateView"models.
    def __init__(self, arg):
        super(TemplateView,models.).__init__()
        self.arg = arg
    """
    model = MonthlyRecord
    fields = ['license_id', 'year', 'month', 'fuel_consumed']
    template_name = 'effectiveCar/monthly/records_list.html'


class CreateMonthlyView(CreateView):

    model = MonthlyRecord
    fields = ['license_id', 'year', 'month', 'fuel_consumed']
    template_name = 'effectiveCar/monthly/edit_monthly.html'

    def get_success_url(self):
        return reverse('records_list')

    def get_context_data(self, **kwargs):
        context = super(CreateMonthlyView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_record')

        return context


class UpdateMonthlyView(UpdateView):

    mmodel = MonthlyRecord
    fields = ['license_id', 'year', 'month', 'fuel_consumed']
    template_name = 'effectiveCar/monthly/edit_monthly.html'

    def get_success_url(self):
        return reverse('records_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateMonthlyView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_record',
                                    kwargs={'pk': self.get_object().id})
        return context


class MonthlyView(DetailView):

    model = MonthlyRecord
    template_name = 'effectiveCar/monthly/monthly.html'
