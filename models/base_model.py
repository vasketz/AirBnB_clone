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
        new_dic = {'update_at': self.update_at.isoformat(),
                   'create_at': self.create_at.isoformat(),
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

