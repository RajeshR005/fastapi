
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import TIMESTAMP, Column,String,Integer,Boolean,create_engine,text,func
Base =declarative_base()
db_url="mysql+pymysql://root:2741@localhost:3307/studentsfastapi"
engine=create_engine(db_url)
Session=sessionmaker(bind=engine)
session=Session()

class Post(Base):
    __tablename__="posts"

    id = Column(Integer,autoincrement=True,primary_key=True)
    title=Column(String(50),nullable=False)
    content=Column(String(255),nullable=False)
    Published=Column(Boolean,default=True)

class User(Base):
    __tablename__="users"
    
    id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String(50),nullable=False)
    email=Column(String(255),nullable=False)
    password=Column(String(255),nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),server_default=func.now())


