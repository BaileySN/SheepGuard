from django.conf.urls import patterns, url
from sheep import views


urlpatterns = patterns('',
                       url(r'^$', views.SheepList.as_view(), name='sheep_list'),
                       url(r'^new$', views.SheepCreate.as_view(), name='sheep_new'),
                       url(r'^edit/(?P<pk>\d+)$', views.SheepUpdate.as_view(), name='sheep_edit'),
                       url(r'^delete/(?P<pk>\d+)$', views.SheepDelete.as_view(), name='sheep_delete'),
                       url(r'^pasture/$', views.PastureList.as_view(), name='pasture_list'),
                       url(r'^pasture/new$', views.PastureCreate.as_view(), name='pasture_new'),
                       url(r'^pasture/edit/(?P<pk>\d+)$', views.PastureUpdate.as_view(), name='pasture_edit'),
                       url(r'^pasture/delete/(?P<pk>\d+)$', views.PastureDelete.as_view(), name='pasture_delete'),
                       )

