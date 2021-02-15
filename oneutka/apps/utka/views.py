from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Utka

def index(request):
	latest_utka_list = Utka.objects.order_by('-pub_date')[:5]
	return render(request, 'utka/list.html', {'latest_utka_list': latest_utka_list})


def detail(request, utka_id):
	try:
		a = Utka.objects.get( id = utka_id )
	except:
		raise Http404('Статья не найдена!')

	latest_comment_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'utka/detail.html', {'utka': a, 'latest_comment_list': latest_comment_list})


def leave_comment(request, utka_id):
	try:
		a = Utka.objects.get( id = utka_id )
	except:
		raise Http404('Статья не найдена!')
	
	a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

	return HttpResponseRedirect( reverse('utka:detail', args=(a.id,)) )