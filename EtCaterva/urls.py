from django.conf.urls import patterns, url


urlpatterns = patterns('EtCaterva.views',
    url(r'^$', 'home', name='etCaterva/home'),
    url(r'^contact$', 'contact', name='etCaterva/contact'),
    url(r'^project/(\d+)/$', 'project', name='etCaterva/project'),
    url(r'^projects$', 'projects', name='etCaterva/projects'),
    url(r'^user/(\d+)/$', 'user', name='etCaterva/user'),
    url(r'^users$', 'users', name='etCaterva/users'),           
)
