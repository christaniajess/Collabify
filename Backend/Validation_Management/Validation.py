#Validation should be making sure that the user doesn't have the same project name, if they do send error

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
portNumber = 5003
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
#'mysql+mysqlconnector://root:root@localhost:3306/Projects'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

#creating a new class
class Project(db.Model):
    __tablename__ = 'projects'

    proj_id = db.Column(db.Integer, primary_key =True, autoincrement=True)
    user_id = db.Column(db.Text)
    proj_name = db.Column(db.Text)
    proj_image = db.Column(db.Text)
    proj_description = db.Column(db.Text)


#function to validate whether user's input is ok (mainly checking whether there is already the same project name in the 
# database)
@app.route('/validation/<string:user_id>/<string:proj_name>', methods = ['GET'])
def validation(user_id, proj_name):
    existing_project = db.session.scalars(db.select(Project).filter_by(user_id=user_id, proj_name=proj_name)).first()
    if existing_project:
        return jsonify(
            {
                'code': 400,
                'data': {
                    'user_id': user_id,
                    'proj_name': proj_name
                },
                'message': 'Project with the same name already exists for this user. Please choose a different name.'
            }
        ), 400

    return jsonify(
        {
            'code': 200,
            'message': 'Project name is available. You can proceed with the rest of the process.'
        }
    ), 200


            
#function to get all the projects
# @app.route('/get_all_projects', methods=['GET'])
# def get_all_projects():
#     try:
#         projects = Project.query.all()
#         project_list = []
#         for project in projects:
#             project_data = {
#                 'proj_id': project.proj_id,
#                 'user_id': project.user_id,
#                 'proj_name': project.proj_name,
#                 'proj_image': project.proj_image,
#                 'proj_description': project.proj_description
#             }
#             project_list.append(project_data)
        
#         if len(project_list):
#             return jsonify(
#                 {
#                     'code':200,
#                     'data': project_list
#                 }
#             )

#         return jsonify(
#             {
#                 'code':404,
#                 'message': 'There are no projects yet'
#             }
#         )

    
#     except Exception as e:  # Catch all exceptions
#         traceback.print_exc()  # Print traceback to console just to see what's wrong 
#         return jsonify(
#             {
#                 'code':500,
#                 'message': 'An error occurred while retrieving projects.'
#             }
#         ), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=portNumber, debug=True)