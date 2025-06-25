from sqlalchemy import create_engine,Column,Integer,String,Boolean,DateTime,text,Float,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker
from datetime import datetime,time,date,timedelta

db_url="mysql+pymysql://root:2741@localhost:3307/e_commerce_fastapi"
Base=declarative_base()
engine=create_engine(db_url)
Session=sessionmaker(bind=engine)
session=Session()


class User(Base):
    __tablename__="users"

    id=Column(Integer,autoincrement=True,primary_key=True)
    name=Column(String(50),nullable=False)
    email=Column(String(50),nullable=False)
    password=Column(String(255),nullable=False)
    phone=Column(String(50),nullable=False)
    address=Column(String(255),nullable=False)
    role=Column(String(50),default="user")
    status=Column(Integer,default=1)
    created_by=Column(String(50),default="user")
    created_at=Column(DateTime,default=datetime.now ,server_default=text("CURRENT_TIMESTAMP"))
    modified_at=Column(DateTime,default=datetime.now ,server_default=text("CURRENT_TIMESTAMP"),onupdate=datetime.now, server_onupdate=text("CURRENT_TIMESTAMP"))
    orders = relationship("Order", back_populates="user")

class Product(Base):
    __tablename__="products"

    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50),nullable=False)
    description=Column(String(255),nullable=False)
    price=Column(Float,nullable=False)
    stock=Column(Integer,nullable=False)
    status=Column(Integer,default=1)
    created_by=Column(String(50),default="vendor")
    created_at=Column(DateTime,default=datetime.now ,server_default=text("CURRENT_TIMESTAMP"))
    modified_at=Column(DateTime,default=datetime.now ,server_default=text("CURRENT_TIMESTAMP"),onupdate=datetime.now, server_onupdate=text("CURRENT_TIMESTAMP"))
    order_items = relationship("Orderitem", back_populates="product")

class Order(Base):
    __tablename__="orders"

    id=Column(Integer,autoincrement=True,primary_key=True)
    user_id=Column(Integer,ForeignKey(User.id))
    total_amount=Column(Float)
    status=Column(Integer,default=1)
    created_at=Column(DateTime,default=datetime.now,server_default=text("CURRENT_TIMESTAMP"))
    user = relationship("User", back_populates="orders")
    orderitems = relationship("Orderitem", back_populates="order")

class Orderitem(Base):
    __tablename__="orderitems"

    id=Column(Integer,autoincrement=True,primary_key=True)
    order_id=Column(Integer,ForeignKey(Order.id))
    product_id=Column(Integer,ForeignKey(Product.id))
    quantity=Column(Integer)
    price=Column(Float)
    status=Column(Integer,default=1)
    created_at=Column(DateTime,default=datetime.now,server_default=text("CURRENT_TIMESTAMP"))
    order = relationship("Order", back_populates="orderitems")
    product = relationship("Product", back_populates="order_items")



Base.metadata.create_all(engine)




