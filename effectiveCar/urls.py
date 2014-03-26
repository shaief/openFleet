from django.conf.urls import patterns, url
from effectiveCar import views
from django.views.generic import TemplateView

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf import settings

urlpatterns = patterns('',
    url(r'^administration/$',
        TemplateView.as_view(template_name="effectiveCar/administration.html"),
        name='administration'),
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
        name='car'),
    url(r'^view_car/(?P<pk>\d+)/$',
        views.view_car,
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

    # KM Reads:
    url(r'^kmreads_list/$',
        views.KMReadListView.as_view(),
        name='kmreads_list'),
    url(r'^add_kmread/$',
        views.CreateKMReadView.as_view(),
        name='add_kmread'),
    url(r'^edit_kmread/(?P<pk>\d+)/$',
        views.UpdateKMReadView.as_view(),
        name='edit_kmread'),
    url(r'^kmread/(?P<pk>\d+)/$',
        views.KMReadView.as_view(),
        name='view_kmread'),

    # Accidents:
    url(r'^accidents_list/$',
        views.AccidentsListView.as_view(),
        name='accidents_list'),
    url(r'^add_accident/$',
        views.CreateAccidentView.as_view(),
        name='add_accident'),
    url(r'^edit_accident/(?P<pk>\d+)/$',
        views.UpdateAccidentView.as_view(),
        name='edit_accident'),
    url(r'^delete_accident/(?P<pk>\d+)/$',
        views.DeleteAccidentView.as_view(),
        name='delete_accident'),
    url(r'^accident/(?P<pk>\d+)/$',
        views.AccidentView.as_view(),
        name='view_accident'),
    url(r'^accidents/(?P<pk>\d+)/$',
        views.AccidentsView,
        name='accidents'),

    # Statistics:
    url(r'^statistics/$',
        views.StatisticsGeneral,
        name='statistics'),
    url(r'^statistics_json/$',
        views.StatisticsGeneral_json,
        name='statistics_json'),
    url(r'^statistics/$',
        views.StatisticsGeneral,
        name='statistics'),
    url(r'^statistics/$',
        views.StatisticsGeneral,
        name='statistics'),
    url(r'^statisticsclassificationmonth_json/(?P<pk>\d+)/(?P<year>\d+)/(?P<month>\d+)/$',
        views.StatisticsClassificationMonth_json,
        name='StatisticsClassificationMonth_json'),
    url(r'^StatisticsClassification/(?P<pk>\d+)/$',
        views.StatisticsClassification,
        name='StatisticsClassification'),


    url(r'^search_car/$', views.search_car),
    url(r'^license_ids/$', views.license_ids, name='license_ids'),
)
