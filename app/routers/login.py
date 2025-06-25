from fastapi import APIRouter,Depends,HTTPException,status
import models,utils,schemas,database
from routers import oauth1
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


#Login user
router=APIRouter(tags=["User Authentication"])

@router.post('/login',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.Login_data)
def verify_user(login:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    validate_user=db.query(models.User).filter(models.User.email==login.username).first()
    if validate_user:
        if utils.verify(login.password,validate_user.password):
            token=oauth1.create_access_token({"user_id": validate_user.id})
            
            return {"access_token": token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")
    

