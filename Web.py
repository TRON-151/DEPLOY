from flask import Flask, flash, render_template, redirect, session, url_for 
from models import db, User 
from routes.auth import auth
from routes.google_login import google_login, oauth
from routes.user import user_routes
from dotenv import load_dotenv
import os
app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY', 'default_key')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#lets initialize the Oauth
oauth.init_app(app)
#also the db
db.init_app(app)

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(google_login, url_prefix='/google_login')
app.register_blueprint(user_routes, url_prefix='/user')

#-----------------Main Route-----------------#
@app.route('/')
def index():
    return render_template('Landing_page.html')

#-----------------welcome Route-------------------#
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

#-----------------Dashboard Route-----------------#
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first.')
        return redirect(url_for('index'))
    
    user = User.query.get(session['user_id'])
    return render_template('dashboard.html', username=user.username)

#--------------------------------------------#
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)

