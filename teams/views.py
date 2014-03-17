from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import teams.models
import teams.forms

@login_required
def index(request) :
	if request.method == 'POST' :

		t_form = teams.forms.CreateTeamForm(request.POST)
		p_form = teams.forms.CreatePlayerForm(request.POST)

		if t_form.is_valid() :
			create_new_team = t_form.cleaned_data['new_team']
		else : 
			create_new_team = False

		if p_form.is_valid() :
			add_player = p_form.cleaned_data['new_player']
		else :
			add_player  = False

		if create_new_team :
			
			if t_form.is_valid() :
				
				t_name = t_form.cleaned_data['name']
				p_name = t_form.cleaned_data['p_name']
				p_position = t_form.cleaned_data['p_position']
				p_number = t_form.cleaned_data['p_number']
				t.size = 1
			
				team = teams.models.Team(name=t_name, coach=request.user.username)
				team.save()

				team.player_set.create(name=p_name, position=p_position, number=p_number)

				team_set = teams.models.Team.objects.filter(coach=request.user.username)
				player_form = teams.forms.CreatePlayerForm()
				context = {
					'create_player_form' : player_form,
					'teams' : team_set,
					'username' : request.user,
					'loged_in' : request.user.is_authenticated(),
				}

				return render(request, 'teams/index.html', context)

		elif add_player :
			if p_form.is_valid() :

				name = p_form.cleaned_data['name']
				position = p_form.cleaned_data['position']
				number = p_form.cleaned_data['number']
				team_id = request.POST.get('team_id')
				team = teams.models.Team.objects.get(coach=request.user.username, id=team_id)

				team.player_set.create(name=name, position=position, number=number)
				team.size = team.player_set.count()
				team.save()
				
				team_set = teams.models.Team.objects.filter(coach=request.user.username)
				player_form = teams.forms.CreatePlayerForm()
				context = {
					'create_player_form' : player_form,
					'teams' : team_set,
					'username' : request.user,
					'loged_in' : request.user.is_authenticated(),
				}

				return render(request, 'teams/index.html', context)

		else :
			team_set = teams.models.Team.objects.filter(coach=request.user.username)
			errors = t_form.errors + p_forms.errors
			team_form = teams.forms.CreateTeamForm()
			player_form = teams.forms.CreatePlayerForm()

			context = {
			'create_player_form' : player_form,
			'create_team_form' : team_form,
			'alert_form' : errors,
			'teams' : team_set,
			'username' : request.user,
			'loged_in' : request.user.is_authenticated(),
			}

			return render(request, 'teams/index.html', context)

	elif request.method == 'GET' :
		team_set = teams.models.Team.objects.filter(coach=request.user.username)
		team_form = teams.forms.CreateTeamForm()
		player_form = teams.forms.CreatePlayerForm()

		context = {
			'create_player_form' : player_form,
			'create_team_form' : team_form,
			'teams' : team_set,
			'username' : request.user,
			'loged_in' : request.user.is_authenticated(),
		}

		return render(request, 'teams/index.html', context)