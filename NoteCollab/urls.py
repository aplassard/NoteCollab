from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'NoteCollab.views.home', name='home'),
    url(r'^student/$', 'student.views.students'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/(?P<pk>\d+)/$','student.views.info'),
    url(r'^student/(?P<pk>\d+)/submit/$','student.views.submit'),
    url(r'^student/new/$','student.views.new'),
    url(r'^student/delete/$','student.views.delete'),
    url(r'^professor/$','professor.views.index'),
    url(r'^professor/new/$','professor.views.new'),
    url(r'^professor/(?P<pk>\d+)/$','professor.views.info'),
    url(r'^professor/submit','professor.views.submit'),
    url(r'^professor/(?P<pk>\d+)/submit/$','professor.views.submitinfo'),
    url(r'^course/$','course.views.index'),
    url(r'^course/submit/$','course.views.submit'),
    url(r'^course/new/$','course.views.new'),
    url(r'^course/(?P<pk>)/$','course.views.info'),
)
