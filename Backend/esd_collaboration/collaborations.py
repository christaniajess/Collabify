import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/collaborations'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)


class collaborations(db.Model):
    __tablename__ = 'collaborations'

    cc_id = db.Column(db.VARCHAR(100), nullable=True,primary_key=True)
    brand_id = db.Column(db.VARCHAR(100), nullable=True,primary_key=True)
    collab_title = db.Column(db.String(20), nullable=True,)
    collab_status = db.Column(db.String(20), nullable=True,)

    def json(self):
        dto = {
            'cc_id': self.cc_id,
            'brand_id': self.brand_id,
            'collab_title': self.collab_title,
            'collab_status': self.collab_status
        }
        
        return dto

# View All Collaborations
@app.route("/collaborations")
def get_all():
    collablist = db.session.scalars(db.select(collaborations)).all()
    if len(collablist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "collaborations": [collaborations.json() for collaborations in collablist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no collaborations."
        }
    ), 404

#View by Content Creator
@app.route("/collaborations/cc/<int:cc_id>")
def find_by_cc(cc_id):
    collabs = db.session.scalars(
        db.select(collaborations).filter_by(cc_id=cc_id).limit(1)).first()
    if collabs:
        return jsonify(
            {
                "code": 200,
                "data": collabs.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "cc_id": cc_id
            },
            "message": "Collaboration not found."
        }
    ), 404

# View by Status
@app.route("/collaborations/status/<string:collab_status>")
def find_by_collab_status(collab_status):
    collabs = db.session.scalars(
        db.select(collaborations).filter_by(collab_status=collab_status).limit(1)).first()
    if collabs:
        return jsonify(
            {
                "code": 200,
                "data": collabs.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "collab_status": collab_status
            },
            "message": "Collaboration not found."
        }
    ), 404

# View by Brand
@app.route("/collaborations/brand/<int:brand_id>")
def find_by_brand(brand_id):
    collabs = db.session.scalars(
        db.select(collaborations).filter_by(brand_id=brand_id).limit(1)).first()
    if collabs:
        return jsonify(
            {
                "code": 200,
                "data": collabs.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "brand_id": brand_id
            },
            "message": "Collaboration not found."
        }
    ), 404

# Create a Collaboration
@app.route("/collaborations", methods=["POST"])
def create_collaboration():
    try: 
        data = request.get_json()
        new_collaboration = collaborations(
            cc_id=data["cc_id"],
            brand_id=data["brand_id"],
            collab_title=data["collab_title"],
            collab_status=data["collab_status"],
        )
        db.session.add(new_collaboration)
        db.session.commit()
        return jsonify(
            {
                "code": 201,
                "data": new_collaboration.json(),
                "message": "Collaboration successfully added."
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating collaboration. " + str(e)
            }
        ), 500

# Update Collaboration Status
@app.route("/collaborations/cc/<int:cc_id>", methods=["PUT"])
def update_collaboration_status(cc_id):
    collabs = db.session.scalars(
        db.select(collaborations).filter_by(cc_id=cc_id).limit(1)).first()
    if collabs:
        try:
            collabs.collab_status = request.json["collab_status"]
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": collabs.json(),
                    "message": "Collaboration status updated successfully."
                }
            )
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred while updating status. " + str(e)
                }
            ), 500
    else:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "cc_id": cc_id
                },
                "message": "Collaboration not found."
            }
        ), 404



if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": managing collabrations ...")
    app.run(host='0.0.0.0', port=5003, debug=True)
