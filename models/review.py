#!/usr/bin/python3
"""This is the revie class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents review class"""
    place_id = ""
    user_id = ""
    text = ""
