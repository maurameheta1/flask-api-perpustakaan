from sqlalchemy import Column, Integer, String
from config.database import Base

class Perpustakaan(Base):
    __tablename__ = "buku"

    id_buku = Column(Integer, primary_key=True, index=True)
    judul_buku = Column(String(150), nullable=False)     
    pengarang = Column(String(100), nullable=False) 
    penerbit = Column(String(100), nullable=False) 
    tahun = Column(Integer, nullable=False) 
    isbn = Column(String(20), nullable=False) 
    cover = Column(String(100), nullable=False) # format datetime


