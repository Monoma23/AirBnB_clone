#!/usr/bin/python3
"""Definess the City classs"""
from models.base_model import BaseModel


class City(BaseModel):
    """representt city

    Attributess:
        state_id (str): The state id
        name (str): name of city
    """

    state_id = ""
    name = ""
