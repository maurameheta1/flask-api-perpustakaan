from flask import Blueprint
from controllers.PerpustakaanController import get_all_buku, add_buku, update_buku, delete_buku

web = Blueprint("web", __name__)

# Endpoint API
web.route("/buku", methods=["GET"])(get_all_buku)
web.route("/buku", methods=["POST"])(add_buku)
web.route("/buku/<int:id_buku>", methods=["PUT"])(update_buku)
web.route("/buku/<int:id_buku>", methods=["DELETE"])(delete_buku)

