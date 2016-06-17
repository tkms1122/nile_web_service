from django.conf.urls import patterns, include, url
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'accounts/logged_out.html'}),
    url(r'^user-creation/$', views.AccountCreateView.as_view(), name='user_creation'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.AccountUpdateView.as_view(), name='user_change'),
)
