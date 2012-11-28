from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'NoteCollab.views.home', name='home'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'submit/','NoteCollab.views.submit'),
    url(r'signup/','NoteCollab.views.newsignup'),
)
