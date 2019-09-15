#!/usr/bin/python3
'''This is the base model class for AirBnB'''
import uuid
from datetime import datetime
import models

now = datetime.utcnow


class BaseModel:
    ''' This class handles object permanence '''

    def __init__(self, *args, **kwargs):
        ''' create instance atts id, created_at, and updated_at '''
        if kwargs:
            # don't allow user to overwrite important atts like __class__ in kwgs
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at':
                    nowf = datetime.strptime(v,"%Y-%m-%dT%H:%M:%S.%f")
                    self.created_at = nowf
                elif k == 'updated_at':
                    nowf = datetime.strptime(v,"%Y-%m-%dT%H:%M:%S.%f")
                    self.updated_at = nowf
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = now()
            self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        ''' prints string representation of self '''
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, str(self.__dict__))

    def save(self):
        ''' save instance into storage and update updated_at '''
        self.updated_at = now()
        models.storage.save()

    def to_dict(self):
        ''' create dictionary representation of self '''
        new = self.__dict__.copy()
        new['updated_at'] = self.updated_at.isoformat()
        new['created_at'] = self.created_at.isoformat()
        new['__class__'] = self.__class__.__name__
        return new
