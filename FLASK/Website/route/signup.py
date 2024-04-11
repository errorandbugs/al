from flask import Blueprint, render_template, redirect, request, url_for, flash
from MODEL import db, User
from login import login
signup_bp =Blueprint('signup',__name__, url_prefix='/signup')
@signup_bp.route('/',methods=['GET', 'POST'])

def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username Already exist', 'error')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created')
            return redirect(url_for('login.login'))