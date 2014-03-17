from django.conf.urls import patterns, url

import teams.views

urlpatterns = patterns('',
    url(r'^$', teams.views.index, name='teams_index'),
    url(r'^new-team/', teams.views.index, {'add_new_team':True}, name='teams_index_new_team'),
    url(r'^delete/', teams.views.delete_team, name='delete_team_url'), #(?P<team_id>\d+)

)