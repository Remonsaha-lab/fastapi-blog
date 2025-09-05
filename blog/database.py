from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Use DATABASE_URL if provided (e.g. Render Postgres), else fall back to local sqlite file
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./blog.db')

if SQLALCHEMY_DATABASE_URL.startswith('sqlite'):  # sqlite needs special connect args
  engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
  engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()