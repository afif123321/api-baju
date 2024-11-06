# app.py
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

# Data baju (database sederhana)
baju_data = [
    {
        "id": 1,
        "nama": "Kaos Polos",
        "harga": 50000,
        "stok": 100
    },
    {
        "id": 2,
        "nama": "Kemeja Batik",
        "harga": 120000,
        "stok": 50
    },
    {
        "id": 3,
        "nama": "Hoodie",
        "harga": 150000,
        "stok": 30
    },
    {
        "id": 4,
        "nama": "Jaket Denim",
        "harga": 200000,
        "stok": 25
    },
    {
        "id": 5,
        "nama": "Sweater Rajut",
        "harga": 130000,
        "stok": 40
    },
    {
        "id": 6,
        "nama": "Kaos Oversize",
        "harga": 75000,
        "stok": 60
    },
    {
        "id": 7,
        "nama": "Polo Shirt",
        "harga": 90000,
        "stok": 80
    },
    {
        "id": 8,
        "nama": "Celana Chino",
        "harga": 120000,
        "stok": 45
    },
    {
        "id": 9,
        "nama": "Celana Jeans",
        "harga": 140000,
        "stok": 70
    },
    {
        "id": 10,
        "nama": "Jaket Kulit",
        "harga": 250000,
        "stok": 10
    }
]

# Helper functions
def get_all_baju():
    return baju_data

def get_baju_by_id(baju_id):
    return next((baju for baju in baju_data if baju["id"] == baju_id), None)

# Resource untuk daftar baju (GET & POST)
class BajuList(Resource):
    def get(self):
        return jsonify(get_all_baju())

    def post(self):
        new_baju = request.get_json()
        new_baju["id"] = baju_data[-1]["id"] + 1 if baju_data else 1
        baju_data.append(new_baju)
        return jsonify(new_baju), 201

# Resource untuk baju individu (GET, PUT, DELETE)
class Baju(Resource):
    def get(self, baju_id):
        baju = get_baju_by_id(baju_id)
        if baju:
            return jsonify(baju)
        return jsonify({"error": "Baju tidak ditemukan"}), 404

    def put(self, baju_id):
        baju = get_baju_by_id(baju_id)
        if not baju:
            return jsonify({"error": "Baju tidak ditemukan"}), 404
        update_data = request.get_json()
        baju.update(update_data)
        return jsonify(baju)

    def delete(self, baju_id):
        global baju_data
        baju_data = [baju for baju in baju_data if baju["id"] != baju_id]
        return jsonify({"message": "Baju berhasil dihapus"}), 204

# Menambahkan endpoint ke API
api.add_resource(BajuList, "/baju")
api.add_resource(Baju, "/baju/<int:baju_id>")

# Menjalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)
