from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import forum.models

@login_required
def index(request) :
	context = {
		'forums_set' : forum.models.Forum.objects.all(),
		'username' : request.user,
		'loged_in' : request.user.is_authenticated(),
	}

	return render(request, 'forum/index.html', context)

