from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
import os, sys
import requests
from invokes import invoke_http

import json

app = Flask(__name__)
CORS(app)

app.config['SWAGGER'] = {
    'title': 'Place Request Complex Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'Place requests for collaboration with selected content creator'
}
swagger = Swagger(app)

blacklist_URL = "http://host.docker.internal:3005/blacklist"
notification_URL = "http://host.docker.internal:3006"
collab_URL = "http://host.docker.internal:3001/collaborations" # changed from collaboration to collaborations


@app.route("/place_request", methods=['POST'])
def place_request():
    """
    Place a Collaboration Request
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
                            description: The unique identifier of the content creator with whom the collaboration is requested.
                        brand_id:
                            type: string
                            description: The unique identifier of the brand initiating the collaboration request.
                        details:
                            type: string
                            description: The details of the collaboration request.
    responses:
      201:
        description: Collaboration request successfully placed and notification sent.
      400:
        description: Invalid JSON input.
      403:
        description: The brand is blacklisted from requesting collaborations with this content creator.
      409:
        description: Collaboration request already exists between the specified brand and content creator.
      500:
        description: Internal server error. Could be due to issues with microservice communication or unexpected server errors.
    """
    if request.is_json:
        try:
            collab = request.get_json()
            print("\nReceived an collab in JSON:", collab)


            result = processPlaceRequest(collab)
            print('\n------------------------')
            print('\nresult: ', result)
            return jsonify(result), result["code"]

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "place_order.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processPlaceRequest(collab):


    print('\n-----Invoking blacklist microservice-----')
    

    
    blacklist_result = invoke_http(blacklist_URL+"?account="+collab["cc_id"]+"&banned_account="+collab["brand_id"], method='GET')
    print('blacklist_result:', blacklist_result)
  

    code = blacklist_result["code"]
    
    if code not in range(200, 300):

        print('\n\n-----Invoking collab microservice-----')

        collab_result=invoke_http(collab_URL , method="POST", json=collab)
        code = collab_result["code"]
        
        print('collab_result:', collab_result)
        
        if code not in range(200, 300):
            print('collab_result:', collab_result)
            
            return {
                "code": 409,
                "message": "Collaboration already exist!"
            }
        else:
            
            print('\n\n-----Invoking notification microservice-----')
            data={
                "sender": collab["brand_id"],
                "message": "Request for collaboration",
                "receiver":collab["cc_id"]
            }

            invoke_http(notification_URL+"/notification/publish", method="POST", json=data)
            
            

            return {
                "code": 201,
                "message": "Collaboration request sent!"
            }
 
    else:
        return{
            "code": 403,
            "message": "You are blacklisted"
        
        }


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)

