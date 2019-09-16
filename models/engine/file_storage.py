#!/usr/bin/python3
''' This module contains one class, FileStorage '''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    ''' This class handles JSON [de]serialization '''
    __file_path = 'file.json'
    __objects = {}
    __allowed_classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

    @staticmethod
    def allowed_classes():
        ''' returns private attr of instantiable classes '''
        return FileStorage.__allowed_classes

    def file_path(self):
        ''' The path of the json file that's being reloaded '''
        return self.__file_path

    def all(self):
        ''' returns objects dict, much like getter '''
        return self.__objects

    def new(self, obj):
        ''' add new object to dict of all objects '''
        self.all()["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        ''' serialize dict of all objects '''
        list_of_dicts = [obj.to_dict() for (key, obj) in
                         self.all().items()]
        with open(FileStorage.__file_path, "w+", encoding="utf-8") as f:
            f.write(json.dumps(list_of_dicts))

    def reload(self):
        ''' instantiate objects from a json file '''
        try:
            with open(FileStorage.__file_path, "r") as f:
                list_of_dicts = FileStorage.from_json_string(f.read())
        except FileNotFoundError:
            list_of_dicts = []
        [FileStorage.allowed_classes()[each_dict['__class__']](**each_dict)
         for each_dict in list_of_dicts if each_dict['__class__'] in
         FileStorage.allowed_classes()]

    def from_json_string(json_string):
        '''convert json string into list of dictionaries representing
           an object's attributes
        '''
        return [] if json_string is None or json_string == "" else json.loads(json_string)
