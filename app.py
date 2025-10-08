from flask import Flask, jsonify
from flask_cors import CORS
from config.database import engine, Base
from routes.web import web
import models.perpustakaan_model  # register model

app = Flask(__name__)
CORS(app)

# Buat tabel otomatis
Base.metadata.create_all(bind=engine)

# Daftarkan blueprint
app.register_blueprint(web)

# ✅ Tambahkan route default biar Railway dapat respons
@app.route("/")
def home():
    return jsonify({
        "message": "API Perpustakaan aktif 🚀",
        "endpoints": ["/buku (GET, POST, PUT, DELETE)"]
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  # pakai port 8080 agar cocok dengan Railway
    app.run(host="0.0.0.0", port=port)
