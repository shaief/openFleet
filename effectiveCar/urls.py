from django.conf.urls import patterns, include, url
from effectiveCar import views


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'effectiveCar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ########################################

    # Cars:
    url(r'^cars_list/$',
        views.CarListView.as_view(),
        name='cars_list'),
    url(r'^add_car/$',
        views.CreateCarView.as_view(),
        name='add_car'),
    url(r'^edit_car/(?P<pk>\d+)/$',
        views.UpdateCarView.as_view(),
        name='edit_car'),
    url(r'^car/(?P<pk>\d+)/$',
        views.CarView.as_view(),
        name='view_car'),

    # Owners:
    url(r'^owners_list/$',
        views.OwnerListView.as_view(),
        name='owners_list'),
    url(r'^add_owner/$',
        views.CreateOwnerView.as_view(),
        name='add_owner'),
    url(r'^edit_owner/(?P<pk>\d+)/$',
        views.UpdateOwnerView.as_view(),
        name='edit_owner'),
    url(r'^owner/(?P<pk>\d+)/$',
        views.OwnerView.as_view(),
        name='view_owner'),

    # Monthly Records:
    url(r'^records_list/$',
        views.MonthlyListView.as_view(),
        name='records_list'),
    url(r'^add_record/$',
        views.CreateMonthlyView.as_view(),
        name='add_record'),
    url(r'^edit_record/(?P<pk>\d+)/$',
        views.UpdateMonthlyView.as_view(),
        name='edit_record'),
    url(r'^record/(?P<pk>\d+)/$',
        views.MonthlyView.as_view(),
        name='view_record'),

    # Classifications:
    url(r'^groups_list/$',
        views.GroupsListView.as_view(),
        name='groups_list'),
    url(r'^add_group/$',
        views.CreateGroupView.as_view(),
        name='add_group'),
    url(r'^edit_group/(?P<pk>\d+)/$',
        views.UpdateGroupView.as_view(),
        name='edit_group'),
    url(r'^group/(?P<pk>\d+)/$',
        views.GroupView.as_view(),
        name='view_group'),
)
