from sqlalchemy import create_engine,text
from models import session

db_url="mysql+pymysql://root:2741@localhost:3307"
engine=create_engine(db_url)
db_name="studentsfastapi"

def create_db():
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print("Database Created Successfully")

def get_db():
    db=session
    try:
        yield db
    finally:
        db.close()