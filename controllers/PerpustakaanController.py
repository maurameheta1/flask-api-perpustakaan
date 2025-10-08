from flask import jsonify, request
from config.database import get_db
from models.perpustakaan_model import Perpustakaan
from sqlalchemy.orm import Session

# GET semua buku
def get_all_buku():
    db: Session = next(get_db())
    data = db.query(Perpustakaan).all()
    return jsonify([
        {
            "id_buku": k.id_buku,
            "judul_buku": k.judul_buku,
            "pengarang": k.pengarang,
            "penerbit": k.penerbit,
            "tahun": k.tahun,
            "isbn": k.isbn,
            "cover": k.cover,
        } for k in data
    ])

# POST tambah buku
def add_buku():
    db: Session = next(get_db())
    body = request.json

    new_data = Perpustakaan(
        judul_buku=body["judul_buku"],
        pengarang=body["pengarang"],
        penerbit=body["penerbit"],
        tahun=body["tahun"],
        isbn=body["isbn"],
        cover=body["cover"]
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return jsonify({
        "message": "Data berhasil ditambahkan",
        "id_buku": new_data.id_buku
    })

# PUT update buku
def update_buku(id_buku):
    db: Session = next(get_db())
    body = request.json

    buku = db.query(Perpustakaan).filter(Perpustakaan.id_buku == id_buku).first()
    if not buku:
        return jsonify({"message": "Data buku tidak ditemukan"}), 404

    buku.judul_buku = body.get("judul_buku", buku.judul_buku)
    buku.pengarang = body.get("pengarang", buku.pengarang)
    buku.penerbit = body.get("penerbit", buku.penerbit)
    buku.tahun = body.get("tahun", buku.tahun)
    buku.isbn = body.get("isbn", buku.isbn)
    buku.cover = body.get("cover", buku.cover)

    db.commit()
    db.refresh(buku)

    return jsonify({
        "message": "Data buku berhasil diperbarui",
        "id_buku": buku.id_buku
    })

# DELETE buku
def delete_buku(id_buku):
    db: Session = next(get_db())
    buku = db.query(Perpustakaan).filter(Perpustakaan.id_buku == id_buku).first()
    if not buku:
        return jsonify({"message": "Data buku tidak ditemukan"}), 404

    db.delete(buku)
    db.commit()

    return jsonify({
        "message": f"Data buku dengan id {id_buku} berhasil dihapus"
    })
