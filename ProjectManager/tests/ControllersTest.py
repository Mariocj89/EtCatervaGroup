'''
Created on 04/05/2013

@author: Mario
'''
from ProjectManager.controllers import *

import random
from django.contrib.auth.models import User
import django.test


class TestProjectController(django.test.TestCase):
    def setUp(self):
        aPj = Project()
        aPj.title = "Test Project"
        aPj.priority = 5
        aPj.save()
        self.target = ProjectController(aPj.pk)
        self.users = []
        for i in range(20):
            aux =  User()
            aux.username = 'RandomUser' + str(i)
            aux.save()
            self.users.append(Usuario())
            self.users[i].baseUser = aux
            self.users[i].birthDate = '1989-05-01'
            self.users[i].save()
        
    def test_getProject(self):
        self.assertIsNotNone(self.target)
        self.assertIsNotNone(self.target.getProjectInstance())
        
    def test_wrong_pid(self):
        self.assertRaises(Project.DoesNotExist, lambda: ProjectController(555))
        
    def test_votes(self):
        i = 0;
        self.target.vote(self.users[i],'+');i+=1
        self.target.vote(self.users[i],'+');i+=1
        self.target.vote(self.users[i],'+');i+=1
        self.assertEqual(3, self.target.getVotes())
        
        #negative votes
        self.target.vote(self.users[i],'-');i+=1
        self.target.vote(self.users[i],'-');i+=1
        self.assertEqual(1, self.target.getVotes())
        
        #Same user votes twice
        self.target.vote(self.users[i],'+');
        self.target.vote(self.users[i],'+');
        self.assertEqual(2, self.target.getVotes())
        
        #user changes his vote
        self.target.vote(self.users[i],'-');
        self.assertEqual(0, self.target.getVotes())
