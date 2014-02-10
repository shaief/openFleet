from django.conf.urls import patterns, include, url
from effectiveCar import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openFleet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

########################################################################
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
)
