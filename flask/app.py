from flask import Flask, render_template, session, request, redirect, flash, url_for
import pymysql
from werkzeug.utils import secure_filename
import os
from datetime import date

app = Flask(__name__)

app.secret_key = 'abc123'
app.config['UPLOAD_FOLDER'] = 'static/uploads'


# DATABASE CONNECTION
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='db_blog',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        a = request.form["uname"]
        b = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM tbl_users WHERE name=%s AND password=%s", (a, b))
        data = cur.fetchone()

        conn.close()

        if data:
            session["login_in"] = True
            session["uid"] = data["uid"]
            session["username"] = data["name"]
            flash("Login Successful", 'success')
            return redirect(url_for('home'))
        else:
            flash("Invalid Credentials..Try Again!", 'danger')

    return render_template("index.html")


@app.route('/logout')
def logout():
    session.clear()
    flash("Logout Successfully", 'success')
    return redirect(url_for('index'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        a = request.form["uname"]
        b = request.form["email"]
        c = request.form["mobile_no"]
        d = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO tbl_users(name, email, mobile_no, password) VALUES (%s,%s,%s,%s)",
            (a, b, c, d)
        )

        conn.commit()
        conn.close()

        flash("Registration Successful", 'success')

    return render_template("register.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/addpost", methods=['POST', 'GET'])
def addpost():
    if request.method == 'POST':
        a = request.form['ptitle']
        b = request.form['pdes']
        image = request.files['pimage']

        filename = ""

        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO tbl_post (uid, ptitle, pdes, pdate, pimage) VALUES (%s,%s,%s,%s,%s)",
            (session["uid"], a, b, date.today(), filename)
        )

        conn.commit()
        conn.close()

        flash("Post added successfully", 'success')

    return render_template("addpost.html")


if __name__ == "__main__":
    app.run(debug=True)