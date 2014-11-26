from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.core.urlresolvers import reverse
from decimal import Decimal
from django.db.models import Count, Min, Sum, Avg
from .models import Greeting, Entry


# Create your views here.
def index(request):
	return HttpResponse('Hello from Python!')


def db(request):
	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})


def Home(request):

	entries = Entry.objects.all().order_by('-date', 'amount')
	total_entries = Entry.objects.aggregate(total=Sum('amount'), average=Avg('amount'))


	total = 0
	for e in entries:
		total += e.amount

	context = {
		'entries': entries,
		'total': total,
		'total_entries': total_entries,
		'user': "david burke" # request.user.first_name
	}
	return render(request, 'save_money_input.html', context)


def SaveMoneyForm(request):
	print request.POST
	text_box = request.POST['txt_value']
	reason = 'None Provided'
	newEntry = Entry()
	newEntry.amount = Decimal(text_box)
	newEntry.reason = reason
	newEntry.save()

	return HttpResponseRedirect(reverse('savemoney-home'))

def ShowHistory(request):
	return HttpResponse("Savings History:")


def add_numbers(a, b):
	return a+b





