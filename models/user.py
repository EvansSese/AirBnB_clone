#!/usr/bin/python3
"""This is the user information class"""


from models.base_model import BaseModel


class User(BaseModel):
    """Represents user class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        email = ""
        password = ""
        first_name = ""
        last_name = ""
