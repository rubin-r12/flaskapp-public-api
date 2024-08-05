import json
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


def custom_converter(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page:': 'Home', 'Message': 'You are at HomePage', 'Time': datetime.now()}
    return json.dumps(data_set, default=custom_converter)


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))
    data_set = {'Page:': 'User', 'Message': f'At User Page. Welcome {user_query}', 'Time': datetime.now()}
    return json.dumps(data_set, default=custom_converter)


if __name__ == '__main__':
    app.run(port=5000)
