#!/usr/bin/python3
import unittest
from models.base_model import BaseModel 
"""Unit tests for base model"""

class testBaseModelInit(unittest.TestCase):
    """Tests for BaseModel init function"""

    def setUp(self):
        """Sets up class for base init"""
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_args(self):
        a = BaseModel(1)
        self.assertNotEqual(a.id, 1)

    def test_kwargs_id(self):
        b = BaseModel(id="435-90312-cb4871")
        self.assertEqual(b.id, "435-90312-cb4871")

    def test_kwargs_casts_id(self):
        c = BaseModel(id=41571)
        self.assertEqual(type(c.id), int)

    def test_kwargs_created_at(self):
        """Tests that created_at is copied to object loaded
        from file"""
        pass

    def test_kwargs_updated_at(self):
        """Tests that updated_at is copied to loaded object"""
        pass

    def test_something(self):
        """idk"""
        pass

class testBaseModelMethods(unittest.TestCase):
    """Tests for BaseModel"""

    def setUp(self):
        self.base = BaseModel()

    def tearDown(self):
        del self.base

    def test_id(self):
        """Tests that uuids are unique"""
        base_x = BaseModel()
        self.assertNotEqual(self.base.id, base_x.id)

    def test_created_at_is_updated_at(self):
        """Tests that initial created_at and updated_at are equal"""
        base_a = BaseModel()
        self.assertNotEqual(base_a.created_at, base_a.updated_at)

    def test_str_class(self):
        """Tests str printing class name correctly"""
        pass

    def test_str_id(self):
        """Tests str printing id correctly"""
        pass

    def test_str_dict(self):
        """Tests str printing dict correctly"""
        pass

    def test_save_updates_updated_at(self):
        """Tests that save updates updated_at"""
        pass

    def test_save_no_file(self):
        """Tests that save works with no file"""
        pass

    def test_save_empty_file(self):
        """Tests that save works on an empty file"""
        pass

    def test_save_file_has_objects(self):
        """Tests that save works on a file that already contains
        other BaseModels"""
        pass

    def test_to_dict(self):
        """Tests that the to_dict method works"""
        pass

if __name__ == "__main__":
    testBaseModel()
