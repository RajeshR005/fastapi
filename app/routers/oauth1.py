from jose import JWTError,jwt
from datetime import datetime,timedelta,timezone
import schemas
from fastapi import Depends,status,HTTPException
from fastapi.security.oauth2 import OAuth2PasswordBearer

oauthschemea=OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY="f302b7453d52228bee662c3c2e29cceb1adfa65eccab587a50f97424934be1a9"

ALGORITHM="HS256"

TOKEN_EXPIRATION_TIME=30

def create_access_token(data: dict):
    encode_data=data.copy()
    encode_data["exp"]=datetime.now(timezone.utc)+ timedelta(minutes=TOKEN_EXPIRATION_TIME)


    token=jwt.encode(encode_data,SECRET_KEY,algorithm=ALGORITHM)

    return token

def verify_access_token(token:str,login_exception):
    payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    
    try:
        user_id=payload.get("user_id")
        if user_id is None:
            raise login_exception
        id:int=user_id
        re_token=schemas.Tokendata(id=id)
    except JWTError:
        raise login_exception
    return re_token

def check_access_token(token:str=Depends(oauthschemea)):
    login_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials",headers={"WWW-Authenticate":"Bearer"})
    return verify_access_token(token,login_exception)



    

