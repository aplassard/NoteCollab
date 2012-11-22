from professor.models import professor
from course.models import course
from student.models import student
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response, redirect
from pymongo import Connection

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
    names=[]
    stud=a.students.all()
    for s in stud:
        names.append(s.id)
    c['classstudents']=names
    names=[]
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
    inids=request.POST.getlist('students',False)
    if inids:
        listids=[]
        b=p.students.all()
        for s in b:
            listids.append(s.id)
        for s in listids:
            if s not in inids:
                p.students.remove(s)
        for s in inids:
            if s not in listids:
                p.students.add(student.objects.get(id=s))
    p.save()
    return render_to_response('course/submitted.html',c)

def notes(request,pk):
    connection = Connection('ds031087.mongolab.com',31087)
    db = connection['notecollab']
    db.authenticate('andrew','password')
    notes = db['notes']
    classnotes = notes.find({"class":pk})
    notelist=[]
    for n in classnotes:
        if n.has_key('name') and n.has_key('pid'):
            notelist.append(note(name=n['name'],num=n['_id']))
    c={}
    c.update(csrf(request))
    c['notes']=notelist
    c['pk']=pk
    return render_to_response('course/notes.html',c)

class note(object):
    def __init__(self,name="",num=None):
        self.name=name
        self.num=num
        
def newnote(request,pk):
    connection = Connection('ds031087.mongolab.com',31087)
    db = connection['notecollab']
    db.authenticate('andrew','password')
    notes = db['notes']
    try:
        newestnote = notes.find({'course':pk}).sort("pid")[0]
        nextval=newestnote["pid"]+1
    except:
        nextval=0
    newobject={
        'name' : "",
        'pid' : nexval,
    }
    return redirect("/course/"+str(pk)+"/note/"+str(nextval)+"/")

def noteinfo(request,pk,n):
    connection = Connection('ds031087.mongolab.com',31087)
    db = connection['notecollab']
    db.authenticate('andrew','password')
    notes = db['notes']
    thisnote=notes.find({'course':n,'pid':n})
    noteobj=note(name=thisnote['name'],num=thisnote['pid'])
    c={}
    c.update(csrf(request))
    c['note']=noteobj
    return render_to_request('course/note.html',c)