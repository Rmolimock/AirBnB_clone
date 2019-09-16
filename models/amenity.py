#!/usr/bin/python3
''' This module contains one class, Amenity '''
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' This class defines amenity objects '''
    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initialize an amenity with BaseModel's atts/methods '''
        super().__init__(self, *args, **kwargs)




