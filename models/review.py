#!/usr/bin/python3
"""Review class inheriting from BaseModel mum
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""
    place_id = ""
    user_id = ""
    text = ""