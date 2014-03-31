from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import KMRead

from braces.views import LoginRequiredMixin

class KMReadListView(ListView):

    model = KMRead
    fields = ['kmread']
    template_name = 'effectiveCar/kmread/kmreads_list.html'


class CreateKMReadView(LoginRequiredMixin, CreateView):

    model = KMRead
    fields = ['license_id', 'reported_at', 'report_type', 'value']
    template_name = 'effectiveCar/kmread/edit_kmread.html'

    def get_success_url(self):
        return reverse('kmreads_list')

    def get_context_data(self, **kwargs):
        context = super(CreateKMReadView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_kmread')

        return context


class UpdateKMReadView(LoginRequiredMixin, UpdateView):

    model = KMRead
    fields = ['license_id', 'reported_at', 'report_type', 'value']
    template_name = 'effectiveCar/kmread/edit_kmread.html'

    def get_success_url(self):
        return reverse('kmreads_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateKMReadView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_kmread',
                                    kwargs={'pk': self.get_object().id})
        return context


class KMReadView(DetailView):

    model = KMRead
    template_name = 'effectiveCar/kmread/kmread.html'
