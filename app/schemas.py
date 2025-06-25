from pydantic import BaseModel,EmailStr
from typing import Optional

class new_post(BaseModel):
    title:str
    content:str
    Published:bool=True

class update_one(BaseModel):
    title:Optional[str]=None
    content:Optional[str]=None
    Published:Optional[bool]=None

class get_post_id(BaseModel):
    title:str
    content:str

    class Config:
        from_attributes=True

class Registration(BaseModel):
    name:str
    email:EmailStr
    password:str

class Userdata(BaseModel):
    id:int
    name:str
    email:EmailStr

    class Config:
        from_attributes=True



class Login_data(BaseModel):
    access_token:str
    token_type:str
    

class Tokendata(BaseModel):
    id:Optional[int]=None