from flask import Blueprint, redirect, url_for, session, flash
from models import db, User
from authlib.integrations.flask_client import OAuth
import os
from dotenv import load_dotenv
google_login = Blueprint('google_login', __name__)

oauth = OAuth()
load_dotenv()

google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'}
)

#-----------------google login Route-----------------#
@google_login.route('/login/google')
def login_google():
    redirect_url = url_for('google_login.authorize_google', _external=True)
    return google.authorize_redirect(redirect_url)

@google_login.route('/login/google/authorize')
def authorize_google():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    email = user_info['email']

    #lets check if the user already exists
    user = User.query.filter_by(email=email).first()
    if not user:
        new_user = User(username=user_info['name'], email=email, password='')
        db.session.add(new_user)
        db.session.commit()
        #this one is to get new user id
        user = User.query.filter_by(email=email).first()
    
    session['user_id'] = user.id
    flash('Google Login successful!')
    return redirect(url_for('dashboard'))
