from django import forms

class CreateTeamForm(forms.Form):
	name = forms.CharField()
	new_team = forms.BooleanField(required=False)
	p_name = forms.CharField()
	p_position = forms.CharField()
	p_number = forms.IntegerField()

class CreatePlayerForm(forms.Form):
	name = forms.CharField()
	position = forms.CharField()
	number = forms.IntegerField()
	new_player = forms.BooleanField(required=False)