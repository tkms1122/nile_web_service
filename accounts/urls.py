from django.conf.urls import patterns, include, url
from accounts import views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login_with_template'),
    url(r'^login/$', views.log_in, name='login_with_template'),
    url(r'^logout/$', auth_views.logout,
    {
        'template_name': 'accounts/logged_out.html',
    },
    name='logout_with_template'
    ),
    url(r'^password-change/$',
        auth_views.password_change,
        {
            'post_change_redirect': reverse_lazy('accounts:pwd_change_done'),
            'template_name': 'accounts/password_change_form.html',
        },
        name='pwd_change'
    ),
    url(r'^password-change-done/$',
        auth_views.password_change_done,
        {
            'template_name': 'accounts/password_change_done.html',
        },
        name='pwd_change_done'
    ),
    url(r'^user-creation/$', views.AccountCreateView.as_view(), name='user_creation'),
    url(r'^signin/$',views.signin),
)
