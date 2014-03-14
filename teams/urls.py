from django.conf.urls import patterns, url

import teams.views

urlpatterns = patterns('',
    url(r'^$', teams.views.index, name='teams_index'),

)