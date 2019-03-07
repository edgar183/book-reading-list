from app import models
from app import app

@app.route('/')
def index():
    return "The home page....."

@app.route('/login')
def login():
    return "The login page....."
    

@app.route('/register')
def register():
    return "The register page....."