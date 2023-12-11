#!/usr/bin/python3
"""our foundation project"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """base classe ."""

    def __init__(self, *args, **kwargs):
        """ our constructor
        """
        regul_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for w, u in kwargs.items():
                if w == "created_at" or w == "updated_at":
                    self.__dict__[w] = datetime.strptime(u, regul_form)
                else:
                    self.__dict__[w] = u
        else:
            models.storage.new(self)

    def save(self):
        """Update with the current datetime now"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Retourne the dictionary of the BaseModel instancee
        also representing
        the class name of the object
        """
        redictt = self.__dict__.copy()
        redictt["created_at"] = self.created_at.isoformat()
        redictt["updated_at"] = self.updated_at.isoformat()
        redictt["__class__"] = self.__class__.__name__
        return redictt

    def __str__(self):
        """print str and rep representation of the BaseModel instance."""
        myClassname = self.__class__.__name__
        return "[{}] ({}) {}".format(myClassname, self.id, self.__dict__)