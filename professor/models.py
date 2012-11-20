from django.db import models

class professor(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	department = models.CharField(max_length=50)

	def __unicode__(self):
		return self.firstname+' '+self.lastname
