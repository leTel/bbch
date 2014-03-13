from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

import poll.models

@login_required
def index(request):
    latest_poll_list = poll.models.Poll.objects.all().order_by('-pub_date')[:5]
    context = {
        'username' : request.user,
        'loged_in' : request.user.is_authenticated(),
        'latest_poll_list': latest_poll_list
        }
    return render(request, 'poll/index.html', context)
@login_required
def detail(request, poll_id):
    p = get_object_or_404(poll.models.Poll, id=poll_id)
    return render(request, 'poll/detail.html', {'poll': p})
@login_required
def results(request, poll_id):
    p = get_object_or_404(poll.models.Poll, id=poll_id)
    return render(request, 'poll/results.html', {'poll': p})
@login_required
def vote(request, poll_id):
    p = get_object_or_404(poll.models.Poll, id=poll_id)
    try:
        selected_choice = p.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'poll/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('poll:results', args=(p.id,)))