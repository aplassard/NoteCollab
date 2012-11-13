from django.db import models

class department(models.Model):
	name = models.CharField(max_length=20)

class professor(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	department = models.ForeignKey(department,null=True)

	def __unicode__(self):
		return firstname+' '+lastname
