from app import models
from app import app

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/login')
def login():
    return render_template('login.html', title='Login')
    

@app.route('/register')
def register():
    return render_template('register.html', title='Register')