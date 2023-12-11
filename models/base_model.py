#!/usr/bin/python3
""" this is the base class of the project"""


import models
from datetime import datetime
import uuid

class BaseModel:
	""" the base class """
	def __init__(self, *args, **kwargs):
		"""our constructor"""
		if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at",
                          None) and isinstance(self.created_at, str):
                self.created_at = datetime.strptime(kwargs["created_at"],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at",
                          None) and isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.updated_at = datetime.utcnow()
            if kwargs["id"] is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()
	def __str__(self):
		"""this is string representation of an objectt"""
		return '[{}] ({}) {}'.format(self.__class__.__name__,
                                self.id,
                                elf.__dict__)

    def save(self):
        """updating public instance attribute
        updated_at with actual date timee"""
        if self.updated_at is not datetime.now():
            self.updated_at = datetime.now()
        else:
            models.storage.new(self.to_dict())
        models.storage.save()

    def to_dict(self):
        """returns dict with all keys/values
        of __dict__ of instancec"""
        mon_dictionaire = {
            "__class__": self.__class__.__name__
        }

        mon_dictionaire.update(self.__dict__)

        if "created_at" in mon_dictionaire:
            mon_dictionaire["created_at"] = self.created_at.isoformat()
        if "updated_at" in mon_dictionaire:
            mon_dictionaire["updated_at"] = self.updated_at.isoformat()
        return mon_dictionaire