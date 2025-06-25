from typing import Optional
from fastapi.params import Body
from fastapi import FastAPI
app=FastAPI()
from pydantic import BaseModel

class post(BaseModel):
    title:str
    content:str
    published: bool = True
    rating: Optional[int]=None

@app.get('/login')
def login(name):
    return name

@app.get('/{name}')
def root(name):
    return {"Hi" : name}



@app.get('/login/successful')
def login_sucess():
    return{"Hello User": "You have Sucessfully Logged In"}

@app.post('/login/successful/createpost')
def create_post(payload:dict=Body):
    print(payload)
    # return{"acknowledgement": "You have successfully created your post"}
    return(f" Title: {payload['title']} Content: {payload['content']}")

# @app.post('/login/successful/createpost')
# def create_post(post:post):
#     print(post.model_dump())
#     return{f"{post.title}"}
#     # return(f" Title: {payload['title']} Content: {payload['content']}")
   

