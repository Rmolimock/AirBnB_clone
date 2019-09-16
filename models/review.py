#!/usr/bin/python3
''' This module contains one class, Review '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' This class defines the review object '''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        ''' Initialize a review with BaseModel's atts/methods '''
        super().__init__(self, *args, **kwargs)
