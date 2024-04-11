
from flask import Flask
from flask_restful import Resource, Api
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'bassceethehot'
     
    from .log import log
    from .auth import auth

    app.register_blueprint(log,url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app 

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)