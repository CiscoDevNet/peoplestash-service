import string
from functools import wraps
import requests
import json

from flask import Flask, jsonify, abort, make_response, request, Response

app = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/leankit/cards', methods=['GET'])
@requires_auth
def get_cards():
    print ("in get cards12")
    # enter your leankit username and password
    replyData = requests.get("https://cisco1787.leankit.com/kanban/api/boards/333122750", auth=('user', 'password'))
    r_json = replyData.json()
    # print (json.dumps(r_json, indent=4, separators=(',', ': ')))
    cards = r_json["ReplyData"][0]["Lanes"][0]["Cards"]
    print (json.dumps(cards, indent=4, separators=(',', ': ')))
    return jsonify({'cards': cards})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run()