from student.models import student
from django.template import Context, loader
from django.http import HttpResponse

def students(request):
	students = student.objects.all()
	t=loader.get_template('student/index.html')
	return HttpResponse(t.render(Context({'s':students})))

def info(request, pk):
	s = student.objects.get(id=pk)
	C = Context({'student':s})
	t=loader.get_template('student/student.html')
	return HttpResponse(t.render(C))

