from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Добро пожаловать на сайт!</h1>"

@app.route("/products")
def products():
    data = [
        {"name": "Крем для лица", "price": 80000},
        {"name": "Шампунь", "price": 50000},
        {"name": "Помада", "price": 65000}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

