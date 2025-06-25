from sqlalchemy import create_engine,text
from models import session

db_url="mysql+pymysql://root:2741@localhost:3307/"
db_name="e_commerce_fastapi"

engine=create_engine(db_url)

def create_db():
    with engine.connect() as conn:
        conn.execute(text(f'CREATE DATABASE IF NOT EXISTS {db_name}'))
        print(f"Data Base Created Successfully {db_name}")

# create_db()

def get_db():
    db = session
    try:
        yield db
    finally:
        db.close()