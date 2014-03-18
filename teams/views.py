from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import teams.models
import teams.forms

@login_required
def index(request, add_new_team=False) :
	if request.method == 'POST' :

		t_form = teams.forms.CreateTeamForm(request.POST)
		p_form = teams.forms.CreatePlayerForm(request.POST)
		t_errors = t_form.errors
		p_errors = p_form.errors

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
				
				name = t_form.cleaned_data['name']
				reroll = t_form.cleaned_data['reroll']
				apo = t_form.cleaned_data['apo']
				assistant = t_form.cleaned_data['assistant']
				pompom = t_form.cleaned_data['pompom']
				pop = t_form.cleaned_data['pop']
				value = t_form.cleaned_data['value']
				treasury = t_form.cleaned_data['treasury']
			
				team = teams.models.Team(
					name=name,
					coach=request.user.username,
					reroll=reroll,
					apo=apo,
					assistant=assistant,
					pompom=pompom,
					pop=pop,
					value=value,
					treasury=treasury,
					)
				team.save()

				team_set = teams.models.Team.objects.filter(coach=request.user.username)
				player_form = teams.forms.CreatePlayerForm()
				context = {
					'tab_id': team.id,
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
				team.value = team.value + team.player_set.get(number=number).value
				team.treasury = team.treasury - team.player_set.get(number=number).value
				team.save()
				
				team_set = teams.models.Team.objects.filter(coach=request.user.username)
				player_form = teams.forms.CreatePlayerForm()
				context = {
					'tab_id': team.id,
					'create_player_form' : player_form,
					'teams' : team_set,
					'username' : request.user,
					'loged_in' : request.user.is_authenticated(),
				}
				return render(request, 'teams/index.html', context)

		else :
			team_set = teams.models.Team.objects.filter(coach=request.user.username)
			team_form = teams.forms.CreateTeamForm()
			player_form = teams.forms.CreatePlayerForm()

			context = {
			'create_player_form' : player_form,
			'create_team_form' : team_form,
			'alert_form_player' : p_errors,
			'alert_form_team' : t_errors,
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
			'add_new_team': add_new_team,
			'create_player_form' : player_form,
			'create_team_form' : team_form,
			'teams' : team_set,
			'username' : request.user,
			'loged_in' : request.user.is_authenticated(),
		}

		return render(request, 'teams/index.html', context)

def delete_team(request, team_id=-1):
	team = teams.models.Team.objects.get(id=team_id)
	team.delete()

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

def delete_player(request, player_id=-1):
	player = teams.models.Player.objects.get(id=player_id)
	team_id = player.team_id
	player.delete()

	team_set = teams.models.Team.objects.filter(coach=request.user.username)
	team_form = teams.forms.CreateTeamForm()
	player_form = teams.forms.CreatePlayerForm()

	context = {
		'tab_id': team_id,
		'create_player_form' : player_form,
		'create_team_form' : team_form,
		'teams' : team_set,
		'username' : request.user,
		'loged_in' : request.user.is_authenticated(),
	}

	return render(request, 'teams/index.html', context)