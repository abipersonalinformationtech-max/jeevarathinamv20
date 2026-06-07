from flask import Flask, render_template, session, request, redirect, flash, url_for
from werkzeug.utils import secure_filename
import pymysql
import os
from datetime import date

app = Flask(__name__)
app.secret_key = "abc123"

# Upload Folder
UPLOAD_FOLDER = "static/uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# MySQL Connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="db_blog",
    cursorclass=pymysql.cursors.DictCursor
)

# ================= LOGIN =================

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form["uname"]
        password = request.form["password"]

        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM tbl_users WHERE name=%s AND password=%s",
            (username, password)
        )

        data = cur.fetchone()
        cur.close()

        print("Username:", username)
        print("Password:", password)
        print("Result:", data)

        if data:
            session["uid"] = data["uid"]
            session["username"] = data["name"]

            flash("Login Successful", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid Username or Password", "danger")

    return render_template("index.html")


# ================= LOGOUT =================

@app.route('/logout')
def logout():
    session.clear()
    flash("Logout Successful", "success")
    return redirect(url_for('index'))


# ================= REGISTER =================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form["uname"]
        email = request.form["email"]
        mobile = request.form["mobile_no"]
        password = request.form["password"]

        cur = conn.cursor()

        # Username already exists check
        cur.execute(
            "SELECT * FROM tbl_users WHERE name=%s",
            (username,)
        )

        user = cur.fetchone()

        if user:
            flash("Username already exists", "danger")
        else:
            cur.execute(
                """
                INSERT INTO tbl_users
                (name,email,mobile_no,password)
                VALUES (%s,%s,%s,%s)
                """,
                (username, email, mobile, password)
            )

            conn.commit()
            flash("Registration Successful", "success")

        cur.close()

    return render_template("register.html")


# ================= HOME =================

@app.route('/home')
def home():
    if 'uid' not in session:
        return redirect(url_for('index'))

    cur = conn.cursor()
    cur.execute("""
        SELECT p.*,u.name
        FROM tbl_post p
        INNER JOIN tbl_users u
        ON p.uid=u.uid
        ORDER BY p.pid DESC
    """)

    data = cur.fetchall()
    cur.close()

    return render_template("home.html", datas=data)


# ================= SINGLE POST =================

@app.route('/singlepost/<int:pid>')
def singlepost(pid):

    cur = conn.cursor()

    cur.execute("""
        SELECT p.*,u.name
        FROM tbl_post p
        INNER JOIN tbl_users u
        ON p.uid=u.uid
        WHERE p.pid=%s
    """, (pid,))

    data = cur.fetchone()
    cur.close()

    return render_template("singlepost.html", datas=data)


# ================= ADD POST =================

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():

    if 'uid' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':

        title = request.form['ptitle']
        description = request.form['pdes']

        filename = ""

        if 'pimage' in request.files:
            image = request.files['pimage']

            if image.filename != "":
                filename = secure_filename(image.filename)

                image.save(
                    os.path.join(
                        app.config['UPLOAD_FOLDER'],
                        filename
                    )
                )

        cur = conn.cursor()

        cur.execute("""
            INSERT INTO tbl_post
            (uid, ptitle, pdes, pdate, pimage)
            VALUES (%s,%s,%s,%s,%s)
        """,
        (
            session["uid"],
            title,
            description,
            date.today(),
            filename
        ))

        conn.commit()
        cur.close()

        flash("Post Added Successfully", "success")
        return redirect(url_for('home'))

    return render_template("addpost.html")


# ================= RUN =================

if __name__ == '__main__':
    app.run(debug=True)