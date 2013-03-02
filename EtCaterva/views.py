# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import request
from EtCaterva.models import Noticia, Proyecto, Usuario
from django.db.models import F

def home(request):
    return render_to_response("index.html", dict(aValue=False))

def contact(request):
    return render_to_response("contact.html", dict(aValue=False))

def project(request,projectid = 0):
    Proyecto.objects.filter(pk=projectid).update(visitas=F('visitas')+1)
    proyecto = Proyecto.objects.get(pk=projectid)
    return render_to_response("project.html", {'project' : proyecto})

def projects(request):
    return render_to_response("projects.html", {'project_list':Proyecto.objects.all(),'footer_project_list':Proyecto.objects.order_by('visitas')[:6]})

def user(request):
    return render_to_response("user.html", dict(aValue=False))

def users(request):
    return render_to_response("users.html", {'user_list':Usuario.objects.all(),'footer_user_list':Usuario.objects.order_by('baseUser__last_name')[:6]})
