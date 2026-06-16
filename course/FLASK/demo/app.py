#pip install flask
from flask import Flask,render_template,request,flash,session,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "db_blog"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql=MySQL(app)


@app.route("/")
def index():
    name = "Ram"
    fruits = ["Apple","Orange","Mango"]
    return render_template("index.html",name=name,fruits=fruits)

@app.route("/shop")
def shop():
    
    return render_template("shop.html")

@app.route("/users")
def users():
    cur = mysql.connection.cursor()
    cur.execute("select * from tbl_users")
    data = cur.fetchall()
    return render_template("users.html",records = data)

@app.route("/add_user",methods=["POST","GET"])
def add_user():
    if request.method=='POST':
        a = request.form["uname"]
        b = request.form["uemail"]
        c = request.form["umobile"]
        d = request.form["upassword"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO `tbl_users`(`uname`, `uemail`, `umobile`, `upassword`) VALUES (%s,%s,%s,%s)",(a,b,c,d))
        mysql.connection.commit()
        cur.close()
        flash("User Added Successfull","success")
    return render_template("add_user.html")

@app.route("/edit_user/<string:uid>",methods=["POST","GET"])
def edit_user(uid):
    if request.method=='POST':
        a = request.form["uname"]
        b = request.form["uemail"]
        c = request.form["umobile"]
        d = request.form["upassword"]
        cur = mysql.connection.cursor()
        cur.execute("update tbl_users set uname=%s,uemail=%s,umobile=%s,upassword=%s where uid=%s",(a,b,c,d,uid))
        mysql.connection.commit()
        cur.close()
        flash("User Updated Successfull","success")
    cur = mysql.connection.cursor()
    cur.execute("select * from tbl_users where uid=%s",(uid))
    data = cur.fetchone()
    return render_template("edit_user.html",info = data)

@app.route("/del_user/<string:uid>",methods=['GET','POST'])
def del_user(uid):
    cur = mysql.connection.cursor()
    cur.execute("delete from tbl_users where uid=%s",(uid))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("users"))

if __name__ == '__main__':
    app.secret_key='abc123'
    app.run(debug=True)