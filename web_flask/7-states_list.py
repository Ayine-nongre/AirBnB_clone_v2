#!/usr/bin/python3
"""
This is a script to start a Flask web application
"""


from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    # This function returns a list of states
    data = storage.all(State)
    data = sorted(data.values(), key=lambda data:data.name)
    return render_template('7-states_list.html', data=data)


@app.teardown_appcontext
def teardown_app():
    # This closes down the session
    storage.close()


if __name__ == "__main__":
    # This makes the app run of host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
