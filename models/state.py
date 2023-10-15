#!/usr/bin/python3
""" Modul State Class """


from models.base_model import BaseModel


class State(BaseModel):
    """
    State class representations

    args:
        name (str): name of the state
    """
    name = ""
