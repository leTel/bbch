from django.conf.urls import patterns, url

import teams.views

urlpatterns = patterns('',
    url(r'^$', teams.views.index, name='index_url'),
    url(r'^new-team/$', teams.views.index, {'add_new_team':True}, name='index_new_team_url'),
    url(r'^delete-t/(?P<team_id>\d+)$', teams.views.delete_team, name='delete_team_url'),
    url(r'^delete-p/(?P<player_id>\d+)$', teams.views.delete_player, name='delete_player_url'),
    url(r'^add_apo/(?P<team_id>\d+)$', teams.views.add_apo, name='add_apo_url'),
    url(r'^add_pompom/(?P<team_id>\d+)$', teams.views.add_pompom, name='add_pompom_url'),
    url(r'^add_assistant/(?P<team_id>\d+)$', teams.views.add_assistant, name='add_assistant_url'),

)