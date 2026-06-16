from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",   
    database="jr_food_order"
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/order', methods=['POST'])
def order():
    name = request.form['name']
    phone = request.form['phone']
    food = request.form['food']

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders (customer_name, phone, food_item) VALUES (%s,%s,%s)",
        (name, phone, food)
    )

    conn.commit()

    return "Order Placed Successfully"

if __name__ == '__main__':
    app.run(debug=True)