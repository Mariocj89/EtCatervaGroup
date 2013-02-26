from django.conf.urls import patterns, include, url
from os import path

urlpatterns = patterns('EtCaterva.views',
    url(r'^$', 'home', name='home'),                   
)
