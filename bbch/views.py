from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import translation

import news.models

@login_required
def home(request, log_message=False):


	news_set = news.models.New.objects.all()
		
 	context={
 		'news_set' : news_set,
 		'username' : request.user,
 		'log_message' : log_message,
 		'loged_in' : request.user.is_authenticated(),
 	}
	return render(request, 'bbch/home.html', context)