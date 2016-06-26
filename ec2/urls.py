from django.conf.urls import patterns, url
from ec2 import views

urlpatterns = patterns('',
                       url(r'^$', views.machines_index, name='root'),
                       url(r'^home/$', views.machines_index, name='home'),
                       url(r'^machines/$', views.machines_index, name='machines'),
                       url(r'^machines/launch$', views.machines_launch, name='launch'),
                       url(r'^machines/destroy-(?P<machine_token>.+)/$', views.machines_destroy, name='destroy'),
                       url(r'^downloadkey-(?P<machine_token>.+)/$', views.machines_downloadkey, name='downloadkey'),
                       url(r'^machines/list$', views.machines_getlist, name='getlist'),
                       # url(r'^machines/(\d+)$', views.machines_show),
                       # url(r'^machines/new$', views.machines_new),
                       # url(r'^machines/create$', views.machines_create), POST
                       # url(r'^machines/destroy$', views.machines_destroy), POST
                       )
