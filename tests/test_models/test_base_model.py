#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test Cases for the BaseModel class.
    """
    def instance_creation(self):
        """
        Instance creation
        """
        my_model = BaseModel()
        self.assertEqual(str(type(
            my_model)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(issubclass(type(my_model), BaseModel))
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))
        self.assertTrue(hasattr(my_model, "id"))
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertTrue(bm1.id != bm2.id)

    def test_save(self):
        """
        Testing save method
        """
        bm = BaseModel()
        old_time = bm.updated_at
        bm.save()
        self.assertTrue(bm.created_at != bm.updated_at)
        self.assertTrue(old_time != bm.updated_at)
        self.assertTrue(type(bm.updated_at), "<class 'datetime.datetime'>")

    def test_to_dict(self):
        """
        Testing to_dict method
        """
        bm = BaseModel()
        d_json = bm.to_dict()
        self.assertTrue(type(d_json), "<class 'dict'>")
        self.assertTrue(type(d_json['id']), "<class 'str'>")
        self.assertTrue(type(d_json['created_at']), "<class 'str'>")
        self.assertTrue(d_json['__class__'], "BaseModel")

    def test_str(self):
        """
        Testing string representation of class
        """
        bm = BaseModel()
        s_bm = str(bm)
        self.assertTrue((s_bm.split(" ")[0]), "[BaseModel]")
        self.assertTrue(s_bm.split(" ")[1] == "({})".format(bm.id))

    def test_kwargs(self):
        """
        Testing **kwargs arguments
        for the constructor of a BaseModel
        """
        bm1 = BaseModel()
        bm2 = BaseModel(**bm1.to_dict())
        self.assertTrue(bm1.id == bm2.id)
