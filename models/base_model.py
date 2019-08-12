#!/usr/bin/python3
"""This module contains the Base class for
all classes in the Holberton BnB Project
"""

import datetime
import models
import uuid


class BaseModel():
    """Base class for Holberton BnB project
    """

    def __init__(self, *args, **kwargs):
        """Initializes the Base Model
        Args:
            args: args
            kwargs: Dictionary of object attributes
        """
        if len(kwargs) > 0:
            self.init_with_kwargs(**kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def init_with_kwargs(self, **kwargs):
        """init with a dictionary"""
        for (k, v) in kwargs.items():
            if k in ('created_at', 'updated_at'):
                self.__dict__[k] = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.__dict__[k] = v

    def __del__(self):
        """Deletes object"""
        del(self)

    def __str__(self):
        """Returns string repr of obj"""
        obj_str = ''
        obj_str += '[{}] '.format(self.__class__.__name__)
        obj_str += '({}) '.format(self.id)
        obj_str += '{}'.format(self.__dict__)
        return obj_str

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts obj to dict
        Return:
            Dict of all obj attributes
        """
        tmp = self.__dict__.copy()
        tmp['__class__'] = self.__class__.__name__
        tmp['created_at'] = self.created_at.isoformat()
        tmp['updated_at'] = self.updated_at.isoformat()
        return tmp
