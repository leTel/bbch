from django.conf.urls import patterns, url

import rules.views

urlpatterns = patterns('',
    url(r'^$', rules.views.index, name='index_url'),
    url(r'^(?P<rule_id>\d+)/$', rules.views.detail, name="detail_url"),
    url(r'^skills/$', rules.views.s_index, name="s_index_url"),
)