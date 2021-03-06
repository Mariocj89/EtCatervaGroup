from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from django.core.files.storage import FileSystemStorage
from EtCatervaGroup.settings import MEDIA_ROOT

mfs = FileSystemStorage(MEDIA_ROOT)

# Create your models here.
class KeyWord(models.Model):
    """Key words para asociar por categoria. Ej:C++"""
    word = models.CharField(max_length=100)
    def __unicode__(self):
        return self.word
    
class Slider(models.Model):
    image = models.ImageField(storage=mfs,upload_to='sliders')
    titulo = models.CharField(max_length=100)
    def __unicode__(self):
        return self.titulo    

class Usuario(models.Model):
    """Usuario personalizado para EtCaterva"""
    baseUser = models.OneToOneField(User)
    birthDate = models.DateField()
    profilePicture = models.ImageField(storage=mfs,upload_to='userAvatar')
    description = models.TextField()
    keyWords = models.ManyToManyField(KeyWord,blank=True, null=True)
    
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    stackOverflow = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return self.baseUser.username
    
class Noticia(models.Model):
    """Noticia en la Web"""
    usuario = models.ForeignKey(Usuario)
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
    image = models.ImageField(storage=mfs,upload_to='projectPic')
    file = models.FileField(storage=mfs,upload_to='projectFiles',blank=True, null=True)
    visitas = models.PositiveIntegerField(default=0)
    link = models.URLField(blank=True, null=True)
    usuarios = models.ManyToManyField('Usuario')
    keyWords = models.ManyToManyField(KeyWord)
    def __unicode__(self):
        return self.titulo
    
    
