from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import Owner

from braces.views import LoginRequiredMixin

class OwnerListView(ListView):

    model = Owner
    fields = ['license_id', 'current_owner']
    template_name = 'effectiveCar/owners/owners_list.html'


class CreateOwnerView(LoginRequiredMixin, CreateView):

    model = Owner
    fields = ['first_name', 'last_name', 'email', 'license_category',
              'license_renewal_date', 'department', 'manager_name', 'image']
    template_name = 'effectiveCar/owners/edit_owner.html'

    def get_success_url(self):
        return reverse('owners_list')

    def get_context_data(self, **kwargs):
        context = super(CreateOwnerView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_owner')

        return context


class UpdateOwnerView(LoginRequiredMixin, UpdateView):

    model = Owner
    fields = ['first_name', 'last_name', 'email', 'license_category',
              'license_renewal_date', 'department', 'manager_name', 'image']
    template_name = 'effectiveCar/owners/edit_owner.html'

    def get_success_url(self):
        return reverse('owners_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateOwnerView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_owner',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteOwnerView(LoginRequiredMixin, DeleteView):
    model = Owner
    success_url = reverse_lazy('owners_list')


class OwnerView(DetailView):

    model = Owner
    template_name = 'effectiveCar/owners/owner.html'
