from django.conf.urls import patterns, url
from customer import views


urlpatterns = patterns('',
                       url(r'^$', views.CustomerList.as_view(), name='customer_list'),
                       url(r'^new$', views.CustomerCreate.as_view(), name='customer_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.CustomerUpdate.as_view(), name='customer_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.CustomerDelete.as_view(), name='customer_delete'),
                       url(r'^profession/$', views.ProfessionList.as_view(), name='profession_list'),
                       url(r'^profession/new$', views.ProfessionCreate.as_view(), name='profession_new'),
                       url(r'^profession/edit/(?P<pk>\d+)$', views.ProfessionUpdate.as_view(), name='profession_edit'),
                       url(r'^profession/delete/(?P<pk>\d+)$', views.ProfessionDelete.as_view(), name='profession_delete'),
                       url(r'^title/$', views.TitleList.as_view(), name='title_list'),
                       url(r'^title/new$', views.TitleCreate.as_view(), name='title_new'),
                       url(r'^title/edit/(?P<pk>\d+)$', views.TitleUpdate.as_view(), name='title_edit'),
                       url(r'^title/delete/(?P<pk>\d+)$', views.TitleDelete.as_view(), name='title_delete'),
                       )
