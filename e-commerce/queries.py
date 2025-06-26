# from random import randint, sample
# from sqlalchemy.orm import Session
# from models import engine,User,Product,Order,Orderitem

# # Create a session
# session = Session(bind=engine)

# user1 = User(
#     name="Rajesh R",
#     email="rajesh@example.com",
#     password="rajesh@02",
#     phone="9876543210",
#     address="Thoothukudi, TN"
# )

# user2 = User(
#     name="Priya M",
#     email="priya@example.com",
#     password="priya@02",
#     phone="9123656780",
#     address="Chennai, TN"
# )
# user3 = User(
#     name="kamal M",
#     email="kamal@example.com",
#     password="kamal@02",
#     phone="9123452780",
#     address="Kovilpatti, TN"
# )
# user4 = User(
#     name="Priyan M",
#     email="priyan@example.com",
#     password="priyan@02",
#     phone="9123456480",
#     address="Dindugal, TN"
# )
# user5 = User(
#     name="sathish M",
#     email="sathish@example.com",
#     password="sathish@02",
#     phone="9123456740",
#     address="Ooty, TN"
# )
# user6 = User(
#     name="Murugan M",
#     email="murugan@example.com",
#     password="murugan@02",
#     phone="9122456780",
#     address="Tiruchendur, TN"
# )
# user7 = User(
#     name="Jamal M",
#     email="jamal@example.com",
#     password="jamal@02",
#     phone="9123498780",
#     address="Chennai, TN" 
# )
# user8 = User(
#     name="Santhosh M",
#     email="santhosh@example.com",
#     password="santhosh@02",
#     phone="9123456080",
#     address="Tirunelveli, TN"
# )

# user9 = User(
#     name="Santhiya M",
#     email="santhiya@example.com",
#     password="santhiya",
#     phone="9123456781",
#     address="Salem, TN"
# )
# user10 = User(
#     name="kirthika M",
#     email="kirthika@example.com",
#     password="kirthika@02",
#     phone="9123456380",
#     address="Gobi, TN"
# )
# # session.add_all([user1, user2,user10,user3,user4,user5,user6,user7,user8,user9])
# # session.commit()


# product1 = Product(
#     name="Dell Laptop",
#     description="14-inch i5 11th Gen",
#     price=55000.00,
#     stock=10
# )

# product2 = Product(
#     name="Logitech Mouse",
#     description="Wireless Optical Mouse",
#     price=750.00,
#     stock=100
# )

# product3 = Product(
#     name="Samsung Monitor",
#     description="24-inch Full HD",
#     price=12000.00,
#     stock=20
# )

# product4 = Product(
#     name="Samsung Phone",
#     description="High performance",
#     price=14999.00,
#     stock=26
# )
# product5 = Product(
#     name="Asus Monitor",
#     description="24-inch Full HD",
#     price=50000.00,
#     stock=200
# )
# product6 = Product(
#     name="Asus laptop",
#     description="New vivo book 16",
#     price=54000.00,
#     stock=26
# )
# product7 = Product(
#     name="ROG",
#     description="High Performance gaming laptop",
#     price=200000.00,
#     stock=21
# )
# product8 = Product(
#     name="Realme 60x 5g",
#     description="New Gen",
#     price=20000.00,
#     stock=16
# )
# product9 = Product(
#     name="Lenova laptop",
#     description="New Lenova BNook",
#     price=42000.00,
#     stock=27
# )
# product10 = Product(
#     name="HP - Laptop",
#     description="stainless steel",
#     price=56000.00,
#     stock=2
# )
# # session.add_all([product1, product2, product3,product4,product5,product6,product7,product8,product9,product10])
# # session.commit()

# # from sqlalchemy.orm import Session
# # from models import User, Product, Order, Orderitem
# # from database import engine
# # from random import randint, sample

# # session = Session(bind=engine)

# for user_id in range(1, 11):  # 10 users, user_id 1 to 10
#     # Step 1: Create the order
#     new_order = Order(user_id=user_id, total_amount=0)
#     session.add(new_order)
#     session.commit()  # Now new_order.id is available

#     # Step 2: Pick 2 random products for this order
#     product_ids = sample(range(1, 11), 2)  # Pick 2 products from 1–10
#     total = 0

#     for pid in product_ids:
#         product = session.get(Product, pid)
#         quantity = randint(1, 3)  # Quantity: 1 to 3
#         price = product.price
#         subtotal = price * quantity
#         total += subtotal

#         # Create OrderItem
#         order_item = Orderitem(
#             order_id=new_order.id,
#             product_id=product.id,
#             quantity=quantity,
#             price=price
#         )
#         session.add(order_item)

#     # Step 3: Update total in order
#     new_order.total_amount = total
#     session.commit()




