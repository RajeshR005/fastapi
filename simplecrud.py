from fastapi import FastAPI,Response,HTTPException,status
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

class updatepost(BaseModel):
    title:Optional[str]=None
    content:Optional[str]=None
    published:Optional[bool]=None
    rating:Optional[int]=None

    

#CRUD Based application 

my_posts1=[{'title':'Hello','content':'Hello world'},{'title':'Elon Musk','content':'Success of Elon Musk'}]

def find_post(title):
    for i in my_posts1:
        if i['title']==title:
            return i

def delete_post(title):
    for i,p in enumerate(my_posts1):
        if p['title']==title:
            del my_posts1[i]
            return("success")

def update_post(title):
    for index, p in enumerate(my_posts1):
        if p['title']==title:
            return index
           
            


@app.get("/")
async def root():
    return {"message": "Hello World is good to go"}
#--------------------Read--------------------------------
#get specific post
@app.get("/login/posts/{title}")
def specific_post(title):
    find_post(title)
    
    if not find_post(title):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Post with title : '{title}' is Not Exists")
        
    return{"Post Data": find_post(title)}
#get all post
@app.get("/login/posts/")
def get_allpost():
    return(my_posts1)    
#-------------------------Insert----------------------------------
#send post
@app.post("/login/posts",status_code=status.HTTP_201_CREATED)
def create_post(post:post):
    my_posts1.append(post.model_dump())
    print(post.model_dump())
    return{"Data":"Data received"}

#------------------------Update--------------------------------------
# #update Whole Post Details
@app.put('/login/update/posts/{title}',status_code=status.HTTP_202_ACCEPTED)
def updated_post(title,post:post):
    upd=update_post(title)
    if upd is not None:
        my_posts1[upd]=post.model_dump()
        return(f"The post with '{title}' Updated Successfully")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The post with '{title}' Not Exists")
# Update only specific fields of a post        
@app.patch('/login/update/posts/{title}',status_code=status.HTTP_202_ACCEPTED)
def updateone(title,post:updatepost):
    upd =update_post(title)
    if upd is not None:
        exist=my_posts1[upd]
        update_specific=post.model_dump(exclude_unset=True)
        exist.update(update_specific)
        return(f"The post with '{title}' Updated Successfully")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The post with '{title}' Not Exists")




#-------------------------Delete--------------------------------------
@app.delete('/login/delete/posts/{title}',status_code=status.HTTP_202_ACCEPTED)
def delete_post1(title):
    del_post=delete_post(title)
    if del_post=="success":
       return(f"The post '{title}' was Deleted Successfully")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Post your Look for with '{title}' Not Exists")


    


