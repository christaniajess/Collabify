import os

from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_cors import CORS
from os import environ
import sys
import json

app = Flask(__name__)
CORS(app)


#1. Invoke the Valudation Management service to get all the user information and check whether the user already has an existing project with that
#name before. 


#2. send the message 




#3. if successful, invoke the project post service posting the new created project in the database  
#4. send the message 
#5. If not succesful, send an error message with a form asking the user to enter the form again
