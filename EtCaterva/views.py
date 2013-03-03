# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import request
from EtCaterva.models import Noticia, Proyecto, Usuario, Slider
from django.db.models import F
from django.db.models import Sum
import datetime
import random
from django import forms
from django.core.mail import send_mail
from django.template.context import RequestContext

class ContactForm(forms.Form):
    correo = forms.EmailField()
    comentario = forms.CharField()
    recibir_copia = forms.BooleanField(required=False)


def home(request):
    noticias = Noticia.objects.order_by('fecha')[:15]
    proyectos = Proyecto.objects.order_by('fecha')[:9]
    ranNum = random.random() * (Usuario.objects.count())
    randomUser = Usuario.objects.all()[ranNum:ranNum+1]
    sliders = Slider.objects.all()[:7]
    return render_to_response("index.html", {'noticias' : noticias, 'proyectos': proyectos, 'randomUser' : randomUser, 'sliders':sliders})

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            subject = "Comenario en etcaterva"
            message = form.cleaned_data['comentario']
            sender = form.cleaned_data['correo']
            cc_myself = form.cleaned_data['recibir_copia']
            recipients = ['admin@etcaterva.com']
            if cc_myself:
                recipients.append(sender)       
            send_mail(subject, message, sender, recipients)     
            render_to_response("contact.html", {'sent': True})
    else:
        form = ContactForm() # An unbound form
    
    return render_to_response("contact.html", {'sent': False,'form': form}, context_instance=RequestContext(request))

def project(request,projectid = 0):
    Proyecto.objects.filter(pk=projectid).update(visitas=F('visitas')+1)
    proyecto = Proyecto.objects.get(pk=projectid)
    return render_to_response("project.html", {'project' : proyecto})

def projects(request):
    return render_to_response("projects.html", {'project_list':Proyecto.objects.all(),'footer_project_list':Proyecto.objects.order_by('visitas')[:6]})

def user(request,userid = 0):
    aUser = Usuario.objects.get(pk=userid)
    edad = datetime.date.today() - aUser.birthDate
    proyectos = Proyecto.objects.filter(usuarios=aUser.pk).order_by('fecha')
    proyectosV = Proyecto.objects.filter(usuarios=aUser.pk).order_by('visitas')
    noticias = Noticia.objects.filter(usuario=aUser.pk).order_by('fecha')
    pVisitas = Proyecto.objects.filter(usuarios=aUser.pk).aggregate(Sum('visitas'))['visitas__sum']*100 / Proyecto.objects.aggregate(Sum('visitas'))['visitas__sum']
    pProyectos = Proyecto.objects.filter(usuarios=aUser.pk).count()*100 / Proyecto.objects.count()
    return render_to_response("user.html", {'usuario' : aUser, 'proyectos':proyectos,'proyectosV':proyectosV,'noticias':noticias, 'edad' : edad.days/365, 'pVisitas' : pVisitas, 'pProyectos': pProyectos})

def users(request):
    return render_to_response("users.html", {'user_list':Usuario.objects.all(),'footer_user_list':Usuario.objects.order_by('baseUser__last_name')[:6]})
