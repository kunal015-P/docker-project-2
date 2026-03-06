from flask import Flask
from routes.products import products

app = Flask(__name__)

app.register_blueprint(products)

@app.route("/")
def home():
    return "Docker E-Commerce Backend Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
