import os
import stripe
from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger
import urllib
app = Flask(__name__)
CORS(app)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

app.config["SWAGGER"] = {
    "title": "Payment Microservice API",
    "version": "1.0",
    "openapi": "3.0.2",
    "description": "Manages payment and checkout sessions for users",
}
swagger = Swagger(app)


@app.route("/")
def home():
    return "Server is running"


@app.route("/checkout-session", methods=["POST"])
def create_checkout_session():
    """
    Create Stripe Checkout Session
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        stripe_key:
                            type: string
                            description: Stripe secret key to authenticate the request.
                        cc_id:
                            type: string
                            description: The unique identifier of the content creator involved in the transaction.
                        brand_id:
                            type: string
                            description: The unique identifier of the brand initiating the payment.
                        items:
                            type: array
                            description: List of items for payment.
                            items:
                                type: object
                                properties:
                                    collab_title:
                                        type: string
                                        description: Title of the collaboration.
                                    amount:
                                        type: integer
                                        description: Amount to be paid for the item in cents.
                                    quantity:
                                        type: integer
                                        description: Number of items (should typically be 1).
    responses:
      200:
        description: Checkout session created successfully. Returns the URL for the checkout session.
        content:
          application/json:
            schema:
                type: object
                properties:
                    url:
                        type: string
                        description: The URL to redirect the user for payment processing.
      500:
        description: An error occurred while creating the checkout session. Returns an error message.
        content:
          application/json:
            schema:
                type: object
                properties:
                    error:
                        type: string
                        description: A descriptive error message.
    """
    try:
        print("h232")
        data = request.get_json()
        print(data, 111111)
        stripe.api_key = data["stripe_key"]

        cc_id=data["cc_id"]
        brand_id=data["brand_id"]
        collab_title=data["collab_title"]
        # storeItems = {1: {"priceInCents": 10000, "name": "Nike Collab"}}
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "sgd",
                        "product_data": {"name": collab_title},
                        "unit_amount": item["amount"],
                    },
                    "quantity": item["quantity"],
                }
                for item in data["items"]
            ],
            # success_url=f"{os.environ.get('CLIENT_URL')}",
            # cancel_url=f"{os.environ.get('CLIENT_URL')}/Collab"
            success_url=f"{os.environ.get('webServerURL')}/Payment?cc_id={cc_id}&brand_id={brand_id}&collab_title={urllib.parse.quote(collab_title)}",
            cancel_url=f"{os.environ.get('webServerURL')}",
        )
        print(2)
        return jsonify({"url": session.url})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
