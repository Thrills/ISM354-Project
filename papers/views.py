from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import Http404
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


from .models import Paper, Review, MyUser

from .forms import PaperForm, ReviewForm, RegisterForm, LoginForm

def home(request):
	title = '' # no nice welcome msg for anon users
	#if request.user.is_authenticated():
	#	title = "Welcome %s" %(request.user) #Displays a personalised welcome msg

	#gonna add a form here apparently
	context = {
		"title": title,
	}
	return render(request, "home.html", context)

# -----------------------needs to be commented out if you want to create a new superuser
def registration(request):

	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		new_user.set_password(password)
		new_user.first_name = first_name
		new_user.last_name = last_name
		new_user.save()
		return HttpResponseRedirect(reverse('login'))

	context = {
		"form": form,
		"action_value": "",
		"submit_btn_value": "Register"
	}
	return render(request, "registration.html", context)

def paper_sub(request):
	form = PaperForm()
	if request.method == 'POST':
		form = PaperForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('paper_sub')

		else:
			form = PaperForm()
		return render(request, 'paper_sub.html', {'form': form})

	# Load document list
	paper_list = Paper.objects.all()

	# Render list page with documents and form
	return render_to_response(
			'paper_sub.html',
			{'paper_list': paper_list, 'form': form},
			context_instance=RequestContext(request)
			)

	
	# return render(request, 'paper_sub.html', {'form': form})


def review_sub(request):
	form = ReviewForm()
	if request.method == 'POST':
		form = ReviewForm(request.POST or None)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('review_sub')

		else:
			form = ReviewForm()
		return render(request, 'review_sub.html', {'form': form})

	# Load document list
	paper_list = Paper.objects.all()

	# Render list page with documents and form
	return render_to_response(
			'paper_sub.html',
			{'paper_list': paper_list, 'form': form},
			context_instance=RequestContext(request)
			)


	return render(request, 'review_sub.html', context)
			

def about(request):
	return render(request, "about.html", {})

def auth_login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():						#Make sure that user exists
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)	#Authentication
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('home'))			

	context = {"form": form}
	return render(request, 'login.html', context)

def auth_logout(request):
	logout(request)
	#return HttpResponseRedirect('/')
	return render(request, 'logout.html')


def index(request):
    paper_list = Paper.objects.order_by('-Paper_SubmissionDate')[:5] # Need to adjust this !
    context = {'paper_list': paper_list}
    return render(request, 'papers/index.html', context)

