import os 

from flask import Flask, request, jsonify
from flask_cors import CORS
from os import environ
import sys
import json

app = Flask (__name__)

#switches between DB_environment and localhost depending on whether the app is running on Docker or not
db_environment = environ.get('db_environment') or 'localhost'

CORS(app)

sample_data = [
    {
        'proj_id':'1',
        'user_id':'23421',
        'proj_name':'66 Days | Change Your Life - Gymshark',
        'proj_image':'https://central.gymshark.com/article/66-days-change-your-life',
        'proj_description':'They say it takes 66 days to form a habit. We believe it takes 66 days to change your life. This is a collaboration with Gymshark where whether you want to lose weight, become president, or simply drink more water, we want you to do something you feel will change your life for the better'
    },
    {
        'proj_id':'1',
        'user_id':'23421',
        'proj_name':'Move to Zero',
        'proj_image': 'https://www.nike.com/sustainability',
        'proj_description': 'Move to Zero is a project with Nike that helps Nike’s journey towards zero carbon and zero waste, helping to protect the future of sport'
    }
]