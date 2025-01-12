from flask import Blueprint, redirect, url_for, flash, session
from models import db, User

user_routes = Blueprint('user_routes', __name__)

#-------------Delete account Route----------#
@user_routes.route('/delete_account', methods=['POST'])
def delete_account():
    if 'user_id' not in session:
        flash('You need to log in first.')
        return redirect(url_for('index'))
    
    user = User.query.get(session['user_id'])
    if user:
        db.session.delete(user)
        db.session.commit()
        #lets log the user out after the deletion
        session.pop('user_id', None)  
        flash('Your account has been deleted successfully.')
        return redirect(url_for('index'))
    else:
        flash('Account not found.')
        return redirect(url_for('dashboard'))
