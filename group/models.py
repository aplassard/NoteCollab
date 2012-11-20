from django.db import models
from student.models import student
from course.models import course

class group(models.Model):
    students = models.ManyToManyField(student)
    course = models.ForeignKey(course)
    
    def __unicode__(self):
        return str(self.course) +': '+str(self.id)