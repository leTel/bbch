from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

import auth.forms

def connection(request, logout_flag=False, log_required=False):
	
	if request.method == 'POST' :
		form = auth.forms.LoginForm(request.POST)
		if form.is_valid() :
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']
			create_new_user = form.cleaned_data['new_account']

			#Create new user
			if create_new_user :
				if clean_password(form) :
					user = User.objects.create_user(username=username, password=password, email=email)
				else :
					context={
			 		'form' : form,
			 		'credential_error' : False,
			 		'loged_in' : False,
			 		'password_confirm_error' : True,
				 	}
				 	return render(request, 'auth/connection.html', context)

			user = authenticate(username=username, password=password)
			

			if user is not None:
				if user.is_active:

					login(request, user)
				 	context={
				 		'username' : request.user,
				 		'loged_in' : request.user.is_authenticated(),
				 	}
				 	return HttpResponseRedirect(reverse('home_log_message'))
					
				else:
					# Return a 'disabled account' error message
					pass
			else:
			 	context={
			 		'form' : form,
			 		'credential_error' : True,
			 		'loged_in' : False,
			 	}
				
		return render(request, 'auth/connection.html', context)
		

	elif request.method =='GET' :
		form = auth.forms.LoginForm()

		if logout_flag :
			logout(request)

 	context={
 		'log_required' :log_required,
 		'loged_out' : logout_flag,
 		'username' : request.user,
 		'form' : form,
 		'credential_error' : False,
 		'loged_in' : request.user.is_authenticated(),
 	}
	return render(request, 'auth/connection.html', context)

@login_required
def user_profile(request):

	if request.method == 'POST' :
		form = auth.forms.ProfileForm(request.POST)
		if form.is_valid() :
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']

			request.user.first_name = first_name
			request.user.last_name = last_name
			request.user.email = email

			request.user.save()

			alert = _("Your profile has been updated !")
			

		 	context={
		 		'alert_content' : alert,
			 	'form' : form,
			 	'user': request.user,
			 	'username' : request.user,
				'loged_in' : request.user.is_authenticated(),
			}

			return render(request, 'auth/user_profile.html', context)		

	elif request.method =='GET':

		form = auth.forms.ProfileForm({
			'email' : request.user.email,
			'first_name' : request.user.first_name,
			'last_name' : request.user.last_name,
		})

	 	context={
		 	'form' : form,
		 	'user': request.user,
		 	'username' : request.user,
			'loged_in' : request.user.is_authenticated(),
		}	

		return render(request, 'auth/user_profile.html', context)


def clean_password(form):

	password1 = form.cleaned_data['password']
	password2 = form.cleaned_data['passwordCheck']

	if password1 != password2:
		return False

	return True
