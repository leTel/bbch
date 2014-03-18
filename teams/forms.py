from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _

class CreateTeamForm(forms.Form):
	name = forms.CharField(label=_("Name"), widget=forms.TextInput(attrs={'autofocus': 'autofocus',}))
	reroll_value = forms.IntegerField(label=_("Reroll value"),initial=50000, min_value=50000, max_value=100000, widget=forms.NumberInput(attrs={'step':'10000'}),)
	reroll = forms.IntegerField(label=_("Reroll"), initial=0, min_value=0,)
	new_team = forms.BooleanField(required=False)
	apo = forms.BooleanField(label=_("Apothicary"),required=False,)
	assistant = forms.IntegerField(label=_("Assistant"), initial=0, min_value=0,)
	pompom = forms.IntegerField(label=_("Pom-pom girls"), initial=0, min_value=0,)
	pop = forms.IntegerField(label=_("Popularity"), initial=0, min_value=0,)
	value = forms.IntegerField(label=_("Team value"), initial=0, widget=forms.NumberInput(attrs={'readonly':'readonly', 'step':'10000'}),)
	treasury = forms.IntegerField(label=_("Treasury"), initial=1000000, widget=forms.NumberInput(attrs={'readonly':'readonly', 'step':'10000'}),)


class CreatePlayerForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus',}))
	position = forms.CharField()
	number = forms.IntegerField(min_value=0,)
	new_player = forms.BooleanField(required=False)