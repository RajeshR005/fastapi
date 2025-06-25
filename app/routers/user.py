from fastapi import Depends,HTTPException,status,APIRouter
from sqlalchemy import func
from database import get_db
from sqlalchemy.orm import Session
import models
import schemas
from utils import password

router=APIRouter()


#--------------------------------------User Registration-------------------------------------------------
#--------------------------------------------------------------------------------------------------------
@router.post('/Registration/',status_code=status.HTTP_201_CREATED)
def register(reg:schemas.Registration,db:Session=Depends(get_db)):
    
    exist=db.query(models.User).filter(models.User.email==reg.email).first()
    if exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="The User Data Already Exists in the Database")
    else:
        hash_pass=password(reg.password)
        pass_data=reg.model_dump()
        pass_data['password']=hash_pass
        new_user=models.User(**pass_data)
        db.add(new_user)
        db.commit()
        return("Registration Successful")
        
#-----------------------------------------Get User Data-------------------------------------------------------
@router.get('/users/{name}',response_model=schemas.Userdata)
def user_data(name:str,db:Session=Depends(get_db)):
    get_data=db.query(models.User).filter(func.lower(models.User.name)==name.lower()).first()
    if get_data:
        return get_data
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The User with ID: {id} is not found on the Database")
