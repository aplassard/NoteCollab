from django.db import models
from professor.models import professor
from student.models import student

class course(models.Model):
	professor = models.ForeignKey(professor)
	students = models.ManyToManyField(student)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=1000, null=True)

	def __unicode__(self):
		return self.name

