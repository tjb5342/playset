from django.conf.urls import patterns, include, url
from django.conf import settings
from django.shortcuts import render_to_response

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^tango_with_django_project/', include('tango_with_django_project.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    # url('r^admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^playset/', include('playset.urls', namespace='playset')),
)
