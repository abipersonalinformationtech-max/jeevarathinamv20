from flask import Flask,render_template,session,request,redirect,flash,url_for
from flask_mysqldb import MySQL

app = Flask(__name__) 

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
            flash("login Successful",'success')
            return redirect(url_for('home'))
        else:
            flash("Invalid Credentials..Try Again!..",'danger')
    return render_template("index.html")
    
@app.route('/logout')
def logout():
    session.clear()
    flash("Logout Successfully..",'success')
    return redirect('login')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method=='POST':
        a=request.form["uname"]
        b=request.form["email"]
        c=request.form["mobile_no"]
        d=request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute("insert into tbl_users( name, email, mobile_no, password) values(%s,%s,%s,%s)",(a,b,c,d))
        mysql.connection.commit()
        cur.close()
        flash("Registration Successfull",'success')
    return render_template("register.html")
    
@app.route("/home")
def home():
    return render_template("home.html")
    
if __name__ == '__main__':
    app.secret_key = 'abc123'
    app.run(debug=True)
    