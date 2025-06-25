from fastapi import FastAPI,Depends
import models,schemas
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc, func,and_
from typing import List
from datetime import datetime,date

app=FastAPI()

@app.get('/getuser',response_model=List[schemas.User_out])
def get_user(db:Session=Depends(get_db)):
    user=db.query(models.User).all()
    return user


# Input: user_id,
# Output: List of order IDs, total amounts, order dates, with product name 

# @app.get('/getuser/allorder/{id}',response_model=schemas.order_all_user)
# def get_all(id:int,db:Session=Depends(get_db)):
#     getall=db.query(models.User.name,models.Order.id,models.Order.total_amount,models.Orderitem.id,models.Product.name,models.Orderitem.quantity,models.Orderitem.price,models.Orderitem.created_at).join(models.User.orders).join(models.Order.orderitems).join(models.Orderitem.product).filter(models.User.id==id).group_by(models.User.name,models.Order.total_amount,models.Order.id,models.Orderitem.id,models.Product.name,models.Orderitem.quantity,models.Orderitem.price,models.Orderitem.created_at).all()
    
    

#     return[
#             {
#                 "name":i[0],
#                 "order_id":i[1],
#                 "total_amount":i[2],
            
#                 "orders":List["order_id":[3][0],"product_name":[3][1],"quantity":[3][2],"price":[3][3],"created_at":[3][4]]

#             }
#             for i in getall
#             for j in i[3]
        
        
#     ]

@app.get('/getusers/desc',response_model=List[schemas.Get_orders])
def get_user_all(db:Session=Depends(get_db)):
    get_data=db.query(models.User.name,func.count(models.Orderitem.id)).join(models.User.orders).join(models.Order.orderitems).group_by(models.User.name).order_by(desc(func.count(models.Orderitem.id))).order_by(asc(models.User.name)).all()
    
    return[
        
        {
            "username":i[0],
            "total_orders":i[1]

        }
        for i in get_data
        
    ]

@app.post('/getusers/datetime')
def get_data_bydate(data:schemas.get_date,db:Session=Depends(get_db)):
    by_date=db.query(models.Orderitem).filter(func.date(models.Orderitem.created_at)>=data.from_date,func.date(models.Orderitem.created_at)<=data.to_date).all()

    return by_date


@app.get('/getusers/top_buy')
def get_topbuy(db:Session=Depends(get_db)):
    get_top_buy=db.query(models.Orderitem.id,models.Orderitem.price,models.Orderitem.created_at).order_by(desc(models.Orderitem.price)).limit(1).all()

    return[
        {
            "order_id":i[0],
            "price":i[1],
            "date":i[2]
        }
        for i in get_top_buy
    ]

@app.get('/getusers/top_buy_daily')
def top_buy_daily(db:Session=Depends(get_db)):
    subquery=db.query(func.date(models.Orderitem.created_at).label('order_date'),func.max(models.Orderitem.price).label('max')).group_by(func.date(models.Orderitem.created_at)).subquery()

    get_data=db.query(models.Orderitem).join(subquery,and_(func.date(models.Orderitem.created_at)==subquery.c.order_date,models.Orderitem.price==subquery.c.max)).all()

    return[
        {
            "order_id":i.id,
            "price":i.price,
            "date":i.created_at
        }
        for i in get_data
    ]


