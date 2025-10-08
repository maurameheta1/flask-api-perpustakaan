from flask import Flask
from flask_cors import CORS
from config.database import engine, Base
from routes.web import web
import models.perpustakaan_model  # register model

app = Flask(__name__)
CORS(app)  # aktifkan CORS untuk semua route

# Buat tabel otomatis (kalau belum ada di DB)
Base.metadata.create_all(bind=engine)

# Daftarkan blueprint route
app.register_blueprint(web)

# Endpoint default agar Railway tahu API hidup
@app.route("/")
def home():
    return {"message": "API Flask Perpustakaan aktif 🚀"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))  # Gunakan port Railway
    app.run(host="0.0.0.0", port=port)
