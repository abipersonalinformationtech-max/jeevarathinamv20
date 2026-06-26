from flask import Flask,flash, render_template, request,url_for,redirect,Response,session,send_file,send_from_directory
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_class'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route("/")
@app.route('/index',methods=['POST','GET'])
def index():
    return render_template("index.html")
    
@app.route("/reg",methods=['POST','GET'])
def reg():
    if request.method=='POST':
        if request.form["submit"]=="Register":
            a=request.form["uname"]
            b=request.form["age"]
            c=request.form["email"]
            d=request.form["mobile"]
            cur=mysql.connection.cursor()
            cur.execute("INSERT INTO tbl_register(rname,rage,email,phone) values(%s,%s,%s,%s)" ,(a,b,c,d))
            mysql.connection.commit()
            cur.close()
    return render_template("reg.html")
    
@app.route('/views',methods=['POST','GET'])
def views():
    cur=mysql.connection.cursor()
    cur.execute("select * from tbl_register")
    data=cur.fetchall()	
    return render_template("views.html",datas=data)
    
if __name__=='__main__':
    app.run(debug=True)

	