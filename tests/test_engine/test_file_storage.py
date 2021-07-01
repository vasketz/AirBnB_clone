#!/usr/bin/python3
"""
unittest for FileStorage
"""
import os.path
from datetime import datetime
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

dicct = {'my_number': 89,
         'name': 'Holberton',
         '__class__': 'BaseModel',
         'updated_at': '2017-09-28T21:05:54.119572',
         'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
         'created_at': '2017-09-28T21:05:54.119427'}


class TestFileStorage(unittest.TestCase):
    """
    Unittest for file_storage.py
    """
    storage = FileStorage()
    path = storage._FileStorage__file_path
    bm_instance = BaseModel(**dicct)
    storage.new(bm_instance)

    def test_storage_isinstance(self):
        """
        Tests if storage is an instance of FileStorage
        """
        self.assertIsInstance(TestFileStorage.storage, FileStorage)

    def test_file_json(self):
        """
        Tests for path existence
        """
        TestFileStorage.storage.save()
        self.assertTrue(os.path.exists(TestFileStorage.path))

    def test_reload(self):
        """
        Test for instances reloaded from path
        """
        key = dicct["__class__"] + "." + dicct["id"]
        with open(TestFileStorage.path, mode="r", encoding="utf-8") as f:
            reader = json.load(f)
        attributes = reader[key]
        self.assertEqual(dicct, attributes)
        self.assertIsInstance(TestFileStorage.storage.all()[key], BaseModel)

    def test_save_another_instance(self):
        """
        Tests for save another instance in path
        """
        bm2_instance = BaseModel()
        bm2_instance.save()
        key = type(bm2_instance).__name__ + "." + str(bm2_instance.id)
        with open(TestFileStorage.path, mode="r", encoding="utf-8") as f:
            reader = json.load(f)
        self.assertEqual(
            reader[key], TestFileStorage.storage.all()[key].to_dict())

if __name__ == '__main__':
    pass
