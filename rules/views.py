from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import translation

import rules.models

@login_required
def index(request) :
	rules_set = rules.models.Rule.objects.all()

	context = {
		'rules' : rules_set,
		'username' : request.user,
		'loged_in' : request.user.is_authenticated(),
	}

	return render(request, 'rules/index.html', context)

@login_required
def detail(request, rule_id=-1) :
	if rule_id is -1 :
		pass
	else :
		rule = rules.models.Rule.objects.get(id=rule_id).description
	
	context = {
		'rule' : rule,
		'username' : request.user,
		'loged_in' : request.user.is_authenticated(),
	}

	return render(request, 'rules/detail.html', context)

@login_required
def s_index(request) :
	if translation.get_language() == 'fr' :
		skills_set = rules.models.SkillFR.objects.all().order_by('name')
	else :
		skills_set = rules.models.Skill.objects.all().order_by('name')

	context = {
		'skills' : skills_set,
		'username' : request.user,
		'loged_in' : request.user.is_authenticated(),
	}

	return render(request, 'rules/s_index.html', context)