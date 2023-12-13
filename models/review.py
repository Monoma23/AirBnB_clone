#!/usr/bin/python3
"""definess deview classs"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represent reve

    Attributes:
        place_id (str): the Place id
        user_id (str): the User id
        text (str): the text of the revie
    """

    place_id = ""
    user_id = ""
    text = ""
