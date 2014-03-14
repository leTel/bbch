from django.conf.urls import patterns, include, url
from django.contrib import admin

import bbch.views
import auth.views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^auth/', include('auth.urls', namespace="auth")),
    url(r'^rules/', include('rules.urls', namespace="rules")),
    url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^teams/', include('teams.urls', namespace="teams")),

    url(r'^accounts/login/$', auth.views.connection, {'log_required':True}),
    url(r'^home/log_in/$', bbch.views.home, {'log_message':True}, name="home_log_message"),
    url(r'^home/$', bbch.views.home, name="bbch"),
    url(r'^$',  bbch.views.home, name="bbch"),

)
