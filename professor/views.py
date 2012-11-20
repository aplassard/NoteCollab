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

def submit(request):
    if 'new' in request.POST:
        return redirect('/professor/new/')
    return redirect('/professor/')
    
def new(request):
    p=professor()
    p.firstname=""
    p.lastname=""
    p.department=""
    p.save()
    return redirect("/professor/%s/" % p.id)

def info(request,pk):
    p=get_object_or_404(professor,id=pk)
    c=Context({'professor':p})
    c.update(csrf(request))
    return render_to_response('professor/professor.html',c)