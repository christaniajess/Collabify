from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

@app.route("/")
def home():
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
    account = request.args.get('account')
    banned_account = request.args.get('banned_account')
    blacklist = db.session.scalars(db.select(Blacklist).filter_by(account=account, banned_account=banned_account)).all()

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
    print(request.get_json())
    data = request.get_json()
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
