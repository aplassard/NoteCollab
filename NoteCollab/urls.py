from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'NoteCollab.views.home', name='home'),
    url(r'^student/$', 'student.views.students'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/(?P<pk>\d+)/$','student.views.info'),
    url(r'^student/(?P<pk>\d+)/submit/$','student.views.submit'),
    url(r'^student/new/$','student.views.new'),
    url(r'^student/delete/$','student.views.delete'),
)
