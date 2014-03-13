from django.conf.urls import patterns, url

import rules.views

urlpatterns = patterns('',
    url(r'^$', rules.views.index, name='rules_index'),
    url(r'^(?P<rule_id>\d+)/$', rules.views.detail, name="rules_detail"),
    url(r'^skills/$', rules.views.s_index, name="skills_index"),
)