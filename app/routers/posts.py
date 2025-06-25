from typing import List
from fastapi import Depends,HTTPException,Response,status,APIRouter
from database import get_db
from sqlalchemy.orm import Session
import models
import schemas
from routers.oauth1 import check_access_token

router=APIRouter()





#---------------------------------Read----------------------------------------------------
#Get specific posts
@router.get('/getpost/{id}',response_model=schemas.get_post_id)
def get_post(id:int,db:Session=Depends(get_db)):
    posts=db.query(models.Post).filter(models.Post.id==id).first()
    if posts:
        return posts
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Post with {id} not Exists in the Database")
     


#Get all post
@router.get('/getpost/',response_model=List[schemas.get_post_id])
def getall_post(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There is no post at the moment")
    else:
        return posts
#---------------------------------Insert-----------------------------------------------------
#Insert your post
@router.post('/createpost',status_code=status.HTTP_202_ACCEPTED)
def create_post(post:schemas.new_post,db:Session=Depends(get_db),user_id:int=Depends(check_access_token)):
    print(user_id)
    create_new=models.Post(**post.model_dump())
    exist_post=db.query(models.Post).filter(models.Post.title==post.title).first()
    if exist_post:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"The Post with Title: {post.title} Already Exists in the Database")
    else:
        db.add(create_new)
        db.commit()
        db.refresh(create_new)
        print(f"Title: {create_new.title} | Content: {create_new.content}")
        return create_new




#-----------------------------------Updated----------------------------------------------------
#Update your post whole
@router.put('/updateall/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_all(id:int,post:schemas.new_post,db:Session=Depends(get_db)):
    update_all_data=db.query(models.Post).filter(models.Post.id==id)
    if update_all_data.first() is not None:
        update_all_data.update(post.model_dump(),synchronize_session=False)
        db.commit()
        return{"Message":f"The Post with {id} Updated Successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Post with {id} you are looking for doesn't exist ")

#update specific fields
@router.patch('/update_one/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateone(id:int,post:schemas.update_one,db:Session=Depends(get_db)):
    specific_update=db.query(models.Post).filter(models.Post.id==id)
    if specific_update.first() is not None:
        specific_update.update(post.model_dump(exclude_unset=True),synchronize_session=False)
        db.commit()
        return{"Message":f"The Post with ID: {id} Updated Successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The post with ID: {id} not exists")
    
#-------------------------------------Delete--------------------------------------------------------
@router.delete('/deletepost/{id}',status_code=status.HTTP_202_ACCEPTED)
def delete_post(id:int,db:Session=Depends(get_db)):
    del_post=db.query(models.Post).filter(models.Post.id==id).first()
    if del_post is not None:
        db.delete(del_post)
        db.commit()
        return{"message":f"The post with ID: {id} Deleted Successfully"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The Post with ID: {id} is not Exist in the Database") 
    