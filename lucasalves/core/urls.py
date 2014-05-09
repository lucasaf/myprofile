# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('lucasalves.core.views',
    url(r'^$', 'index', name='index'),
)
