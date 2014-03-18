from django.conf.urls import patterns, url

import auth.views

urlpatterns = patterns('',
    url(r'^$', auth.views.connection, name='connection_url'),
    url(r'^logout/', auth.views.connection, {'logout_flag':True}, name='connection_logout_url'),
    url(r'^profile/', auth.views.user_profile, name='user_profile_url'),
)