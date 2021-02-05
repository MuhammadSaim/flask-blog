from flask import Blueprint, render_template

controller = Blueprint('home',
                       __name__,
                       url_prefix='/')


@controller.route('/', methods=['GET'])
def index():
    return render_template('pages/home.html')
