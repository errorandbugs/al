from flask import Flask
from flask_sqlalchemy import SQLAlcamy
from flask_login import LoginManager

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
