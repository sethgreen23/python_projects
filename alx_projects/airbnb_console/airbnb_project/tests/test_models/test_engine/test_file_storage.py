#!/usr/bin/python3
"""Unittest for FileStorage Class"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os


class TestFileStorageClass(unittest.TestCase):
    """Test cases for Class FileStorage"""

    def setUp(self):
        """setUp method"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.f1 = FileStorage()
        # self.f2 = FileStorage()

    def tearDown(self):
        del self.b1
        del self.b2
        del self.f1
        # del self.f2
        filename = "file.json"
        try:  # Delete the file
            os.remove(filename)
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test attributes for class FileStorage"""
        FileStorage._FileStorage__objects = {}
        filename = "file.json"
        try:  # Delete the file
            os.remove(filename)
        except FileNotFoundError:
            pass
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_all_empty(self):
        """Tests all() instance method when __objects is empty"""
        result = self.f1.all()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        # self.assertEqual(len(result), 1)

    def test_all_none_empty(self):
        """Tests all() instance method"""
        self.f1.new(self.b1)
        result = self.f1.all()
        self.assertIsInstance(result, dict)
        self.assertNotEqual(result, {})
        self.assertIs(result, self.f1._FileStorage__objects)

    def test_new(self):
        """Tests new() instance method"""
        self.f1.new(self.b1)
        obj = self.f1.all()
        self.assertIsNotNone(obj)

    # def test_save(self):
    #     """Tests save() instance method"""
    #     self.b1.name = "My_First_Model"
    #     self.b1.my_number = 89
    #     self.b1.save()
    #     self.f1.reload()
    #     obj = self.f1.all()
    #     print("\n",obj)

    # def test_reload_nofile(self):
    #     """Tests reload() instance method"""
    #     filename = "file.json"
    #     try:# Delete the file
    #         os.remove(filename)
    #     except FileNotFoundError:
    #         pass
    #     result = self.f1.all()
    #     print("STORAGE\n{}\n".format(self.f1))
    #     self.assertIsNotNone(result)
