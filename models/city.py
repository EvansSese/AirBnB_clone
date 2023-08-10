#!/usr/bin/python3
"""This is the city class"""


from models.base_model import BaseModel


class City(BaseModel):
    """Represents the city class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
