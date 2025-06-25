from pydantic import BaseModel
from typing import List
from datetime import datetime,date
class User_out(BaseModel):
    id:int
    name:str
    email:str
    phone:str
    address:str


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderCreate(BaseModel):
    user_id: int
    total_amount: float
    items: List[OrderItemCreate]

class Order_list(BaseModel):
    order_id:int
    product_name:str
    quantity:int
    price:float
    created_at:datetime

class Orderall(BaseModel):
    name:str
    order_id:int
    total_amount:float
class order_all_user(Orderall):
    orders:list[Order_list]

    class Config:
        from_attributes=True

class Get_orders(BaseModel):
    username:str
    total_orders:int


class get_date(BaseModel):
    from_date:date
    to_date:date

class Top_buy(BaseModel):
    order_id:int
    price:float
    date: date

    class Config:
        from_attributes=True

