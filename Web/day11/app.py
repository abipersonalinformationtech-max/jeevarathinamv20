from flask import Flask,render_template,session,request,redirect,flash
from flask_mysqldb import MySQL

app = Flask(__name__) 

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_blog'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route('/')
@app.route('/login')
def index():
    return render_template("index.html")

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
    
if __name__ == '__main__':
    app.secret_key = 'abc123'
    app.run(debug=True)
    