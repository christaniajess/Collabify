from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

app.config["SWAGGER"] = {
    "title": "View Profile Complex Microservice API",
    "version": "1.0",
    "openapi": "3.0.2",
    "description": "View content creator profiles",
}
swagger = Swagger(app)

ACCOUNT_URL = "http://host.docker.internal:3000"
COLLAB_URL = "http://host.docker.internal:3001/collaborations"
PAYMENT_URL = "http://" + os.environ.get("internalService") + ":3010/checkout-session"

# ACCOUNT_URL = "http://" + "localhost" + ":3000"
# COLLAB_URL = "http://" + "localhost" + ":3001/collaborations"
# PAYMENT_URL = "http://" + "localhost" + ":5000/checkout-session"
# http://localhost:5000/checkout-session


@app.route("/close_collab", methods=["POST"])
def close_collab():
    """
    Close Collaboration and Initiate Payment
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
                            description: The unique identifier of the brand involved in the collaboration.
                        collab_title:
                            type: string
                            description: The title of the collaboration.
                        amount:
                            type: number
                            format: float
                            description: The amount to be paid for the collaboration.
    responses:
      200:
        description: Collaboration successfully closed and payment initiated. Returns the payment URL.
        content:
          application/json:
            schema:
                type: object
                properties:
                    payment_url:
                        type: string
                        description: URL to redirect for payment processing.
      400:
        description: Invalid JSON input.
      404:
        description: Account not found for the specified user ID.
      500:
        description: Internal server error. Could be due to failure in invoking account or payment microservices.
    """
    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            details = request.get_json()
            print(
                "\nReceived a profile in JSON:", details
            )  # Details provided is the id of the requested user in json format

            # Get all the relevant details of the user
            result = get_profile_data(details)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = (
                str(e)
                + " at "
                + str(exc_type)
                + ": "
                + fname
                + ": line "
                + str(exc_tb.tb_lineno)
            )
            print(ex_str)

            return (
                jsonify(
                    {
                        "code": 500,
                        "message": "Internal server error: " + ex_str,
                    }
                ),
                500,
            )

    # if reached here, not a JSON request.
    return (
        jsonify(
            {"code": 400, "message": "Invalid JSON input: " + str(request.get_data())}
        ),
        400,
    )


def get_profile_data(details):
    # Collect Account details
    # Invoke Account Microservice
    print("\n-----Invoking account microservice-----")
    account_result = invoke_http(
        ACCOUNT_URL + "/user/payment?user_id=" + str(details["cc_id"]), method="GET"
    )
    print("account_result:", account_result)

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

    stripe_key = account_result["data"]["stripe_key"]
    # Collect Payment details
    # Invoke Payment Microservice
    print("\n-----Invoking payment microservice-----")

    payment_result = invoke_http(
        PAYMENT_URL,
        method="POST",
        json={
            "items": [
                {
                    "amount": details["amount"],
                    "quantity": 1,
                }
            ],
            "stripe_key": stripe_key,
            "brand_id": details["brand_id"],
            "cc_id": details["cc_id"],
            "collab_title": details["collab_title"],
        },
    )

    print("paymentResult:", payment_result)

    code = account_result["code"]
    if code not in range(200, 300):

        return {
            "code": 500,
            "data": {"payment_result": payment_result},
        }

    return {
        "code": 200,
        "payment_url": payment_result['url'],
    }


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
