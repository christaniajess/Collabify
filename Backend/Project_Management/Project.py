import os

from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import sys
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Project(db.Model):
  __tablename__ = 'Project'
  proj_id = db.Column(db.String)
  user_id = db.Column(db.String)
  proj_name = db.Column(db.String)
  proj_image = db.Column(db.String)
  proj_description = db.Column(db.String)

def json(self):
  dto = {
    'proj_id': self.proj_id,
    'user_id': self.user_id,
    'proj_name': self.proj_name,
    'proj_image': self.proj_image,
    'proj_description': self.proj_description


#1. Invoke the Valudation Management service to get all the user information and check whether the user already has an existing project with that
#name before. 


#2. send the message 




#3. if successful, invoke the project post service posting the new created project in the database  
#4. send the message 
#5. If not succesful, send an error message with a form asking the user to enter the form again
