
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def hello():
    return "hola"

@app.route('/post', methods=['POST'])
def create():
    return 'post'