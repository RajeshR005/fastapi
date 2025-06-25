from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

def password(password: str):
    hash_pass=pwd_context.hash(password)
    return hash_pass


def verify(plainpassword,hashpassword):
    return pwd_context.verify(plainpassword,hashpassword)