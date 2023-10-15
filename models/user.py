#!/usr/bin/python3
""" User class Module. """


from models.base_model import BaseModel


class User(BaseModel):
    """ userclass representation

        args:
            email (str): email of the user
            password (str): password of the user
            first_name (str): first name of the user
            last_name (str): last name of the user
 """

    email = ""
    password = ""
    first = ""
    last_name = ""
