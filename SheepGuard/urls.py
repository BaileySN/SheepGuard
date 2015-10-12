from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'sheepguard/login.html'}),
    url(r'^accounts/logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^sheep/', include('sheep.urls', namespace='sheep')),
    url(r'^customers', include('customer.urls', namespace='customers')),
    url(r'^$', 'SheepGuard.views.index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
