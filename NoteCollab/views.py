from student.models import student
from django.template import Context, loader
from django.http import HttpResponse

def home(request):
	return HttpResponse('Welcome Home!')
