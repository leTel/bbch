from django.conf.urls import patterns, url

import teams.views

urlpatterns = patterns('',
    url(r'^$', teams.views.index, name='index_url'),
    url(r'^new-team/$', teams.views.index, {'add_new_team':True}, name='index_new_team_url'),
    url(r'^delete/(?P<team_id>\d+)$', teams.views.delete_team, name='delete_team_url'),

)