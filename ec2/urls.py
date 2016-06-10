<<<<<<< HEAD
from django.conf.urls import patterns, url
from ec2 import views

urlpatterns = patterns('',
                       url(r'^$', views.main, name='main'),
                       url(r'^tab/$', views.tab, name='tab'),
                       )
