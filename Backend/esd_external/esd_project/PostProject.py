from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import logging
# import traceback
from os import environ
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
portNumber = 5000
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
#'mysql+mysqlconnector://root:root@localhost:3306/project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

app.config['SWAGGER'] = {
    'title': 'Project Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'Manage projects of content creators'
}
swagger = Swagger(app)

class Project(db.Model):
    __tablename__ = 'project'

    proj_id = db.Column(db.Integer, primary_key =True, autoincrement=True)
    user_id = db.Column(db.Text)
    proj_name = db.Column(db.Text)
    proj_image = db.Column(db.Text)
    proj_description = db.Column(db.Text)

    def __init__(self, user_id, proj_name, proj_image, proj_description):
        self.user_id = user_id
        self.proj_name = proj_name
        self.proj_image = proj_image
        self.proj_description = proj_description

    def json(self):
        return {
            "proj_id": self.proj_id, "user_id": self.user_id, "proj_name": self.proj_name,
            "proj_image": self.proj_image, "proj_description": self.proj_description
        }

#creating a new project (this is after the have passed validation as this microservice is only invoked after it has passed validation)
@app.route('/create_project/<string:user_id>', methods=['POST'])
def create_project(user_id):
    """
    Create a project
    ---
    parameters:
      - in: path
        name: user_id
        required: true
        schema:
          type: string
        description: The unique identifier of the user creating the project.
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              proj_name:
                type: string
                description: The name of the project.
              proj_image:
                type: string
                description: URL to the project's representative image.
              proj_description:
                type: string
                description: Detailed description of the project.
    responses:
      201:
        description: Project created successfully. Returns the created project details.
        content:
          application/json:
            schema:
              type: object
              properties:
                user_id:
                  type: string
                proj_name:
                  type: string
                proj_image:
                  type: string
                proj_description:
                  type: string
      500:
        description: An error occurred while creating the project.
    """
    data = request.get_json()
    project = Project(user_id=user_id, proj_name=data.get('proj_name'), proj_image=data.get('proj_image'), proj_description=data.get('proj_description'))

    try:
        db.session.add(project)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                'code': 500,
                'data': {
                    'user_id': user_id,
                },
                'message': 'An error occurred while creating the project.'
            }
        ), 500

    return jsonify(
        {
            'code': 201,
            'data': {
                'user_id': user_id,
                'proj_name': project.proj_name,
                'proj_image': project.proj_image,
                'proj_description': project.proj_description
            },
            'message': 'Project created successfully!'
        }
    ), 201

#if user wants to edit after they created a new project (they cannot change project name!!)
@app.route('/update_project', methods =['PUT'])
def update_project():
    """
    Update a project
    ---
    parameters:
      - in: path
        name: user_id
        required: true
        schema:
          type: string
        description: The user ID of the project owner.
      - in: path
        name: proj_name
        required: true
        schema:
          type: string
        description: The name of the project to update.
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              proj_image:
                type: string
                description: Updated URL to the project's image.
              proj_description:
                type: string
                description: Updated project description.
    responses:
      200:
        description: Project updated successfully.
      404:
        description: Project not found.
      500:
        description: An error occurred while updating the project.
    """
    data = request.json
    user_id = data.get('user_id')
    proj_name = data.get('proj_name')
    # proj_image = data.get('proj_image')
    proj_description = data.get('proj_description')

    try:
        project = Project.query.filter_by(user_id=user_id, proj_name=proj_name).first()

        if not project:
            return jsonify({
                'code': 404,
                'message': 'Project not found.'
            }), 404

        # Update project attributes
        # project.proj_image = proj_image
        project.proj_description = proj_description

        db.session.commit()

        return jsonify({
            'code': 200,
            'message': 'Project updated successfully!'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': 'An error occurred while updating the project.'
        }), 500


#deletion of the project
@app.route('/delete_project/<string:user_id>/<string:proj_name>', methods=['DELETE'])
def delete_project(user_id, proj_name):
    """
    Delete a project
    ---
    parameters:
      - in: path
        name: user_id
        required: true
        schema:
          type: string
        description: The user ID of the project owner.
      - in: path
        name: proj_name
        required: true
        schema:
          type: string
        description: The name of the project to be deleted.
    responses:
      200:
        description: Project deleted successfully.
      404:
        description: Project not found.
      500:
        description: An error occurred while deleting the project.
    """
    logging.info(f"Deleting project: {proj_name} for user: {user_id}")
    try:
        project = Project.query.filter_by(user_id=user_id, proj_name=proj_name).first()

        if not project:
            return jsonify({
                'code': 404,
                'message': 'Project not found.'
            }), 404

        db.session.delete(project)
        db.session.commit()

        return jsonify({
            'code': 200,
            'message': 'Project deleted successfully!'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': 'An error occurred while deleting the project.'
        }), 500


@app.route('/get_all_project', methods=['GET'])
def get_all_project():
    """
    Get all projects
    ---
    responses:
      200:
        description: A list of all projects.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  proj_id:
                    type: integer
                  user_id:
                    type: string
                  proj_name:
                    type: string
                  proj_image:
                    type: string
                  proj_description:
                    type: string
      404:
        description: No projects found.
      500:
        description: An error occurred while retrieving projects.
    """
    try:
        project = Project.query.all()
        project_list = []
        for project in project:
            project_data = {
                'proj_id': project.proj_id,
                'user_id': project.user_id,
                'proj_name': project.proj_name,
                'proj_image': project.proj_image,
                'proj_description': project.proj_description
            }
            project_list.append(project_data)
        
        if len(project_list):
            return jsonify(
                {
                    'code':200,
                    'data': project_list
                }
            )

        return jsonify(
            {
                'code':404,
                'message': 'There are no project yet'
            }
        )

    
    except Exception as e:  # Catch all exceptions
        traceback.print_exc()  # Print traceback to console just to see what's wrong 
        return jsonify(
            {
                'code':500,
                'message': 'An error occurred while retrieving project.'
            }
        ), 500


@app.route('/get_project', methods=['GET'])
def get_project():
    """
    Get projects by content creator ID
    ---
    parameters:
      - in: query
        name: cc_id
        schema:
          type: string
        required: true
        description: The content creator ID to retrieve projects for.
    responses:
      200:
        description: A list of projects for the given content creator ID.
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  proj_id:
                    type: integer
                  user_id:
                    type: string
                  proj_name:
                    type: string
                  proj_image:
                    type: string
                  proj_description:
                    type: string
      404:
        description: No projects found for the given content creator ID.
      500:
        description: An error occurred while retrieving projects.
    """
    try:
        cc_id = request.args.get("cc_id")
        project = Project.query.filter_by(user_id=cc_id).all()
        project_list = []
        for project in project:
            project_data = {
                'proj_id': project.proj_id,
                'user_id': project.user_id,
                'proj_name': project.proj_name,
                'proj_image': project.proj_image,
                'proj_description': project.proj_description
            }
            project_list.append(project_data)

        if len(project_list):
            return jsonify(
                {
                    'code': 200,
                    'data': project_list
                }
            )
        return jsonify(
            {
                'code': 404,
                'data': 'There are no projects for the given cc_id',
            }
        )

    
    except Exception as e:  # Catch all exceptions
        traceback.print_exc()  # Print traceback to console just to see what's wrong 
        return jsonify(
            {
                'code':500,
                'message': 'An error occurred while retrieving project.'
            }
        ), 500

  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = portNumber, debug=True)