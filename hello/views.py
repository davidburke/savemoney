from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.core.urlresolvers import reverse
from decimal import Decimal
from django.db.models import Count, Min, Sum, Avg
from .models import Greeting, Entry
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
	return HttpResponse('Got any grapes?')


def db(request):
	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})


def Login(request):

	if request.method == 'POST':

		# user = User.objects.create_user('dave', 'dave@dave.com', 'password')
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('savemoney-home'))
			else:
				print('Disabled Account')
				return render(request, 'login.html')
		else:
			print('Invalid login. Please try again')
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')


def LogoutUser(request):

	logout(request)
	return render(request,'logout.html')


def Register(request):

	if request.method == 'POST':
		name = ' '
		un = request.POST['username']
		pw = request.POST['password']
		User.objects.create_user(un, un, pw)

		user = authenticate(username=un, password=pw)
		login(request, user)
		return HttpResponseRedirect(reverse('savemoney-home'))

	else:
		return render(request, 'register.html')


@login_required
def Home(request):

	entries = Entry.objects.filter(user=request.user).order_by('-date', 'amount')[:3]

	total_entries = Entry.objects.filter(user=request.user).aggregate(total=Sum('amount'), average=Avg('amount'))

	context = {
		'entries': entries,
		'total_entries': total_entries,
		'user': request.user.username
	}

	return render(request, 'save_money_input.html', context)


def SaveMoneyForm(request):


	print request.POST
	text_box = request.POST['txt_value']
	reason = 'None Provided'
	newEntry = Entry()
	newEntry.user = request.user
	newEntry.amount = Decimal(text_box)
	newEntry.reason = reason
	newEntry.save()

	return HttpResponseRedirect(reverse('savemoney-home'))


@login_required
def ShowHistory(request):

	entries = Entry.objects.filter(user=request.user).order_by('-date', 'amount')
	total_entries = Entry.objects.filter(user=request.user).aggregate(total=Sum('amount'), average=Avg('amount'))


	"""
	# redundant total
	total = 0
	for e in entries:
		total += e.amount
	"""
	context = {
		'entries': entries,
		'total_entries': total_entries,
		'user': request.user.username
	}

	return render(request, 'show_history.html', context)


@csrf_exempt
def ProcessUpdate(request):

	print request.POST
	row_pk = request.POST['pk']
	row_value = request.POST['value']

	Entry.objects.filter(pk=row_pk, user=request.user).update(amount=row_value)

	return HttpResponse('Test')


@csrf_exempt
def ProcessDelete(request):


	row_pk = request.GET['id']

	Entry.objects.filter(pk=row_pk, user=request.user).delete()

	return HttpResponseRedirect(reverse('show-history-form'))


def add_numbers(a, b):
	return a+b


def Goals(request):
	return render(request, 'goals.html')


def Contact(request):
	return render(request, 'contact.html')

def Account(request):
	return render(request, 'account.html')