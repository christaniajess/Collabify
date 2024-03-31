from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

app.config['SWAGGER'] = {
    'title': 'View Profile Complex Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'View content creator profiles'
}
swagger = Swagger(app)

ACCOUNT_URL = "http://host.docker.internal:3000"
COLLAB_URL = "http://host.docker.internal:3001/collaborations"
REVIEW_URL = "http://"+os.environ.get("internalService")+":3002"
PROJECT_URL = "http://host.docker.internal:3003/"
ERROR_URL = "http://host.docker.internal:5005/error"


@app.route("/profile", methods=['GET'])
def get_profile():
    """
    Get a Comprehensive Profile View
    ---
    parameters:
      - in: requestBody
        name: cc_id
        required: true
        schema:
          type: object
          properties:
            cc_id:
              type: integer
          description: The unique identifier of the content creator for whom the profile is fetched.
    responses:
      200:
        description: Successfully retrieved the comprehensive profile view, including account details, collaborations, reviews, and projects.
        content:
          application/json:
            schema:
              type: object
              properties:
                account:
                  type: object
                  description: Account details of the content creator.
                  properties:
                    user_id:
                      type: integer
                      description: The unique identifier of the content creator.
                    username:
                      type: string
                      description: The username of the content creator.
                    # Additional account properties...
                collab:
                  type: array
                  description: A list of collaborations associated with the content creator.
                  items:
                    type: object
                    # Define the schema for a single collaboration...
                review:
                  type: array
                  description: A list of reviews given to the content creator.
                  items:
                    type: object
                    # Define the schema for a single review...
                project:
                  type: array
                  description: A list of projects created by the content creator.
                  items:
                    type: object
                    # Define the schema for a single project...
      400:
        description: Invalid JSON input or missing required query parameter `cc_id`.
      500:
        description: Internal server error or unable to fetch from external services.
    """
    # Simple check of input format and data of the request are JSON
    try:
      
        details = request.args
        print(details)
        print("\nReceived a profile in JSON:", details) # Details provided is the id of the requested user in json format

        # Get all the relevant details of the user
        result = get_profile_data(details)
        return jsonify(result), result["code"]

    except Exception as e:
        # Unexpected error in code
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
        print(ex_str)

        return jsonify({
            "code": 500,
            "message": "complex_viewProfile.py internal error: " + ex_str
        }), 500




def get_profile_data(details):
    # Collect Account details
    # Invoke Account Microservice
    print('\n-----Invoking account microservice-----')
    account_result = invoke_http(ACCOUNT_URL+"/users?user_id="+str(details['cc_id']), method='GET', json=details)
    print('account_result:', account_result)

    code = account_result["code"]
    if code != 404:
      if code not in range(200, 300):
          print('\n\n-----Invoking error microservice as details fails-----')
          invoke_http(ERROR_URL, method="POST", json=account_result)
          # - reply from the invocation is not used; 
          # continue even if this invocation fails
          print("Account status ({:d}) sent to the error microservice:".format(
              code), account_result)
          return {
              "code": 500,
              "data": {"account_result": account_result},
              "message": "Account collection failure sent for error handling."
          }
    
    # Collect review details
    # Invoke the review microservice
    print('\n-----Invoking review microservice-----')
    review_result = invoke_http(REVIEW_URL+"/reviews/"+str(details['cc_id']), method='GET', json=details)
    print('review_result:', review_result)

    code = review_result["code"]
    if code != 404:
      if code not in range(200, 300):
          print('\n\n-----Invoking error microservice as details fails-----')
          invoke_http(ERROR_URL, method="POST", json=review_result)
          # - reply from the invocation is not used; 
          # continue even if this invocation fails
          print("Review status ({:d}) sent to the error microservice:".format(
              code), review_result)
          return {
              "code": 500,
              "data": {"review_result": review_result},
              "message": "Review collection failure sent for error handling."
          }

    # Collect collaboration details
    # Invoke collab microservice
    print('\n-----Invoking collab microservice-----')
    collab_result = invoke_http(COLLAB_URL+"/cc/"+str(details['cc_id']), method='GET', json=details)
    print('collab_result:', collab_result)
    code = collab_result["code"]

    if code != 404:
      if code not in range(200, 300):
          print('\n\n-----Invoking error microservice as details fails-----')
          invoke_http(ERROR_URL, method="POST", json=collab_result)
          # - reply from the invocation is not used; 
          # continue even if this invocation fails
          print("Collab status ({:d}) sent to the error microservice:".format(
              code), collab_result)
          return {
              "code": 500,
              "data": {"collab_result": collab_result},
              "message": "Collab collection failure sent for error handling."
          }


    # Collect project details
    # Invoke Project microservice
    print('\n-----Invoking project microservice-----')
    project_result = invoke_http(PROJECT_URL+"/get_project?cc_id="+str(details['cc_id']), method='GET', json=details)
    print('project_result:', project_result)

    code = project_result["code"]
    if code != 404:
      if code not in range(200, 300):
          print('\n\n-----Invoking error microservice as order fails-----')
          invoke_http(ERROR_URL, method="POST", json=project_result)
          # - reply from the invocation is not used; 
          # continue even if this invocation fails
          print("Review status ({:d}) sent to the error microservice:".format(
              code), project_result)
          return {
              "code": 500,
              "data": {"order_result": project_result},
              "message": "Review collection failure sent for error handling."
          }

    if "brand" in details:
      collab_result["data"] = [collab for collab in collab_result["data"] if collab["data"]["collab_status"] != "on-going"]



    complex_results = {
                "code": 200,
                "data":{
                    "collab":
                        collab_result["data"]
                    ,
                    "account":
                        account_result["data"]
                    ,
                    "review":
                        review_result["data"],
                    "project":
                        project_result["data"]
                    
                }
            }
    return complex_results

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
