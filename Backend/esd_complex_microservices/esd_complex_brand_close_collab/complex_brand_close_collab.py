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

ACCOUNT_URL = "http://"+os.environ.get("simpleServer")+":3000"
COLLAB_URL = "http://"+os.environ.get("simpleServer")+":3001/collaborations"



@app.route("/profile", methods=['POST'])
def close_collab():
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
    if request.is_json:
        try:
            details = request.get_json()
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

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def get_profile_data(details):
    # Collect Account details
    # Invoke Account Microservice
    print('\n-----Invoking account microservice-----')
    account_result = invoke_http(ACCOUNT_URL+"/user/payment?user_id="+str(details['cc_id']), method='GET')
    print('account_result:', account_result)

    code = account_result["code"]
    if code not in range(200, 300):

        if code == 404:
            return {
                "code": 404,
                "data": {"message": "Account not found for the specified user ID."},
            }
        else:
          return {
              "code": 500,
              "data": {"account_result": account_result},
          }
    

    stripe_key=account_result['data']['stripe_key']
    # Collect Payment details
    # Invoke Payment Microservice
    print('\n-----Invoking payment microservice-----')
    

    return {
      "code": 200,
      'stripe_key': account_result['data']['stripe_key'],
    }

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
