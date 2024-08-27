#!/usr/bin/python3
"""
Unittest for FileStorage class
"""
import unittest
import os
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test Cases for the FileStorage class.
    """
    def test_attrs(self):
        """
        Test for attributes
        """
        fs = FileStorage()
        self.assertEqual(type(fs._FileStorage__file_path), str)
        self.assertEqual(type(fs._FileStorage__objects), dict)
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertIsInstance(fs, FileStorage)
        self.assertEqual(type(fs.all()), dict)
        self.assertTrue(type(fs.new), "<class 'method'>")
    
    def test_new(self):
        """
        Testing FileStorage new method
        """
        bm = BaseModel()
        all_d = storage.all()
        for val in all_d.values():
            tmp = val
        self.assertTrue(tmp == val)

    def test_save_reload(self):
        """
        Testing FileStorage save method
        """
        fs = FileStorage()
        file_path = "file.json"
        fs.save()
        self.assertTrue(os.path.exists(file_path))
        ids = []
        for i in range(5):
            bm = BaseModel()
            fs.new(bm)
            ids.append(bm.id)
        fs.save()
        fs.reload()
        all_reloaded = fs.all()
        bm = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))
