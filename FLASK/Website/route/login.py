from flask import Blueprint, render_template, redirect, request, url_for, flash,Flask
from MODEL import db, User
from flask_login import LoginManager

app = Flask(__name__)

login_bp =Blueprint('login',__name__, url_prefix='/login')
@login_bp.route('/',methods=['GET', 'POST'])

def login():
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
            return render_template(url_for('dashborad.html'))
        

if __name__ == "__main__":
    app.run(debug=True)