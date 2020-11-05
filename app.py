from flask import Flask

app = Flask(__name__)

# create flask route
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/test/')
def test_func():
    return 'This is a test of the Code Monkey Emergency Signaling System (CMESS)!'
