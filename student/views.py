from student.models import student
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf


def students(request):
	students = student.objects.all()
	c={}
	c.update(csrf(request))
	c['s']=students
	return render_to_response('student/index.html',c)


def info(request, pk):
	s = student.objects.get(id=pk)
	C = Context({'student':s})
	return render_to_response('student/student.html',C,context_instance=RequestContext(request))

def submit(request,pk):
	c = {}
	c.update(csrf(request))
	p = get_object_or_404(student, id=pk)
	a=request.POST.get('firstname',False)
	if a:
		p.firstname=a
	a=request.POST.get('lastname',False)
	if a:
		p.lastname=a
	a=request.POST.get('grade',False)
	if a:
		p.grade=a
	p.save()
	return render_to_response('student/submitted.html',{})

def new(request):
	s=student()
	s.firstname=""
	s.lastname=""
	s.grade=""
	s.save()
	return redirect("/student/%s/" % s.id)

def delete(request):
	c = {}
	c.update(csrf(request))
	o=[]
	a=request.POST.getlist('student',False)
	if 'new' in request.POST:
		return redirect("/student/new/")
	if a:
		if len(a)>0:
			for s in a:
				p=get_object_or_404(student,id=s)
				o.append(p.id)
				p.delete()
	else:
		return redirect("/student/")
	c['s']=o
	return render_to_response('student/deleted.html',c)
