from flask import Blueprint, render_template, request, jsonify
from werkzeug.exceptions import BadRequest
from app import db, guard
from sqlalchemy.exc import IntegrityError
from app.models.user import User
import bcrypt

controller = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth'
)


@controller.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        return "Form submitted"
    return render_template("pages/auth/signin.html")


@controller.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        password = bcrypt.hashpw(request.form['password'], bcrypt.gensalt())

    return render_template("pages/auth/signup.html")


@controller.route('/api/signin', methods=['POST'])
def sign_in_api():
    try:
        req_data = request.get_json(force=True)
    except BadRequest as e:
        return jsonify({
            "success": False,
            "error": "Invalid request syntax"
        }), e.code

    try:
        email = req_data.get('email')
        password = req_data.get('password')
        user = guard.authenticate(email, password)
        token = guard.encode_jwt_token(user)
        parsed_token = guard.extract_jwt_token(token)
        ret = {'access_token': token, 'exp': parsed_token.get('exp'), 'rf_exp': parsed_token.get('rf_exp')}
        return jsonify(ret), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": "Internal Server Error",
        }), 500


@controller.route('/api/signup', methods=['POST'])
def sign_up_api():
    try:
        req_data = request.get_json(force=True)
    except BadRequest as e:
        return jsonify({
            "success": False,
            "error": "Invalid request syntax"
        }), e.code

    try:
        full_name = req_data.get('full_name')
        email = req_data.get('email')
        password = guard.hash_password(req_data.get('password'))
        user = User()
        try:
            user.full_name = full_name
            user.email = email
            user.password = password
            user.role = "user"
            db.session.add(user)
            db.session.flush()
            db.session.commit()
            return jsonify({
                'success': True,
                'error': "You are signup successfully."
            }), 201
        except IntegrityError as e:
            db.session.rollback()
            return jsonify({
                'success': False,
                'error': "New email is already associated with another account."
            }), 409

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": "Internal Server Error",
        }), 500


