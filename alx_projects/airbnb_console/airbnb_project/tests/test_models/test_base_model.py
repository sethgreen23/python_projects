#!/usr/bin/env python3
"""Unittest for the BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
	Test class for BaseModel class
    """       
    
    def test_uuid(self):
        """Testing the uuid"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertTrue(hasattr(b1, "id"))
        self.assertNotEqual(b1.id, b2.id)
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.id, str)
    
    def test_created_at(self):
        """Testing created_at"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertIsInstance(b1.created_at, datetime)
    
    def test_updated_at(self):
        """Testing updated_at"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertIsInstance(b1.updated_at, datetime)
    
    def test_created_at_updated_at(self):
        """Testing dates"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertNotEqual(b1.updated_at, b2.updated_at)
        
if __name__=="__main__":
    unittest.main()    
