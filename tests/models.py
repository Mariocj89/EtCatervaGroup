"""Tests for the models module.
"""

import unittest
from ProjectManager.models import Project
from datetime import timedelta

class TestModel(unittest.TestCase):
    def setUp(self):
        self.targetProject = Project()
    
    def tearDown(self):
        pass
    
    def test_initialized_project(self):
        self.assertTrue(self.targetProject.title != None)
        self.assertTrue(self.targetProject.priority == None)
        self.assertTrue((self.targetProject.date_start - self.targetProject.date_start) != timedelta(days=30))
    
if __name__ == '__main__':
    unittest.main()    
