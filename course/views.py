from professor.models import professor
from course.models import course
from student.models import student
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response, redirect

def index(request):
    courses = course.objects.all()
    c={}
    c.update(csrf(request))
    c['courses']=courses
    return render_to_response('course/index.html',c)

def submit(request):
    if 'new' in request.POST:
        return redirect('/course/new')
    elif 'delete' in request.POST:
        return delete(request)
    else:
        return redirect('/course/')
    
def delete(request):
    c = {}
    c.update(csrf(request))
    a=request.POST.getlist('course', False)
    o=[]
    if a and len(a)>0:
        for s in a:
            p=get_object_or_404(course,id=s)
            o.append(p.name)
            p.delete()
    else:
        return redirect("/course/")
    c['c']=o
    return render_to_response('course/deleted.html',c)

def new(request):
    a=course()
    a.name=""
    a.description=""
    a.professor=professor("")
    a.save()
    return redirect("/course/%s/"%a.id)

def info(request,pk):
    a=get_object_or_404(course,id=pk)
    c={}
    c.update(csrf(request))
    c['course']=a
    if a.professor:
        p=a.professor
        c['professor']=p
    else:
        c['professor']=False
    professors=professor.objects.all()
    c['professors']=professors
    c['classstudents']=a.students
    c['allstudents']=student.objects.all()
    return render_to_response('course/course.html',c)

def submitinfo(request,pk):
    c = {}
    c.update(csrf(request))
    p=get_object_or_404(course,id=pk)
    a=request.POST.get('name',False)
    if a:
        p.name=a
    a=request.POST.get('description',False)
    if a:
        p.description=a
    a=request.POST.get('professor',False)
    if a:
        p.professor=professor.objects.get(id=int(a))
    p.save()
    return render_to_response('course/submitted.html',c)