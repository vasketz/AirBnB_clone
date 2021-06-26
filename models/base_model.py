#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime

class BaseModel():
    """
    parent class BaseModel
    """

    def __init__(self, *args, **kwargs):
        """
        Contructor
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "update_at":
                    setattr(self, key, datetime.strptime(str(value), "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.update_at = datetime.now()

    def __str__(self):
        """Return string"""
        return str("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def to_dict(self):
        new_dic = {'update_at': self.update_at.isoformat(),
                   'create_at': self.created_at.isoformat(),
                   '__class__': self.__class__.__name__}
        return dict(self.__dict__, **new_dic)

    #name = self.__class__.__name__
    #new_dict = self.__dict__.copy()
    #if new_dict[create_at]:
    #   new_dict.update(__class__=name, creat_at=self.create_at.isoformat())
    #else:
    #   

    def save(self):
        self.update_at = datetime.now()

