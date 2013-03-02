from django.conf.urls import patterns, url


urlpatterns = patterns('EtCaterva.views',
    url(r'^$', 'home', name='home'),
    url(r'^contact$', 'contact', name='contact'),
    url(r'^project/(\d+)/$', 'project', name='project'),
    url(r'^projects$', 'projects', name='projects'),
    url(r'^user/(\d+)/$', 'user', name='user'),
    url(r'^users$', 'users', name='users'),           
)
