from flask import Blueprint, render_template, current_app

controller = Blueprint('home', __name__)


@controller.route('/', methods=['GET'])
def index():
    print(current_app.config)
    return "working"
