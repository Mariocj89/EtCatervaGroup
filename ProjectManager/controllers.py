'''
Created on 04/05/2013

@author: Mario
'''

from ProjectManager.models import *

class ProjectController:
    '''
        Class to handle all project actions in a handy way
    '''
    
    def __init__(self,pId):
        try:
            self.project = Project.objects.get(pk=pId)
        except Project.DoesNotExist:
            raise Project.DoesNotExist

    def getProjectInstance(self):
        return self.project
    
    def getVotes(self):
        '''Return the number of votes (posit - negati)'''
        if self.project.votes.count() == 0:
            return 0
        return self.project.votes.filter(vote__typeV='+').count() - self.project.votes.filter(vote__typeV='-').count()
        
    def vote(self,uid,typeV):
        '''Votes a user for a the project'''
        try:
            toInsert = Vote.objects.get(user=uid,project = self.project)
        except Vote.DoesNotExist:
            toInsert = None 
        if toInsert == None:
            toInsert = Vote()
            toInsert.project = self.project
            toInsert.user = uid
        toInsert.typeV = typeV
        toInsert.save()
        