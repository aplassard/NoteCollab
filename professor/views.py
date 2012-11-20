from professor.models import professor
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response, redirect

def index(request):
    c={}
    c.update(csrf(request))
    professors=professor.objects.all()
    if len(professors)>0:
        c['p']=professor
    else:
        c['p']=None
    return render_to_response('professor/index.html',c)