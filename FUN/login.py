#from flask import Flask,render_template
from flask import Flask,render_template, url_for, redirect
from flask_sqlalchemy  import SQLAlchemy
from flask_login import  UserMixin,LoginManager,login_user,login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')