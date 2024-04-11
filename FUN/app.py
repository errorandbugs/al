from flask import Flask,render_template, url_for, redirect
from flask_sqlalchemy  import SQLAlchemy
from flask_login import  UserMixin,LoginManager,login_user,login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, length, ValidationError
from flask_bcrypt import Bcrypt


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = "$#@!~~!@#$%^&*())"
db.create_all

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class user(db.Model,UserMixin):
    id = db.column(db.integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)


class ReigisterFrom(FlaskForm):
    username = StringField(validators=[InputRequired(),length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    
    Password = PasswordField(validators=[InputRequired(),length(
        min=4, max=20)],render_kw={"placeholder", "password"})
    
    submit = SubmitField("Registe")

    def Validata_username(self, username):
        existing_user_username = user.query.filter_by(
            username=username.data).first()
        
        if existing_user_username:
            raise ValidationError(
                "THAT Username Already Exists. please choose a different one.")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(),length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    Password = PasswordField(validators=[InputRequired(), length(
        min=4, max=20)], render_kw={"placeholder": "password"})

    submit = SubmitField("Login")


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = user.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashbroad'))
    return render_template('login.html',form=form)

@app.route('/dashbroad', methods=['GET', 'POST'])
@login_required
def dashbroad():
    return render_template('dashbroad.html')


@app.route('/logout', methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = ReigisterFrom()

    if form.Validata_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.Password.data)
        new_user = user(Username =form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commJit()
        return redirect(url_for('login'))


    return render_template('signup.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)