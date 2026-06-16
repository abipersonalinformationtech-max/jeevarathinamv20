from flask import Flask,render_template,session,request,redirect,flash,url_for
from flask_mysqldb import MySQL

from werkzeug.utils import secure_filename
import os
from datetime import date

app = Flask(__name__) 

app.config['UPLOAD_FOLDER']='static/uploads'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_blog'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route('/')
@app.route('/login', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        a=request.form["uname"]
        b=request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute("select * from tbl_users where name=%s and password=%s",(a,b))
        data = cur.fetchone()
        if data:
            session["login_in"] = True
            session["uid"] = data["uid"]
            session["username"] = data["name"]
            flash("Login Successfull",'success')
            return redirect(url_for('home'))
        else:
            flash("Invalid Credentials..Try Again!..",'danger')
    return render_template("index.html")
    
@app.route('/logout')
def logout():
    session.clear()
    flash("logout Successfully..",'success')
    return redirect('login')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=='POST':
        a=request.form["uname"]
        b=request.form["email"]
        c=request.form["mobile_no"]
        d=request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_users( name, email, mobile_no, password) values (%s,%s,%s,%s)",(a,b,c,d))
        mysql.connection.commit()
        cur.close()
        flash("Registration Successfull",'success')
    return render_template("register.html")
    
@app.route("/home")
def home():
    if 'uid' not in session:
        return redirect(url_for('login'))
        
    cur = mysql.connection.cursor()
    cur.execute("select * from tbl_post")
    data = cur.fetchall()
    return render_template("home.html",datas=data)
    
    
@app.route("/singlepost/<int:pid>")
def singlepost(pid):
    cur= mysql.connection.cursor()
    cur.execute("select p.*,u.name from tbl_post p inner join tbl_users u on p.uid=u.uid where p.pid=%s",(pid,))
    data = cur.fetchone()
    return render_template("singlepost.html",datas=data)
    
@app.route("/addpost",methods=['POST','GET'])
def addpost():
    if request.method=='POST':
        a=request.form['ptitle']
        b=request.form['pdes']
        image=request.files['pimage']
        filename = ""
        
        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            
           
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_post (uid, ptitle, pdes, pdate, pimage) values (%s,%s,%s,%s,%s)",(session["uid"],a,b,date.today(),filename))
        mysql.connection.commit()
        cur.close()
        flash("Registration Successfull",'success')
        
    return render_template("addpost.html")
       
    
    
if __name__ == '__main__':
    app.secret_key = 'abc123'
    app.run(debug=True)
    
    
    