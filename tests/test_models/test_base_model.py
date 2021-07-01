#!/usr/bin/python
"""
Unitest base model
"""
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(TestCase):
    """
    Class test
    """ 
    def save(self):
        self.updated_at = datetime.utcnow()

    def test_id(self):
        object1 = BaseModel()
        object2 = BaseModel()
        object1.name = "prueba"
        self.assertEqual(object1.name, "prueba")
        self.assertNotEqual(object1.id, object2.id)

    def test_created(self):
        object1 = BaseModel()
        object2 = BaseModel()
        self.assertNotEqual(object1.created_at, object2.created_at)
        self.assertNotEqual(object1.updated_at, object2.updated_at)

    def test_base_model(self):
        """
        Testing a class BaseModel
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(issubclass(type(obj), BaseModel))
        self.assertIs(type(obj), BaseModel)

        obj.name = "Holberton"
        obj.my_number = 89
        self.assertEqual(obj.name, "Holberton")
        self.assertEqual(obj.my_number, 89)
        """
        at_class = {
            "id": str,
            "created_at": datetime
            "updated_at": datetime
            "name": str
            "my_number": int
        }
        """

    def test_none(self):
        """Check for instance in not null"""
        obj = BaseModel()
        self.assertIsNotNone(obj)

    def test_uuid(self):
        """Check ids in the created instances"""
        obj = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertNotEqual(obj.id, obj2.id)

    def test_created_at(self):
        """Check if the instance has created_at Atttibute"""
        obj = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(obj, "created_at")
        self.assertTrue(obj2, "created_at")

    def test_updated_at(self):
        """Check if the instance has created_at Atttibute"""
        obj = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(obj, "updated_at")
        self.assertTrue(obj2, "updated_at")

    def test_str_output(self):
        """Check the string of an created instance"""
        obj = BaseModel()
        output = "[{}] ({}) {}".format(
            obj.__class__.__name__, obj.id, obj.__dict__)
        self.assertEqual(str(obj), output)

    def test_to_dict(self):
        """Test the to_dict method from BaseModel"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(str(obj.id), obj_dict["id"])
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_save(self):
        """Test to check each update in the storage"""
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "updated_at"))
        obj.save()
        self.assertTrue(hasattr(obj, "updated_at"))
        dicct = {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                 'create_at': datetime(2017, 9, 28, 21, 5, 54, 119427),
                 'updated_at': datetime(2017, 9, 28, 21, 5, 54, 119572),
                 'name': 'obj'}
        obj2 = BaseModel(dicct)
        obj2.save()
        last_time = obj2.updated_at
        obj2.save()
        self.assertNotEqual(last_time, obj2.updated_at)

    def test_basemodel_from_dict(self):
        """test to check a new instance witk Kwargs"""
        my_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                   'created_at': '2017-09-28T21:03:54.052298',
                   '__class__': 'BaseModel', 'my_number': 89,
                   'updated_at': '2017-09-28T21:03:54.052302',
                   'name': 'Holberton'}
        obj = BaseModel(**my_dict)
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertEqual(obj.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.name, str)
        self.assertEqual(obj.name, 'Holberton')
        self.assertEqual(
            obj.created_at.isoformat(), '2017-09-28T21:03:54.052298')
        self.assertEqual(
            obj.updated_at.isoformat(), '2017-09-28T21:03:54.052302')
