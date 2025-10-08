import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ambil URL database dari environment (Railway)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check Railway Variables.")

# Buat koneksi database
engine = create_engine(DATABASE_URL, echo=False)

# ORM setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
