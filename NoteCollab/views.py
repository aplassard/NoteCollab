from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
	c={}
	c.update(csrf(request))
	return render_to_response('index.html',c)

def submit(request):
	if request.POST.get("new",False)!=False:
		return signup(request)
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect("/account/loggedin/")
	else:
		return HttpResponseRedirect("/")
	
	
def signup(request):
	c={}
	c.update(csrf(request))
	return render_to_response('signup.html',c)

def newsignup(request):
	c={}
	c.update(csrf(request))
	if request.POST.get("home")=="home":
		return HttpResponseRedirect("/")
	
	if request.POST['email1'] == request.POST['email2'] and request.POST['password1'] == request.POST['password2']:
		user = User.objects.create_user(username=request.POST['email1'],password=request.POST['password1'])
		user.first_name=request.POST.get('firstname','')
		user.last_name=request.POST.get('lastname','')
#		user.save()
		return HttpResponse("Welcome %s"%request.POST['email1'])
	return HttpResponse("Something Went Wrong")