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

@APP.route("/projects", methods=["GET", "POST"])
def projects():
    prjs = [
        {
            "name": "Project Zero",
            "description": "The Beginning of it all"
        },
        {
            "name": "Project Alpha",
            "description": "The one that comes before the omega"
        },
        {
            "name": "Project Omega",
            "description": "The End"
        }
    ]
    if flask.request.method == "GET":
        return flask.jsonify(prjs)
    else:
        try:
            data = dict(flask.request.json)
        except TypeError:
            return "Gimme JSON!", 400

        name = data.get('name', None)
        description = data.get('description', None)
        if not (name and description):
            errors = {}
            if not name:
                errors['name'] = "This field is required"
            if not description:
                errors['description'] = "This field is required"
            return unprocessable(errors)

        return flask.jsonify({
            "name": name,
            "description": description
        }), 201


if __name__ == "__main__":
    APP.run(debug=True)
