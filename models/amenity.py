#!/usr/bin/python3
"""This is the amenity class"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents amenity class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
