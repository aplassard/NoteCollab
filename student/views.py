from student.models import student
from django.template import Context, loader

def students(request):
	students = student.objects.all()
	t=loader.get_template('student/index.html')
	HttpResponse(t.render(Context({'s':students})))
