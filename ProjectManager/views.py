from django.http import HttpResponse
from django.shortcuts import render_to_response


def Home(request):
    return render_to_response("ProjectManager/index.html")

def Question(request,pjid):
    return HttpResponse("New Question for " + pjid)
    
def Answer(request,pjid,qid):
    return HttpResponse("New Answer for " + pjid)
    
def RequestJoin(request,pjid,act):
    return HttpResponse("Request for project " + pjid + " type: "+ act)
    
def AnswerJoin(request,pjid,act):
    return HttpResponse("Answer to join project: "+ pjid + act)
    
def Vote(request,pjid,act):
    return HttpResponse("vote "+ act + " for " + pjid)