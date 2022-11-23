from flask import Flask
from flask import render_template

from settings import HOST
from settings import PORT
from settings import DEBUG

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)
