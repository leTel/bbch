from django.conf.urls import patterns, url

import auth.views

urlpatterns = patterns('',
    url(r'^$', auth.views.connection, name='connection'),
    url(r'^logout/', auth.views.connection, {'logout_flag':True}, name='connection_logout'),
)