from sqlalchemy import create_engine,text
from . models import Session

db_url="mysql+pymysql://root:2741@localhost:3307"
db_name="collegefastapi"

engine=create_engine(db_url)

def create_db():
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
        print(f"Database Created Successfully with Name of {db_name}")

# create_db()

def get_db():
    db=Session
    try:
        yield db
    finally:
        db.close()