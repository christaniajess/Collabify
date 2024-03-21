from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SWAGGER'] = {
    'title': 'Account Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'Manage user accounts'
}
swagger = Swagger(app)

class User(db.Model):
    __tablename__= "account"
    user_id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.Text)
    acc_type = db.Column(db.Text)
    full_name = db.Column(db.Text)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    user_photo = db.Column(db.Text)
    interests = db.Column(db.Text)

# Function to get all users and their details
@app.route('/users', methods=['GET'])
def list_users():
    """
    List all users
    ---
    responses:
        200:
            description: A list of users
            content:
                application/json:
                    schema:
                        type: array
                        items:
                            type: object
                            properties:
                                user_id:
                                    type: integer
                                    description: The unique identifier for a user
                                username:
                                    type: string
                                    description: User's chosen username
                                acc_type:
                                    type: string
                                    description: Account type
                                full_name:
                                    type: string
                                    description: User's full name
                                email:
                                    type: string
                                    description: User's email address
                                user_photo:
                                    type: string
                                    description: URL to user's photo
                                interests:
                                    type: string
                                    description: User's interests
        500:
            description: Internal Server Error
    """
    try:
        users = User.query.all()
        user_list = []
        for user in users:
            user_data = {
                'user_id': user.user_id,
                'username': user.username,
                'acc_type': user.acc_type,
                'full_name': user.full_name,
                'email': user.email,
                'user_photo': user.user_photo,
                'interests': user.interests
            }
            user_list.append(user_data)
        return jsonify(
            {
                'code': 200,
                'data': user_list
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'message': f'Internal Server Error: {str(e)}'
            }
        ), 500


@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        user_id:
                            type: integer
                            description: The unique identifier for a user                                        
                        username:
                            type: string
                            description: User's chosen username
                        acc_type:
                            type: string
                            description: Account type (e.g., admin, standard user)
                        full_name:
                            type: string
                            description: User's full name
                        email:
                            type: string
                            description: User's email address
                        password:
                            type: string
                            description: User's password
                        user_photo:
                            type: string
                            description: URL to user's photo
                        interests:
                            type: string
                            description: User's interests
    responses:
        201:
            description: Account created successfully
        409:
            description: Email already exists
    """
    data = request.json

    user_id = data.get('user_id')
    username = data.get('username')
    acc_type = data.get('acc_type')
    full_name = data.get('full_name')
    email = data.get('email')
    password = generate_password_hash(data.get('password'))  # Hashing the password
    user_photo = data.get('user_photo')
    interests = data.get('interests')

    try:
        new_user = User(
            user_id=user_id,
            username=username,
            acc_type=acc_type,
            full_name=full_name,
            email=email,
            password=password,
            user_photo=user_photo,
            interests=interests
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify(
            {
                'code': 201,
                'message': 'Account set up successfully!'
            }
        ), 201
    except IntegrityError:
        # Handling the case where the email already exists
        db.session.rollback()
        return jsonify(
            {
                'code': 409,
                'message': 'Email already exists. Please choose a different email.'
            }
        ), 409

# Function to update user details
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user's details
    ---
    parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
            description: The unique identifier for a user
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        username:
                            type: string
                            description: User's chosen username
                        acc_type:
                            type: string
                            description: Account type
                        full_name:
                            type: string
                            description: User's full name
                        email:
                            type: string
                            description: User's email address
                        user_photo:
                            type: string
                            description: URL to user's photo
                        interests:
                            type: string
                            description: User's interests
    responses:
        200:
            description: User details updated successfully
        404:
            description: User not found
    """
    try:
        user = User.query.get_or_404(user_id)
        data = request.json

        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()

        return jsonify(
            {
                'code': 200,
                'message': 'User details updated successfully'
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'code': 404,
                'data': 'User not found',
                'message': f'User not found: {str(e)}'
            }
        ), 404

# Function to delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user
    ---
    parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
            description: The unique identifier for a user
    responses:
        200:
            description: User deleted successfully
        404:
            description: User not found
    """
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify(
            {
                'code': 200,
                'message': 'User deleted successfully'
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'code': 404,
                'data': 'User not found',
                'message': f'User not found: {str(e)}'
            }
        ), 404

# Function to get user details by user_id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a single user's details
    ---
    parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
            description: The unique identifier for a user
    responses:
        200:
            description: User details retrieved successfully
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            user_id:
                                type: integer
                                description: The unique identifier for a user
                            username:
                                type: string
                                description: User's chosen username
                            acc_type:
                                type: string
                                description: Account type
                            full_name:
                                type: string
                                description: User's full name
                            email:
                                type: string
                                description: User's email address
                            user_photo:
                                type: string
                                description: URL to user's photo
                            interests:
                                type: string
                                description: User's interests
        404:
            description: User not found
    """
    print('FINDING USER!')
    try:
        user = User.query.get_or_404(user_id)
        user_data = {
            'user_id': user.user_id,
            'username': user.username,
            'acc_type': user.acc_type,
            'full_name': user.full_name,
            'email': user.email,
            'user_photo': user.user_photo,
            'interests': user.interests
        }
        return jsonify(
            {
                'code': 200,
                'data': user_data
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'code': 404,
                'data': 'User not found',
                'message': f'User not found: {str(e)}'
            }
        ), 404

# Function to get users by interests
@app.route('/users/interests/<string:interests>', methods=['GET'])
def get_users_by_interests(interests):
    """
    Get users by interests
    ---
    parameters:
        - in: path
          name: interests
          required: true
          schema:
            type: string
            description: User interests to filter by
    responses:
        200:
            description: Users filtered by interests
            content:
                application/json:
                    schema:
                        type: array
                        items:
                            type: object
                            properties:
                                user_id:
                                    type: integer
                                    description: The unique identifier for a user
                                username:
                                    type: string
                                    description: User's chosen username
                                acc_type:
                                    type: string
                                    description: Account type
                                full_name:
                                    type: string
                                    description: User's full name
                                email:
                                    type: string
                                    description: User's email address
                                user_photo:
                                    type: string
                                    description: URL to user's photo
                                interests:
                                    type: string
                                    description: User's interests
        500:
            description: Internal Server Error
    """
    try:
        interest_list = interests.split(",")
        print(interest_list)
        user_list = []
        for interest in interest_list:
            users = User.query.filter(User.interests.ilike(f'%{interest}%')).all()
            for user in users:
                user_data = {
                    'user_id': user.user_id,
                    'username': user.username,
                    'acc_type': user.acc_type,
                    'full_name': user.full_name,
                    'email': user.email,
                    'user_photo': user.user_photo,
                    'interests': user.interests
                }
                if user_data not in user_list:
                    user_list.append(user_data)
        return jsonify(
            {
                'code': 200,
                'data': user_list
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'message': f'Internal Server Error: {str(e)}'
            }
        ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
