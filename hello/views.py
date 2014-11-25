from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.core.urlresolvers import reverse

from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})



def Home(request):
	x = 0
	y = 0

	try:
		x = Decimal(request.GET.get('x', 0))
		y = Decimal(request.GET.get('y', 0))
	except Exception, e:
		return HttpResponse("Something went wrong: %s" % str(e) )

	result = add_numbers(x,y)
	context = {
		'result': result,
		'user': "david burke" # request.user.first_name
	}
	return render(request, 'save_money_input.html', context)


def SaveMoneyForm(request):
	print request.POST
	text_box = request.POST['txt_value']
	

	return HttpResponseRedirect(reverse('savemoney-home'))

def ShowHistory(request):
	return HttpResponse("Savings History:")


def add_numbers(a,b):
	return a+b




