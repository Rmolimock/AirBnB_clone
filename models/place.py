#!/usr/bin/python3
"""This module contains the Place class for
which inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """State class for Holberton BnB project
    Args:
        BaseModel: Inherits from BaseModel class
    """

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
        """Initializes the Place obj
        Args:
            args: args
            kwargs: Dictionary of object attributes
        """
        super().__init__(self, *args, **kwargs)
