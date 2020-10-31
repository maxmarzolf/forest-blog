import flask
from flask import render_template


blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET'])
def show_homepage():
    return render_template('pages/home.html')
