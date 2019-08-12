#!/usr/bin/python3
"""This module contains the FileStorage class
which serializes/deserializes dictionaries/JSON files
"""

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os


class FileStorage():
    """convert between dictionary string representations of
    objects and JSON files
    Attributes
        file_path: json file to store json formatted objs in
        objects: Dict of objs by [class].[id]
    """
    __file_path = str(os.getcwd()) + "/file.json"      # path to the JSON file
    __objects = {}        # stores objects by [class].[id]

    def __init__(self):
        """Initializes file storage class"""
        self.__class__.__objects = {}

    def all(self):
        """Returns list of all objects in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets a new object's key and value in __objects"""
        tmp_dict = obj.to_dict()
        obj_key = tmp_dict['__class__'] + '.' + str(tmp_dict['id'])
        self.__objects[obj_key] = obj

    def save(self):
        """Saves objects to file"""
        with open(FileStorage.__file_path, mode="w") as fp:
            json.dump({k:v.to_dict() for k, v in FileStorage.__objects.items()}, fp)

    def reload(self):
        """Reloads file from disk"""
        try:
            with open(FileStorage.__file_path) as fp:
                data = json.load(fp)
        except FileNotFoundError:
            return
        tmp = {}
        for k, v in data.items():
            tmp[k] = eval(k.split(".")[0] + '(**v)')
            FileStorage.__objects = tmp

    @property
    def objects(self):
        """objects getter"""
        return self.__class__.__objects

    @objects.setter
    def objects(self):
        """objects getter"""
        tmp = {}
        self.__class__.__objects = tmp
