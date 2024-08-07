from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        json_schema_extra = {
            'example': {
                'username': 'Jon07',
                'first_name': 'Smith',
                'last_name': 'Jon',
                'email': "jonsmith@gmail.com",
                'password': "JonSmith0707",
                'is_staff': False,
                'is_active': True,
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '939c73710faefc41b9f2ee3fdf5e3ab7b755d5583c41d285d6a954451de9242a'

