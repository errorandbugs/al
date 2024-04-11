from flask import Blueprint

log = Blueprint("log",__name__)

@log.route("/")
def home():
    return "<h1>Test</h1>"
