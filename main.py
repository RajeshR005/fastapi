from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

from typing import Optional

app = FastAPI()

#request get method url:"/" which hits the first match of the url then check for the next even if the order is up or down. 
class post(BaseModel):
    title: str
    content:str
    published:bool=True
    rating:Optional[int]=None

@app.get("/")
async def root():
    return {"message": "Hello World is good to go"}

@app.get("/login/posts")
def user_login():
    return{"Post1": "This is my first post"}

@app.post("/login/createpost")
def create_post(new_post:post):
    print(new_post.published)
    print(new_post.model_dump())
    return{"DAta":"Data received"}