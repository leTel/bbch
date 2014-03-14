from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import teams.models
import teams.forms

@login_required
def index(request) :
	if request.method == 'POST' :

		form = teams.forms.CreateTeamForm(request.POST)
		if form.is_valid() :
			create_new_team = form.cleaned_data['new_team']
			t_name = form.cleaned_data['name']
			p_name = form.cleaned_data['p_name']
			p_position = form.cleaned_data['p_position']
			p_number = form.cleaned_data['p_number']

			if create_new_team :
				team = teams.models.Team(name=t_name, coach=request.user.username)
				team.save()

				team.player_set.create(name=p_name, position=p_position, number=p_number)
				

				team_set = teams.models.Team.objects.filter(coach=request.user.username)
				context = {
					'teams' : team_set,
					'username' : request.user,
					'loged_in' : request.user.is_authenticated(),
				}

				return render(request, 'teams/index.html', context)

		else :
			team_set = teams.models.Team.objects.filter(coach=request.user.username)
			errors = form.errors
			form = teams.forms.CreateTeamForm()
			context = {
				'create_team_form' : form,
				'alert_form' : errors,
				'teams' : [],
				'username' : request.user,
				'loged_in' : request.user.is_authenticated(),
			}

			return render(request, 'teams/index.html', context)

	elif request.method == 'GET' :
		team_set = teams.models.Team.objects.filter(coach=request.user.username)
		form = teams.forms.CreateTeamForm()
		context = {
			'create_team_form' : form,
			'teams' : team_set,
			'username' : request.user,
			'loged_in' : request.user.is_authenticated(),
		}

		return render(request, 'teams/index.html', context)