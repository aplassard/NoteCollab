from course.models import course
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def index(request):
    courses = course.objects.all()
    c={}
    c.update(csrf(request))
    c['courses']=courses
    return render_to_response('course/index.html',c)