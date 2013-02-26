from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.core.files.storage import FileSystemStorage

mfs = FileSystemStorage('E:/Mis Documentos/workspace/Django/EtCatervaGroup/EtCaterva/media')

# Create your models here.
class Usuario(models.Model):
    """Usuario personalizado para EtCaterva"""
    baseUser = models.OneToOneField(User)
    birthDate = models.DateField()
    profilePicture = models.ImageField(storage=mfs,upload_to='userAvatar',blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    stackOverflow = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return self.baseUser.username
    
class Noticia(models.Model):
    """Noticia en la Web"""
    usuario = models.ForeignKey(Usuario,unique=True)
    fecha = models.DateField(default=datetime.today())
    titulo = models.CharField(max_length=100)
    content = models.TextField()
    
    def __unicode__(self):
        return self.titulo
    
class Proyecto(models.Model):    
    """Proyecto en Et Caterva"""
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(default=datetime.today())
    image = models.ImageField(storage=mfs,upload_to='projectPic',blank=True, null=True)
    visitas = models.PositiveIntegerField(default=0)
    link = models.URLField(blank=True, null=True)
    usuarios = models.ManyToManyField('Usuario')
    def __unicode__(self):
        return self.titulo
    
    
    