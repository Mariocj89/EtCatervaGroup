from django.conf.urls import patterns, url


urlpatterns = patterns('EtCaterva.views',
    url(r'^$', 'home', name='home'),
    url(r'^contact$', 'contact', name='contact'),
    url(r'^login$', 'login', name='login'),
    url(r'^projects$', 'projects', name='projects'),
    url(r'^project$', 'project', name='project'),
    url(r'^user$', 'user', name='user'),
    url(r'^users$', 'users', name='users'),           
)
