from invokes import invoke_http
from flask import Flask, request, jsonify
from flasgger import Swagger
import requests 
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
portNum = 5100

app.config['SWAGGER'] = {
    'title': 'Project Management Complex Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'Manage the projects of the content creator'
}
swagger = Swagger(app)

Validation_Service_URL = "http://"+os.environ.get("simpleServer")+":5003/validation" #might need to change this URL
Project_Post_Service_URL = "http://"+os.environ.get("simpleServer")+":5004/create_project" #might need to change this URL

@app.route('/health', methods =('GET', 'POST'))
def index():
    return 'all microservices are all up and running'

@app.route('/create_projects' , methods = ['POST'])
def create_projects():
    """
    Create a new project for a content creator
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        user_id:
                            type: string
                            description: The unique identifier of the content creator creating the project.
                        proj_name:
                            type: string
                            description: The name of the project. Must be unique.
                        proj_image:
                            type: string
                            description: The URL of the project's image. Optional.
                        proj_description:
                            type: string
                            description: The description of the project. Optional.
                    required:
                      - user_id
                      - proj_name
    responses:
        201:
            description: Project created successfully. Indicates that the project passed validation and was added.
        400:
            description: Missing required fields or invalid input format.
        403:
            description: Project name already exists for this user. The validation service has rejected the project name.
        500:
            description: Internal server error. Could occur during communication with the validation or project posting services.
    """
    data = request.get_json()

    #invoke the validation microservice 

    if not data or 'user_id' not in data or 'proj_name' not in data:
        return jsonify({'error': 'missing required fields'}), 400

    #these are the parameters that are needed
    user_id=data['user_id']
    proj_name=data['proj_name']

    #check if the project name is available by invoking the Validation microservice
    #this validation_response will either return 200 (if the project name is not listed yet)
    validation_response = requests.get(f"{Validation_Service_URL}/{user_id}/{proj_name}")

    if validation_response.status_code ==200:
        #this means that it passed validation -> invoke the project post microservice
        project_post_data = {
            'user_id':user_id,
            'proj_name':proj_name,
            'proj_image': data.get('proj_image',''),
            'proj_description':data.get('proj_description','')
        }
        project_post_response = requests.post(Project_Post_Service_URL + f"/{user_id}",
        json=project_post_data)

        if project_post_response.status_code == 201:
            #this part should be invoking the notification microservice
            return jsonify({'message': 'Project created succesfully!'}),201
        else:
            return jsonify({'error': 'Failed to create the project. Please try again.'}), project_post_response.status_code

    #means that didn't pass validation -> existing project name
    else:
        #means that project name already exists 
        return jsonify (validation_response.json()),validation_response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=portNum, debug=True)


