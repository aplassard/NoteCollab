from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NoteCollab.views.home', name='home'),
    # url(r'^NoteCollab/', include('NoteCollab.foo.urls')),
	url(r'^student/', 'student.views.students'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
