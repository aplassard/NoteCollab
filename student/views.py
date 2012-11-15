from student.models import student
from django.template import Context, loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse


def students(request):
	students = student.objects.all()
	t=loader.get_template('student/index.html')
	return HttpResponse(t.render(Context({'s':students})))

def info(request, pk):
	s = student.objects.get(id=pk)
	C = Context({'student':s})
	t=loader.get_template('student/student.html')
	return HttpResponse(t.render(C))

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
	a.save()
	return HttpResponse("Submitted")
#	return HttpResponseRedirect(
#	reverse('student.views.submitted',args=(a.id,))
#	)

def submitted(request,pk):
	return render_to_response('student/submitted.html',RequestContext(request))