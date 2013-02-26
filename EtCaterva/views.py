# Create your views here.
from django.shortcuts import render_to_response
from django.core.context_processors import request


def home(request):
    return render_to_response("index.html", dict(aValue=False))
