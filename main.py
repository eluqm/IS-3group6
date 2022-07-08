from flask import Flask
app = Flask(__name__)


@app.route('/')
def hola():
    return "<h1>Welcome to Huella Carbono init project</h1>"
