#!/usr/bin/python3
"""Definesss thee FileStoragee class."""
import json
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """hadless seriaizationn and deserializationn of BaseModel instance.


    Attributess:
        __file_path (str):  name of file to save objects to
        __objects (dict): dictionary of instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returthe dicrsy __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set __objects obj key <obj_class_name>.id"""
        My_yocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(My_yocname, obj.id)] = obj

    def save(self):
        """Serialize __objectthe JSON file __file_path"""
        My_yodict = FileStorage.__objects
        yobjdict = {obj: My_yodict[obj].to_dict() for obj in My_yodict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(yobjdict, f)

    def reload(self):
        """deserialize JSe_path to __objects, if exists."""
        try:
            with open(FileStorage.__file_path) as f:
                yobjdict = json.load(f)
                for k in yobjdict.values():
                    cls_name = k["__class__"]
                    del k["__class__"]
                    self.new(eval(cls_name)(**k))
        except FileNotFoundError:
            return
