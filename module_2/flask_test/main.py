# This is not an excutable code block
from flask import Flask

app = Flask("myapp")

@app.route('/')
def hello_world():
    return 'Hello, World!'