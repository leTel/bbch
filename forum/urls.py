from django.conf.urls import patterns, url

import forum.views

urlpatterns = patterns('',
    url(r'^$', forum.views.index, name='forum_index'),
)