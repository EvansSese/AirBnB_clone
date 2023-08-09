#!/usr/bin/python3
"""This is the state class"""


from models.base_model import BaseModel


class State(BaseModel):
    """Represents state class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    self.name = ""
