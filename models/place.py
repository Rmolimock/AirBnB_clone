#!/usr/bin/python3
''' This module contains one class, User '''
from models.base_model import BaseModel


class Place(BaseModel):
    ''' This class defines the place object '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [""]

    def __init__(self, *args, **kwargs):
        ''' Initialize a place with BaseModel's atts/methods '''
        super().__init__(self, *args, **kwargs)
