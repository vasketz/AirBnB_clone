#!/usr/bin/python3
"""
module of engine storage
"""
import json


class FileStorage():
    """
    class storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dicctionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj clas name>.id
        """
        self.__objects = {"{}.{}".format(obj.__class__.__name__, obj.id): obj}
        return self.__objects.update()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file(__file_path)
        exists: otherwise, do nothing. if the file doesn't exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                json.load(file)
        except:
            pass
