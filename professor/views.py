from professor.models import professor
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext


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

def submitinfo(request,pk):
    c={}
    c.update(csrf(request))
    p = get_object_or_404(professor,id=pk)
    a=request.POST.get('firstname',False)
    if a:
        p.firstname=a
    a=request.POST.get('lastname',False)
    if a:
        p.lastname=a
    a=request.POST.get('department',False)
    if a:
        p.department=a
    p.save()
    return render_to_response('professor/submitted.html',c)
