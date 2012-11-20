from django.db import models
from department.models import department

class professor(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	department = models.ForeignKey(department,null=True)

	def __unicode__(self):
		return self.firstname+' '+self.lastname
