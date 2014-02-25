from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import Owner


class OwnerListView(ListView):

    model = Owner
    fields = ['license_id', 'current_owner']
    template_name = 'effectiveCar/owners/owners_list.html'


class CreateOwnerView(CreateView):

    model = Owner
    fields = ['name', 'email', 'license_renewal_date']
    template_name = 'effectiveCar/owners/edit_owner.html'

    def get_success_url(self):
        return reverse('owners_list')

    def get_context_data(self, **kwargs):
        context = super(CreateOwnerView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_owner')

        return context


class UpdateOwnerView(UpdateView):

    model = Owner
    fields = ['name', 'email', 'license_renewal_date']
    template_name = 'effectiveCar/owners/edit_owner.html'

    def get_success_url(self):
        return reverse('owners_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateOwnerView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_owner',
                                    kwargs={'pk': self.get_object().id})
        return context


class OwnerView(DetailView):

    model = Owner
    template_name = 'effectiveCar/owners/owner.html'
