from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://pi2usertest:pi2passtest@dbtest:5442/irrigation_app_test"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def override_get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()