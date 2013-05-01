from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from ProjectManager.models import Project

urlpatterns = patterns('ProjectManager.views',
    #url(r'^$', 'home', name='home'),  #FIXME home
    '''url(r'^projects$', ListView.as_view(
            queryset=Project.objects.order_by('-priority'),
            context_object_name='project_list',
            template_name='void.html')),   #FIXME 
    url(r'^project/(?P<pk>\d+)/detail$', DetailView.as_view(
            model=Project,
            template_name='void.html')),    #FIXME
    url(r'^project/(?P<pk>\d+)/update$', UpdateView.as_view(
            model=Project,
            template_name='void.html')),    #FIXME   
    url(r'^project/create/$', CreateView.as_view(
            model=Project,
            template_name='void.html')),    #FIXME
    #url(r'^project/(?P<pk>\d+)/vote/\d/$', 'vote'),    #FIXME'''
    #Ask, Answer, comment, requestParticipation, approve/decline request, start project
               
)
