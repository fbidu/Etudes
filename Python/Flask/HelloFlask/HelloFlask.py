from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/[sid]')
def say(sid):
    return sid





if __name__ == '__main__':
    app.run()
