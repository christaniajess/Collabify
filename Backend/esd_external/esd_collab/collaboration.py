import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost:3306/collaboration"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

CORS(app)

db = SQLAlchemy(app)

app.config['SWAGGER'] = {
    'title': 'Collaboration Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'Manage collaborations between brands and content creators'
}
swagger = Swagger(app)


class Collaboration(db.Model):
    __tablename__ = 'collaboration'

    cc_id = db.Column(db.VARCHAR(100), nullable=True,primary_key=True)
    brand_id = db.Column(db.VARCHAR(100), nullable=True,primary_key=True)
    collab_title = db.Column(db.String(20), nullable=True,primary_key=True)
    collab_status = db.Column(db.String(20), nullable=True,)

    def json(self):
        dto = {
            'cc_id': self.cc_id,
            'brand_id': self.brand_id,
            'collab_title': self.collab_title,
            'collab_status': self.collab_status
        }
        
        return dto

# View All Collaboration
@app.route("/collaborations", methods=['GET'])
def get_all_collaborations():
    """
    List All Collaborations
    ---
    responses:
      200:
        description: Successfully retrieved a list of all collaborations.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  cc_id:
                    type: string
                    description: The unique identifier of the content creator.
                  brand_id:
                    type: string
                    description: The unique identifier of the brand.
                  collab_title:
                    type: string
                    description: The title of the collaboration.
                  collab_status:
                    type: string
                    description: The current status of the collaboration.
      404:
        description: No collaborations found.
    """
    collaboration_list = db.session.scalars(db.select(Collaboration)).all()
    if len(collaboration_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "collaboration": [collaboration.json() for collaboration in collaboration_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no collaboration."
        }
    ), 404

#View by Content Creator
@app.route("/collaborations/cc/<string:cc_id>", methods=['GET'])
def get_collaborations_by_cc(cc_id):
    """
    Get Collaborations by Content Creator ID
    ---
    parameters:
      - in: path
        name: cc_id
        required: true
        schema:
          type: string
          description: The unique identifier of the content creator whose collaborations are being queried.
    responses:
      200:
        description: Successfully retrieved collaborations for the specified content creator.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  cc_id:
                    type: string
                  brand_id:
                    type: string
                  collab_title:
                    type: string
                  collab_status:
                    type: string
      404:
        description: Collaborations not found for the specified content creator.
    """
    collaborations = db.session.scalars(
        db.select(Collaboration).filter_by(cc_id=cc_id)).all()
    print(collaborations)
    
    if collaborations:
        return jsonify(
            {
                "code": 200,
                "data": [collaboration.json() for collaboration in collaborations]
            }

        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "cc_id": cc_id,
                "message": "Collaboration not found."
            },
            "message": "Collaboration not found."
        }
    ), 404

# View by Status
@app.route("/collaborations/status/<string:collab_status>", methods=["GET"])
def get_collaboration_by_status(collab_status):
    """
    Get Collaborations by Status
    ---
    parameters:
      - in: path
        name: collab_status
        required: true
        schema:
          type: string
          description: The status to filter collaborations by.
    responses:
      200:
        description: Successfully retrieved collaborations with the specified status.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  cc_id:
                    type: string
                  brand_id:
                    type: string
                  collab_title:
                    type: string
                  collab_status:
                    type: string
      404:
        description: No collaborations found with the specified status.
    """
    collabs = db.session.scalars(
        db.select(Collaboration).filter_by(collab_status=collab_status)).all()
    if collabs:
        return jsonify(
            {
                "code": 200,
                "data": [collaboration.json() for collaboration in collabs]
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "collab_status": collab_status,
                "message": "Collaboration not found."
            },
            "message": "Collaboration not found."
        }
    ), 404

# View by Brand
@app.route("/collaborations/brand/<string:brand_id>", methods=["GET"])
def get_collaboration_by_brand(brand_id):
    """
    Get Collaboration by Brand ID
    ---
    parameters:
      - in: path
        name: brand_id
        required: true
        schema:
          type: string
          description: The unique identifier of the brand whose collaborations are being queried.
    responses:
      200:
        description: Successfully retrieved collaborations for the specified brand.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  cc_id:
                    type: string
                  brand_id:
                    type: string
                  collab_title:
                    type: string
                  collab_status:
                    type: string
      404:
        description: Collaborations not found for the specified brand.
    """
    collabs = db.session.scalars(
        db.select(Collaboration).filter_by(brand_id=brand_id)).all()
    if collabs:
        return jsonify(
            {
                "code": 200,
                "data": [collaboration.json() for collaboration in collabs]

            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "brand_id": brand_id,
                "message": "Collaboration not found."
            },
            "message": "Collaboration not found."
        }
    ), 404

# Create a Collaboration
@app.route("/collaborations", methods=["POST"])
def create_collaboration():
    """
    Create a New Collaboration
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        cc_id:
                            type: string
                            description: The unique identifier of the content creator.
                        brand_id:
                            type: string
                            description: The unique identifier of the brand.
                        collab_title:
                            type: string
                            description: The title of the collaboration.
                        collab_status:
                            type: string
                            description: The initial status of the collaboration.
    responses:
      201:
        description: Collaboration created successfully.
      500:
        description: An error occurred while creating the collaboration.
    """
    try: 
        data = request.get_json()
        new_collaboration = Collaboration(
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
@app.route("/collaborations/status", methods=["PUT"])
def update_collaboration_status():
    """
    Update Collaboration Status
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        cc_id:
                            type: string
                            description: The unique identifier of the content creator involved in the collaboration.
                        brand_id:
                            type: string
                            description: The unique identifier of the brand involved in the collaboration.
                        collab_status:
                            type: string
                            description: The new status of the collaboration.
    responses:
      200:
        description: Collaboration status updated successfully.
      404:
        description: Collaboration not found.
      500:
        description: An error occurred while updating the collaboration status.
    """
    data=request.get_json()
    print(data)
    collabs = db.session.scalars(
        db.select(Collaboration).filter_by(cc_id=data["cc_id"],brand_id=data["brand_id"])).first()
    if collabs:
        try:
            collabs.collab_status = data["collab_status"]
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
                    "cc_id": data["cc_id"],
                     "message": "Collaboration not found."
                },
                "message": "Collaboration not found."
            }
        ), 404



# Remove Collaboration
@app.route("/collaborations", methods=["DELETE"])
def remove_collaboration():
    """
    Remove Collaboration
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        cc_id:
                            type: string
                            description: The unique identifier of the content creator involved in the collaboration.
                        brand_id:
                            type: string
                            description: The unique identifier of the brand involved in the collaboration.
    responses:
      200:
        description: Collaboration removed successfully.
      404:
        description: Collaboration not found.
    """
    cc_id = request.json["cc_id"]
    brand_id=request.json["brand_id"]
    
    
    
    collaboration = db.session.scalars(
        db.select(Collaboration).filter_by(cc_id=cc_id, brand_id=brand_id)).first()
    if collaboration:
        db.session.delete(collaboration)
        db.session.commit()
        return jsonify(message="Collaboration removed successfully"), 200
    else:
        return jsonify(message="Collaboration not found"), 404






if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": managing collabrations ...")
    app.run(host='0.0.0.0', port=5000, debug=True)
