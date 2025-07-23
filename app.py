from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Добро пожаловать на сайт!</h1>"

@app.route("/products")
def get_products():
    products = [
        {"name": "Крем для лица", "price": 80000},
        {"name": "Шампунь", "price": 50000},
        {"name": "Помада", "price": 65000}
    ]
    return render_template('products.html', products=products)


if __name__ == "__main__":
    app.run(debug=True)

