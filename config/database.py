import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables dari file .env
load_dotenv()

# Ambil URL database dari environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Pastikan URL tidak None
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Please check your .env file or Railway environment variables.")

# Buat engine koneksi
engine = create_engine(DATABASE_URL, echo=True)

# Session dan Base ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
