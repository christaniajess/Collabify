from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import traceback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/Projects'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = 'projects'

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

@app.route('/get_all_projects', methods=['GET'])
def get_all_projects():
    try:
        projects = Project.query.all()
        project_list = []
        for project in projects:
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
                'message': 'There are no projects yet'
            }
        )

    
    except Exception as e:  # Catch all exceptions
        traceback.print_exc()  # Print traceback to console just to see what's wrong 
        return jsonify(
            {
                'code':500,
                'message': 'An error occurred while retrieving projects.'
            }
        ), 500

#creating a new project (this is after the have passed validation as this microservice is only invoked after it has passed validation)
@app.route('/create_project/<string:user_id>', methods=['POST'])
def create_project(user_id):
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
@app.route('/update_project/<string:user_id>/<string:proj_name>', methods =['PUT'])
def update_project(user_id,proj_name):

    data = request.json

    proj_image = data.get('proj_image')
    proj_description = data.get('proj_description')

    try:
        project = Project.query.filter_by(user_id=user_id, proj_name=proj_name).first()

        if not project:
            return jsonify({
                'code': 404,
                'message': 'Project not found.'
            }), 404

        # Update project attributes
        project.proj_image = proj_image
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

  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)