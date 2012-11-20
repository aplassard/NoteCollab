from professor.models import professor
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response, redirect

def index(request):
    c={}
    c.update(csrf(request))
    professors=professor.objects.all()
    c['p']=professor
    return render_to_response('professor/index.html',c)