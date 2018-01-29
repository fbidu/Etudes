import flask
import math
from flask_cors import CORS

APP = flask.Flask(__name__)
CORS(APP)

def unprocessable(message):
    response = flask.jsonify(message)
    response.status_code = 422
    return response

@APP.route("/")
def home():
    return "Oh, hai"


@APP.route("/factorial/<int:a>")
def factorial(a):
    return str(math.factorial(a))


@APP.route("/upper", methods=['POST'])
def up():
    name = flask.request.json['name']

    if name == "":
        return unprocessable({"name": "This field is required"})

    upper = name.upper()
    if name != upper:
        return flask.jsonify({"name": name.upper()})

    return flask.jsonify({"name": name+"STER"})

if __name__ == "__main__":
    APP.run(debug=True)
