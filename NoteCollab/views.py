from student.models import student
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.core.context_processors import csrf

def home(request):
	c={}
	c.update(csrf(request))
	return render_to_response('index.html',c)
