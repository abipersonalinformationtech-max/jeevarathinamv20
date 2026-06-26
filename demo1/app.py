from flask import Flask,render_template,url_for
app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/adminlogin')
def admin():
    return render_template("admin_login.html")
    
@app.route('/studentlogin')
def student():
    return render_template("student_login.html")
    
@app.route('/admin')
def adep():
    return render_template("adep.html")
    
@app.route('/student')
def result():
    return render_template("result.html")
    
if __name__=='__main__':
    app.run(debug=True)