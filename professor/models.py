from django.db import models

class professor(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_lengh=20)
	department = models.ForeignKey(department,null=True)

class department(models.Model):
	name = models.CharField(max_length=20)
