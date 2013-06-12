from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from ProjectManager.models import Project

urlpatterns = patterns('ProjectManager.views',
    url(r'^$', 'Home', name='home'),  #FIXME home
    url(r'^projects$', ListView.as_view(
            queryset=Project.objects.order_by('-priority'),
            context_object_name='project_list',
            template_name='ProjectManager/void.html')),   #FIXME 
    url(r'^project/(?P<pk>\d+)/detail$', DetailView.as_view(
            model=Project,
            template_name='ProjectManager/void.html')),    #FIXME
    url(r'^project/(?P<pk>\d+)/update$', UpdateView.as_view(
            model=Project,
            template_name='ProjectManager/void.html')),    #FIXME   
    url(r'^project/create/$', CreateView.as_view(
            model=Project,
            template_name='ProjectManager/void.html')),    #FIXME
    url(r'^project/(?P<pjid>\d+)/question','Question'),
    url(r'^project/(?P<pjid>\d+)/answer/(?P<qid>\d+)','Answer'),
    url(r'^project/(?P<pjid>\d+)/requestJoin/(?P<act>.)','RequestJoin'),
    url(r'^project/(?P<pjid>\d+)/answerJoin/(?P<act>.)','AnswerJoin'),
    url(r'^project/(?P<pjid>\d+)/vote/(?P<act>.)$', 'Vote'),
    #start project
               
)
