from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user(db.model):
    id = db.column(db.integer, primary_key = True)
    username = db.column(db.string, unique = True, nullable=False)
    password = db.column(db.string(100),nullable=False)

    def setpass(self,password):
        self.password_hash = generate_password_hash(password)

    def checkpass(self,password):
        return checkpass(self,password_hash,password)