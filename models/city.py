#!/usr/bin/python3
''' This module contains one class, City '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' This class defines the City object '''
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initialize a city with BaseModel's atts/methods '''
        super().__init__(self, *args, **kwargs)
