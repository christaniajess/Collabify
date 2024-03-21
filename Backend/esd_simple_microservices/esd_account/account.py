from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
@app.route('/get_all_users', methods=['GET'])
def get_all_users():
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


@app.route('/setup_account', methods=['POST'])
def setup_account():
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
@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
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
                'message': f'User not found: {str(e)}'
            }
        ), 404

# Function to delete user
@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
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
                'message': f'User not found: {str(e)}'
            }
        ), 404

# Function to get user details by user_id
@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
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
                'message': f'User not found: {str(e)}'
            }
        ), 404

# Function to get users by interests
@app.route('/get_users_by_interests/<string:interests>', methods=['GET'])
def get_users_by_interests(interests):
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
