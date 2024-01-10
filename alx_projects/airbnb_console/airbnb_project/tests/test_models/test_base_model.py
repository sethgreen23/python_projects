#!/usr/bin/env python3
"""Unittest for the BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test class for BaseModel class
    """

    def setUp(self):
        """setUp method for base_model test
        """
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """tearDown method for base_model test
        """
        del self.b1
        del self.b2

    def test_id(self):
        """Testing the uuid"""
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertIsInstance(self.b1, BaseModel)
        self.assertIsInstance(self.b1.id, str)

    def test_created_at(self):
        """Testing created_at"""
        self.assertTrue(hasattr(self.b1, "created_at"))
        self.assertIsInstance(self.b1.created_at, datetime)

    def test_updated_at(self):
        """Testing updated_at"""

        self.assertTrue(hasattr(self.b1, "updated_at"))
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_created_at_updated_at(self):
        """Testing dates"""
        self.assertNotEqual(self.b1.created_at, self.b2.created_at)
        self.assertNotEqual(self.b1.updated_at, self.b2.updated_at)

    def test_save(self):
        """Testing save"""
        self.b1.save()
        self.assertIsInstance(self.b1.updated_at, datetime)

    def test_to_dict(self):
        """Testing to_dict"""
        d = self.b1.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertIsInstance(d["created_at"], str)
        self.assertIsInstance(d["updated_at"], str)

    def test_str(self):
        """Testing str"""
        str_rep = str(self.b1)
        self.assertIn("BaseModel", str_rep)
        self.assertIn(self.b1.id, str_rep)
        # order preserving
        self.assertIn(str(self.b1.__dict__), str_rep)

    def test_init_from_dict(self):
        """
        Testing the creation of instance from a dictionary
        """
        self.b1.name = "My_First_Model"
        self.b1.my_number = 89
        dict_json = self.b1.to_dict()
        b1_clone = BaseModel(**dict_json)
        self.assertTrue(hasattr(b1_clone, "id"))
        self.assertTrue(hasattr(b1_clone, "created_at"))
        self.assertTrue(hasattr(b1_clone, "updated_at"))
        self.assertTrue(hasattr(b1_clone, "name"))
        self.assertTrue(hasattr(b1_clone, "my_number"))
        self.assertEqual(self.b1.id, b1_clone.id)
        self.assertEqual(self.b1.created_at, b1_clone.created_at)
        self.assertEqual(self.b1.updated_at, b1_clone.updated_at)
        self.assertEqual(self.b1.name, b1_clone.name)
        self.assertEqual(self.b1.my_number, b1_clone.my_number)
        self.assertEqual(str(self.b1.to_dict()), str(b1_clone.to_dict()))
        self.assertIsInstance(b1_clone, BaseModel)

    def test_save(self):
        """Test save() method from FileStorage Class in BaseModel class"""
        update_1 = self.b1.updated_at
        self.b1.save()
        update_2 = self.b1.updated_at
        self.assertNotEqual(update_1, update_2)


if __name__ == "__main__":
    unittest.main()
