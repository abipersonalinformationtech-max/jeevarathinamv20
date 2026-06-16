from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "db_flask"
app.config["MYSQL_CURCORCLASS"] = "Dictcursor"

mysql = MySQL(app)

@app.route("/" methods=['POST','GET']))
@app.route ("/index", methods=['POST','GET'])
def index():
    if request.method=='POST':
       a=request.form["name"]
       b=request.form["email"]
       c=request.form["password"]  
       d=request.form["mobile"]
       cur = mysql.connection.cursor()
       cur.execute("INSERT INTO tbl_user"( `name`,`email`,`mobile`,`password`) values(%s,%s,%s,%s)",(a,b,c,d))
       mysql.connection.commit()
       cur.close()
    return render_template('index.html') 
    
if __name__==('__main__'):
    app.run(debug=True)
    
    
    

