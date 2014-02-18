from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from effectiveCar.models import Classification


class GroupsListView(ListView):

    model = Classification
    fields = ['group']
    template_name = 'effectiveCar/classification/groups_list.html'


class CreateGroupView(CreateView):

    model = Classification
    fields = ['group']
    template_name = 'effectiveCar/classification/edit_group.html'

    def get_success_url(self):
        return reverse('groups_list')

    def get_context_data(self, **kwargs):
        context = super(CreateGroupView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_group')

        return context


class UpdateGroupView(UpdateView):

    mmodel = Classification
    fields = ['group']
    template_name = 'effectiveCar/classification/edit_group.html'

    def get_success_url(self):
        return reverse('groups_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateGroupView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_group',
                                    kwargs={'pk': self.get_object().id})
        return context


class GroupView(DetailView):

    model = Classification
    template_name = 'effectiveCar/classification/group.html'
