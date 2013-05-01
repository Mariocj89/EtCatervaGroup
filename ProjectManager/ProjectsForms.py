'''
Created on 30/04/2013

@author: Mario
'''

from django import forms
from django.forms import Form
from ProjectManager.models import *

class ProjectForm(Form):
    class Meta:
        model = Project
        fields = ('title', 'priority', 'date_created', 'date_start')

