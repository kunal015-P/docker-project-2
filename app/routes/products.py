from flask import Blueprint, jsonify
from db import get_db_connection

products = Blueprint("products", __name__)

@products.route("/products")
def get_products():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, price FROM products")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    product_list = []

    for row in rows:
        product_list.append({
            "id": row[0],
            "name": row[1],
            "price": row[2]
        })

    return jsonify(product_list)
