from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EtCatervaGroup.views.home', name='home'),
    # url(r'^EtCatervaGroup/', include('EtCatervaGroup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls),name='admin'),
    
    url(r'', include('EtCaterva.urls')),

)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
