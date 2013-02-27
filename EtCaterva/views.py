# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import request

def home(request):
    return render_to_response("index.html", dict(aValue=False))

def contact(request):
    return render_to_response("contact.html", dict(aValue=False))

def login(request):
    return render_to_response("login.html", dict(aValue=False))

def project(request):
    return render_to_response("project.html", dict(aValue=False))

def projects(request):
    return render_to_response("projects.html", dict(aValue=False))

def user(request):
    return render_to_response("user.html", dict(aValue=False))

def users(request):
    return render_to_response("users.html", dict(aValue=False))
