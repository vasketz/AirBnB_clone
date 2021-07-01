#!/usr/bin/python3
"""
unittest for FileStorage
"""
import unittest
import json
from models.base_model import BaseModel
dicct = {'my_number': 89, 
         'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 
         'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 
         'name': 'Holberton', 
         'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}

class TestFileStorage(unittest.TestCase):
    """
    Unittest for file_storage.py
    """
    storage = FileStorage()
    path = storage._FileStorage__file_path
    bm_instance = BaseModel(**my_dict)
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
        key = my_dict["__class__"] + "." + my_dict["id"]
        with open(TestFileStorage.path, mode="r", encoding="utf-8") as f:
            reader = json.load(f)
        attributes = reader[key]
        self.assertEqual(my_dict, attributes)
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
