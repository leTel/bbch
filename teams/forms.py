from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

class CreateTeamForm(forms.Form):
	name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={'autofocus': 'autofocus',}))
	reroll_value = forms.IntegerField(label=_("Reroll value - in KPO"), initial=50, min_value=50, max_value=100)
	reroll = forms.IntegerField(label=_("Reroll"), initial=0, min_value=0,)
	new_team = forms.BooleanField(required=False)
	apo = forms.BooleanField(label=_("Apothicary"),)
	assistant = forms.IntegerField(label=_("Assistant"), initial=0, min_value=0,)
	pompom = forms.IntegerField(label=_("Pom-pom girls"), initial=0, min_value=0,)
	pop = forms.IntegerField(label=_("Popularity"), initial=0, min_value=0,)
	value = forms.IntegerField(label=_("Team value"), initial=0, widget=forms.TextInput(attrs={'readonly':'readonly'}),)
	treasury = forms.IntegerField(label=_("Treasury"), initial=1000, widget=forms.TextInput(attrs={'readonly':'readonly'}),)


class CreatePlayerForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus',}))
	position = forms.CharField()
	number = forms.IntegerField(min_value=0,)
	new_player = forms.BooleanField(required=False)