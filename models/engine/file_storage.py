#!/usr/bin/python3
"""
Now we can recreate a BaseModel from another one 
by using a dictionary representation:
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """
    class storage to process the data
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dicctionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj clas name>.id
        """
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dicc = {}
        for key, value in self.__objects.items():
            dicc[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(dicc, file, indent=4)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file(__file_path)
        exists: otherwise, do nothing. if the file doesn't exist,
        no exception should be raised)
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                j_json = json.load(file)
                for key, value in j_json.items():
                    self.__objects[key] = BaseModel(**value)
        except:
            pass
