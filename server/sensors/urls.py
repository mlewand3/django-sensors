from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pocketServ.views.home', name='home'),
    url(r'^ajax-gauge-update$', 'pocketServ.views.ajax_gauge_update', name='ajax_gauge_update'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)
