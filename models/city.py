#!/usr/bin/python3
"""This module contains the City` class for
which inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class for Holberton BnB project
    Args:
        BaseModel: Inherits from BaseModel class
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the City obj
        Args:
            args: args
            kwargs: Dictionary of object attributes
        """
        super().__init__(self, *args, **kwargs)
