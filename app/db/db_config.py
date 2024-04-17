import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv("POSTGRES_DB_URL")

print(DATABASE_URL)


engine = create_engine(DATABASE_URL, connect_args={}, future=True)

SessionLocal = sessionmaker(future=True, autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# get the db
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
