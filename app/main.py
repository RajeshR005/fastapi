from fastapi import FastAPI
import models
from models import engine
from routers import posts,user,login




models.Base.metadata.create_all(engine)

app = FastAPI()



@app.get("/")
def root():
    return {"message": "Hello"}


app.include_router(posts.router,prefix="/posts",tags=['Posts'])
app.include_router(user.router,prefix='/users',tags=['Users'])
app.include_router(login.router)