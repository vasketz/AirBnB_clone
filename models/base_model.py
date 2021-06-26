#!/usr/bin/python3
# Defines all common attributes/methods for other classes
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    parent class BaseModel
    """
    id = str(uuid4())
    create_at = datetime.now()
    update_at = datetime.now()

    def __str__(self):
        """Return string"""
        return str("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def to_dict(self):
        new_dic = {'update_at':self.update_at, 'create_at':self.create_at, '__class__':self.__class__.__name__}
        return dict(self.__dict__, **new_dic)

    def save(self):
        self.update_at = datetime.now()
