from flask import Flask,render_template

app = Flask(__name__) 


@app.route('/')
@app.route('/login')
def index():
    return render_template("index.html")
    

@app.route('/register')
def register():
    return render_template("register.html")
    
    
if __name__ == '__main__':
    app.secret_key = 'abc123'
    app.run(debug=True)
    