from django.db import models

# Create your models here.
from EtCaterva.models import Usuario
from datetime import timedelta
import datetime
from django.utils.translation import ugettext_lazy as _

VOTE_TYPE = (
        ("+","+"),
        ("-","-"), 
)

REQUEST_TYPE = (
        ("1","participant"),
        ("2","owner"), 
)

class Strength(models.Model):
    text = models.CharField(_("strength"),max_length=50)
    def __unicode__(self):
        return self.text
    
    
class Weakness(models.Model):
    text = models.CharField(_("weakness"),max_length=50)    
    def __unicode__(self):
        return self.text    

class Project(models.Model):
    """Represents a project to be evaluated."""
    title = models.CharField(_("title"),max_length=50)
    priority = models.DecimalField(_("priority"),max_digits = 3, decimal_places=2, blank=True)
    date_created = models.DateField(_("creation date"), default=datetime.date.today)
    date_start = models.DateField(_("start date"), default=(datetime.date.today() + timedelta(days=30)))

    owners = models.ManyToManyField(Usuario,related_name="owner_of")
    participants = models.ManyToManyField(Usuario,related_name="participate_in")
    votes = models.ManyToManyField(Usuario,related_name="votes",through="Vote")
    requests = models.ManyToManyField(Usuario,related_name="request_access_to",through="JoinRequest")
    strengths = models.ManyToManyField(Strength)
    weaknesses = models.ManyToManyField(Weakness)
    questions = models.ManyToManyField(Usuario,related_name="questioned_at",through="Question")
    #link to Comments
    
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(_("comment"),max_length=50)
    project = models.ForeignKey(Project)
    def __unicode__(self):
        return self.text    

class Question(models.Model):
    text = models.CharField(_("question"),max_length=2000)
    project = models.ForeignKey(Project)
    user = models.ForeignKey(Usuario)
    def __unicode__(self):
        return "[Q:"+self.user+"->"+self.project+"]:"+self.text    
    
class Answer(models.Model):
    text = models.CharField(_("answer"),max_length=2000)
    question = models.OneToOneField(Question)
    user = models.ForeignKey(Usuario)
    def __unicode__(self):
        return "[A:"+self.user+"->"+self.question.project+"]:"+self.text     

class Vote(models.Model):
    type = models.CharField(_("type"),max_length=5,choices = VOTE_TYPE)
    project = models.ForeignKey(Project)
    user = models.ForeignKey(Usuario)
    def __unicode__(self):
        return "["+self.user+"->"+self.project+"]:"+self.type     
    
    
class JoinRequest(models.Model):
    date = models.DateField(_("request date"), default=datetime.date.today)
    type = models.CharField(_("type"),max_length=5,choices = REQUEST_TYPE)
    project = models.ForeignKey(Project)
    user = models.ForeignKey(Usuario)
    def __unicode__(self):
        return "["+self.user+"->"+self.project+"]:"+self.type     
    
class Log(models.Model):
    date = models.DateTimeField(_("log time"), default=datetime.datetime.now())
    user = models.ForeignKey(Usuario)
    action = models.CharField(_("content"),max_length=2000)
    def __unicode__(self):
        return "["+self.user+"->"+self.date+"]:"+self.action     
