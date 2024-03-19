from invokes import invoke_http
from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)
portNum = 5005

Validation_Service_URL = 'http://localhost:5003/validation' #might need to change this URL
Project_Post_Service_URL = 'http://localhost:5004/create_project' #might need to change this URL

@app.route('/health', methods =('GET', 'POST'))
def index():
    return 'all microservices are all up and running'

@app.route('/create_projects' , methods = ['POST'])
def create_projects():
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


