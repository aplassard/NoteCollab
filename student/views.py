from student.models import student

def students(request):
	students = student.objects.all()
	t=loader.get_template('student/index.html')
	HttpResponse(t.render(Context({'s':students})))
