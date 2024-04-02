from flask import Flask, request, jsonify
import os, sys
import requests
from flasgger import Swagger
from invokes import invoke_http
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config['SWAGGER'] = {
    'title': 'Update Collaboration Complex Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'View content creator profiles'
}
swagger = Swagger(app)

blacklist_URL = "http://host.docker.internal:3005/blacklist"
notification_URL = "http://host.docker.internal:3006"
collab_URL = "http://host.docker.internal:3001/collaborations"

@app.route("/update_request", methods=['PUT'])
def accept_request():
    """
    Update a Collaboration Request
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
                            description: The unique identifier of the brand initiating the collaboration.
                        collab_title:
                            type: string
                            description: The title of the collaboration being updated.
                        collab_status:
                            type: string
                            description: The new status of the collaboration (e.g., "Completed", "Review").
    responses:
      201:
        description: Collaboration request successfully updated. Notifications sent to relevant parties if applicable.
      400:
        description: Invalid JSON input.
      404:
        description: Collaboration request not found.
      500:
        description: Internal server error. Could be due to issues with microservice communication or unexpected server errors.
    """
    if request.is_json:
        try:
            collab = request.get_json()
            print("\nReceived an collab in JSON:", collab)

            result = processUpdateRequest(collab)
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
                "message": "app.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processUpdateRequest(collab):

    print('\n\n-----Invoking collab microservice-----')
    collab_result=invoke_http(collab_URL+"/status" , method="PUT", json=collab)
    code = collab_result["code"]
    # print('collab_result:', collab_result)
    
    if code not in range(200, 300):
        print('collab_result:', collab_result)
        
        return {
            "code": 404,
            "message": "Collab request not found!!"
        }
    else:
        
        print('\n\n-----Invoking notification microservice-----')
        if (collab_result["data"]["collab_status"]=="Completed"):
            data={
                "sender": collab_result["data"]["brand_id"],
                "message": "Collaboration updated!\nBrand: "+collab_result["data"]["brand_id"]+"\nCollab title: "+collab_result["data"]["collab_title"]+"\nCollab_status: "+collab_result["data"]["collab_status"],
                "receiver":collab_result["data"]["cc_id"]
            }
            invoke_http(notification_URL+"/notify", method="POST", json=data)
            
            
        elif (collab_result["data"]["collab_status"]=="Review"):
            data={
                "sender": collab_result["data"]["cc_id"],
                "message": "Collaboration updated!\nContent creator: "+collab_result["data"]["cc_id"]+"\nCollab title: "+collab_result["data"]["collab_title"]+"\nCollab_status: "+collab_result["data"]["collab_status"],
                "receiver":collab_result["data"]["brand_id"]
            }

            invoke_http(notification_URL+"/notification/publish", method="POST", json=data)
        
        

        return {
            "code": 201,
            "message": "Collaboration updated!"
        }
 



if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + "111111111111111111111...")
    app.run(host="0.0.0.0", port=5100, debug=True)

