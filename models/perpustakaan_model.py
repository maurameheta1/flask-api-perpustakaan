from sqlalchemy import Column, Integer, String
from config.database import Base

class Perpustakaan(Base):
    __tablename__ = "buku"

    id_buku = Column(Integer, primary_key=True, index=True)
    judul_buku = Column(String(255))
    pengarang = Column(String(255))
    penerbit = Column(String(255))
    tahun = Column(String(10))
    isbn = Column(String(50))
    cover = Column(String(255))
