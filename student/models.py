from django.db import models

class student(models.Model):
	firstname = models.CharField(max_length=25,null=True,blank=True)
	lastname = models.CharField(max_length=25,null=True,blank=True)
	
	GRADES=(
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)
	grade = models.CharField(max_length=10,choices=GRADES,null=True,blank=True)

	def __unicode__(self):
		return self.firstname+' '+self.lastname
