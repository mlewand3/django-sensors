from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'sensors.views.home', name='home'),
    url(r'^update-readings/?$', 'sensors.views.update_sensors', name='update_readings'),
    url(r'^ajax-gauge-update/?$', 'sensors.views.ajax_gauge_update', name='ajax_gauge_update'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)
