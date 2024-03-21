from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

account_URL = "http://"+os.environ.get("simpleServer")+":3000"
collab_URL = "http://"+os.environ.get("simpleServer")+":3001/collaboration"
review_URL = "http://"+os.environ.get("simpleServer")+":3002"
project_URL = "http://"+os.environ.get("simpleServer")+":3003/"
error_URL = "http://"+os.environ.get("simpleServer")+":5005/error"


@app.route("/view_profile", methods=['GET'])
def check_profile():
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            details = request.get_json()
            print("\nReceived a profile in JSON:", details)

            # do the actual work
            # 1. Send order info {cart items}
            result = processViewProfile(details)
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


def processViewProfile(details):
    # Collect Account details
    # Invoke Account Microservice
    print('\n-----Invoking account microservice-----')
    account_result = invoke_http(account_URL+"/get_user/"+str(details['cc_id']) ,method='GET', json=details)
    print('account_result:', account_result)

    code = account_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Invoking error microservice as details fails-----')
        invoke_http(error_URL, method="POST", json=account_result)
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
    review_result = invoke_http(review_URL+"/review/"+str(details['cc_id']), method='GET', json=details)
    print('review_result:', review_result)

    code = review_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Invoking error microservice as details fails-----')
        invoke_http(error_URL, method="POST", json=review_result)
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
    collab_result = invoke_http(collab_URL+"/cc/"+str(details['cc_id']), method='GET', json=details)
    print('collab_result:', collab_result)
    code = collab_result["code"]

    if code not in range(200, 300):
        print('\n\n-----Invoking error microservice as details fails-----')
        invoke_http(error_URL, method="POST", json=collab_result)
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
    project_result = invoke_http(project_URL+"/get_project", method='GET', json=details)
    print('project_result:', project_result)

    code = project_result["code"]
    if code not in range(200, 300):
        print('\n\n-----Invoking error microservice as order fails-----')
        invoke_http(error_URL, method="POST", json=project_result)
        # - reply from the invocation is not used; 
        # continue even if this invocation fails
        print("Review status ({:d}) sent to the error microservice:".format(
            code), project_result)
        return {
            "code": 500,
            "data": {"order_result": project_result},
            "message": "Review collection failure sent for error handling."
        }


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
