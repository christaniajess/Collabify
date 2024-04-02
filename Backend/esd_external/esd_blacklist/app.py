from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import os
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

app.config['SWAGGER'] = {
    'title': 'Blacklist Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'Manage blacklists between brand and content creators'
}
swagger = Swagger(app)

class Blacklist(db.Model):
    __tablename__ = 'blacklist'

    account = db.Column(db.String(255), primary_key=True)
    banned_account = db.Column(db.String(255), primary_key=True)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, account, banned_account,date):
        self.account = account
        self.banned_account = banned_account
        self.date=date

    def json(self):
        return {"account": self.account, "banned_account": self.banned_account, "date": self.date}

@app.route("/",methods=['get'])
def home():
    print(request.args.get("account"))
    return "Hello, this is the book service!"


@app.route("/blacklist/all")
def get_all():
    blacklist = db.session.scalars(db.select(Blacklist)).all()
    if len(blacklist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "records": [record.json() for record in blacklist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no blacklists."
        }
    ), 404


@app.route("/blacklist")
def find_by_account():
    """
    Get All Blacklist Records
    ---
    responses:
      200:
        description: Successfully retrieved all blacklist records.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  account:
                    type: string
                    description: The account ID of the user.
                  banned_account:
                    type: string
                    description: The account ID of the banned user.
                  date:
                    type: string
                    format: date-time
                    description: The date and time when the blacklist record was created.
      404:
        description: There are no blacklists found.
    """
    account = request.args.get('account')   
    print(account)
    blacklist = db.session.scalars(db.select(Blacklist).filter_by(account=account)).all()

    if blacklist:
        return jsonify(
            {
                "code": 200,
                "data": [record.json() for record in blacklist]
                
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "blacklist not found."
        }
    ), 404
    
    
@app.route("/blacklist", methods=['POST'])
def create_blacklist():
    """
    Find Blacklist Record by Account
    ---
    parameters:
      - in: query
        name: account
        required: true
        schema:
          type: string
          description: The account ID of the user for which the blacklist records are being queried.
    responses:
      200:
        description: Successfully retrieved blacklist records for the account.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  account:
                    type: string
                  banned_account:
                    type: string
                  date:
                    type: string
                    format: date-time
      404:
        description: Blacklist records not found for the specified account.
    """
    data = request.get_json()["data"]
    account = data['account']
    banned_account = data['banned_account']
    
    if (db.session.scalars(db.select(Blacklist).filter_by(account=account,banned_account=banned_account).limit(1)).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "account": account,
                    "banned_account": banned_account
                },
                "message": "Blacklist already exists."
            }
        ), 400
    blacklist = Blacklist(account,banned_account,datetime.now())


    try:
        
        db.session.add(blacklist)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "account": account,
                    "banned_account": banned_account
                },
                "message": "An error occurred creating the blacklist record."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": blacklist.json()
        }
    ), 201


@app.route("/blacklist", methods=['DELETE'])
def delete_blacklist():
    """
    Delete a Blacklist Record
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        account:
                            type: string
                            description: The account ID of the user requesting the blacklist deletion.
                        banned_account:
                            type: string
                            description: The account ID of the banned user whose record is to be deleted.
    responses:
      200:
        description: Blacklist record successfully deleted.
      404:
        description: Blacklist record not found.
    """
    data = request.get_json()
    account = data['account']
    banned_account = data['banned_account']
    blacklist = db.session.scalars(db.select(Blacklist).filter_by(account=account, banned_account=banned_account).limit(1)).first()
    if blacklist:
        db.session.delete(blacklist)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "account": account,
                    "banned_account": banned_account
                },
                "message": "Blacklist deleted."
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "account": account,
                "banned_account": banned_account
            },
            "message": "Blacklist not found."
        }
    ), 404


if __name__ == '__main__':
    print(66666)
    app.run(port=5000, debug=True, host="0.0.0.0")
