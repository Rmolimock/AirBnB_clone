#!/usr/bin/python3
"""This module contains the Review class for
which inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for Holberton BnB project
    Args:
        BaseModel: Inherits from BaseModel class
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the review obj
        Args:
            args: args
            kwargs: Dictionary of object attributes
        """
        super().__init__(self, *args, **kwargs)
