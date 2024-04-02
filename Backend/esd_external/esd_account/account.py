from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
import os
from flask_cors import CORS
from flask import jsonify


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost:3306/account"

      

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)
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
    stripe_key = db.Column(db.Text)

# Function to get all users and their details
@app.route('/all_users', methods=['GET'])
def list_users():
    """
    List All Users
    ---
    responses:
      200:
        description: Successfully retrieved all users.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  user_id:
                    type: integer
                    description: The unique identifier of the user.
                  username:
                    type: string
                    description: The username of the user.
                  acc_type:
                    type: string
                    description: The account type of the user.
                  full_name:
                    type: string
                    description: The full name of the user.
                  email:
                    type: string
                    description: The email address of the user.
                  user_photo:
                    type: string
                    description: The URL to the user's photo.
                  interests:
                    type: string
                    description: The interests of the user.
      500:
        description: An internal server error occurred while fetching user data.
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
                'interests': user.interests,
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
    Create New User
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        username:
                            type: string
                            description: The user's chosen username.
                        acc_type:
                            type: string
                            description: The user's account type.
                        full_name:
                            type: string
                            description: The user's full name.
                        email:
                            type: string
                            description: The user's email address.
                        password:
                            type: string
                            description: The user's password.
                        user_photo:
                            type: string
                            description: URL of the user's photo.
                        interests:
                            type: string
                            description: The user's interests.
    responses:
      201:
        description: User successfully created.
      409:
        description: Email already exists.
      500:
        description: Internal server error occurred while creating the user.
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
    Update User Details
    ---
    parameters:
      - in: path
        name: user_id
        required: true
        schema:
          type: integer
          description: The unique identifier of the user to update.
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        username:
                            type: string
                            description: New username of the user.
                        acc_type:
                            type: string
                            description: New account type of the user.
                        full_name:
                            type: string
                            description: New full name of the user.
                        email:
                            type: string
                            description: New email address of the user.
                        user_photo:
                            type: string
                            description: New URL of the user's photo.
                        interests:
                            type: string
                            description: New interests of the user.
    responses:
      200:
        description: User details updated successfully.
      404:
        description: User not found.
      500:
        description: Internal server error.
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
    Delete User
    ---
    parameters:
      - in: path
        name: user_id
        required: true
        schema:
          type: integer
          description: The unique identifier of the user to be deleted.
    responses:
      200:
        description: User deleted successfully.
      404:
        description: User not found.
      500:
        description: Internal server error occurred while attempting to delete the user.
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
@app.route('/users', methods=['GET'])
def get_user():
    """
    Get User Details by User ID
    ---
    parameters:
      - in: query
        name: user_id
        required: true
        schema:
          type: string
          description: The unique identifier of the user whose details are to be retrieved.
    responses:
      200:
        description: Successfully retrieved user details.
        content:
          application/json:
            schema:
                type: object
                properties:
                    user_id:
                        type: integer
                        description: The unique identifier of the user.
                    username:
                        type: string
                        description: The username of the user.
                    acc_type:
                        type: string
                        description: The account type of the user.
                    full_name:
                        type: string
                        description: The full name of the user.
                    email:
                        type: string
                        description: The email address of the user.
                    user_photo:
                        type: string
                        description: The URL to the user's photo.
                    interests:
                        type: string
                        description: The interests of the user.
      404:
        description: User not found.
      500:
        description: Internal server error occurred while attempting to retrieve the user's details.
    """
    print('FINDING USER!')
    user_id=request.args.get("user_id")
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
    Get Users by Interests
    ---
    parameters:
      - in: path
        name: interests
        required: true
        schema:
          type: string
          description: The interests by which to filter users.
    responses:
      200:
        description: Successfully retrieved users with specified interests.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                    user_id:
                        type: integer
                        description: The unique identifier of the user.
                    username:
                        type: string
                        description: The username of the user.
                    acc_type:
                        type: string
                        description: The account type of the user.
                    full_name:
                        type: string
                        description: The full name of the user.
                    email:
                        type: string
                        description: The email address of the user.
                    user_photo:
                        type: string
                        description: The URL to the user's photo.
                    interests:
                        type: string
                        description: The interests of the user.
      500:
        description: Internal server error occurred while attempting to retrieve users by interests.
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

@app.route('/user/payment', methods=['GET'])
def get_user_payment_info():
    """
    Get User Payment Information
    ---
    parameters:
      - in: query
        name: user_id
        required: true
        schema:
          type: string
          description: The unique identifier of the user whose payment information is to be retrieved.
    responses:
      200:
        description: Successfully retrieved user payment information.
        content:
          application/json:
            schema:
                type: object
                properties:
                    user_id:
                        type: integer
                        description: The unique identifier of the user.
                    stripe_key:
                        type: string
                        description: The Stripe key associated with the user.
      404:
        description: User not found.
      500:
        description: Internal server error occurred while attempting to retrieve the user's payment information.
    """
    user_id=request.args.get("user_id")
    print(user_id)
    try:
        user = User.query.filter_by(user_id=str(user_id)).first()
        if user:
            return jsonify({
                'code': 200,
                'data': {
                    'user_id': user.user_id,
                    'stripe_key': user.stripe_key
                }
            }), 200
        else:
            return jsonify({
                'code': 404,
                'message': 'User not found'
            }), 404
            
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'message': f'Internal Server Error: {str(e)}'
            }
        ), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
