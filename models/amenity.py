#!/usr/bin/python3
"""This module contains the Amenity class for
which inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for Holberton BnB project
    Args:
        BaseModel: Inherits from BaseModel class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Amenity obj
        Args:
            args: args
            kwargs: Dictionary of object attributes
        """
        super().__init__(self, *args, **kwargs)




