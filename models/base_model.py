#!/usr/bin/python3
"""Defines BaseModel class hihi"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Representss BaseModel of the HBnB project good"""

    def __init__(self, *args, **kwargs):
        """Initializezz new BaseModell.

        Argss:
            *args (any): Unused
            **kwargs (dict): Key/value pairs attribute
        """
        My_ytform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = (str(uuid4()))
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for z, r in kwargs.items():
                if z == "created_at" or z == "updated_at":
                    self.__dict__[z] = datetime.strptime(r, My_ytform)
                else:
                    self.__dict__[z] = r
        else:
            models.storage.new(self)

    def save(self):
        """Updateeze updated_at with currentt datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returnbb the dictionaryy of BaseModelll instance

        Includess the key/value pair __class__ representinnng
        the class name the objecttt
        """
        My_rdict = self.__dict__.copy()
        My_rdict["created_at"] = self.created_at.isoformat()
        My_rdict["updated_at"] = self.updated_at.isoformat()
        My_rdict["__class__"] = self.__class__.__name__
        return My_rdict

    def __str__(self):
        """Returnnn the print/str representation of BaseModel instancce"""
        My_clname = self.__class__.__name__
        return "[{}] ({}) {}".format(My_clname, self.id, self.__dict__)
