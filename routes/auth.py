from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

auth = Blueprint('auth', __name__)

#-----------------Signup Route-----------------#
@auth.route('/signup', methods=['POST'])
def signup():
    username = request.form['signup-username']
    email = request.form['signup-email']
    password = request.form['signup-password']
    
    if not username or not email or not password:
        flash('All fields are required.')
        return redirect(url_for('index'))

    #Lets Hash the password 
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    
    #Lets check if the user already exists
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        flash('Username or email already exists.')
        return redirect(url_for('index'))
    
    #Lets save new user to the database
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    flash('Signup successful! You can now login.')
    return redirect(url_for('welcome'))

#-----------------Login Route-----------------#
@auth.route('/login', methods=['POST'])
def login():
    username = request.form['login-username']
    password = request.form['login-password']
    
    #lets check if user is entering both username and password
    if not username or not password:
        flash('All fields are required yes all fields.')
        return redirect(url_for('index'))
    
    user = User.query.filter_by(username=username).first()
    
    if user:
        if check_password_hash(user.password, password):
            flash('Login successful!')
            #here we are storing the user id in the session
            session['user_id'] = user.id   
            return redirect(url_for('dashboard'))
        else:
            flash('Wrong password.')
            return redirect(url_for('index'))
    else:
        flash('User not found.')
        return redirect(url_for('index'))
    
#-----------------Logout Route-----------------#
@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    # flash('You have been logged out.')
    return redirect(url_for('index'))

#--------------------------------------------#