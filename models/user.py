#!/usr/bin/python3
"""Define User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        email (str): the emaile of the user
        password (str): the password of the user
        first_name (str): the first naeme of the user
        last_name (str): the last namee of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
