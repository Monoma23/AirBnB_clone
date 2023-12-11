#!/usr/bin/python3
"""class User iinheriting from BaseModel mum
"""
from models.base_model import BaseModel


class User(BaseModel):
    """our class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""