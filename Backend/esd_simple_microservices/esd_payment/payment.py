import os
import stripe
from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger

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
                        items:
                            type: array
                            description: List of items to include in the checkout session.
                            items:
                                type: object
                                properties:
                                    id:
                                        type: integer
                                        description: The unique ID of the item.
                                    quantity:
                                        type: integer
                                        description: Quantity of the item to purchase.
                    required:
                        - items
    responses:
        200:
            description: Checkout session created successfully. Returns the session URL for redirection.
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            url:
                                type: string
                                description: URL to the Stripe checkout session. Redirect your user to this URL for the payment process.
        500:
            description: An error occurred in creating the checkout session. Check the error message for more details.
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            error:
                                type: string
                                description: Detailed error message.
    """
    try:
        print("h232")
        data = request.get_json()
        print(data, 111111)
        stripe.api_key = data["stripe_key"]

        cc_id=data["cc_id"]
        brand_id=data["brand_id"]
        # storeItems = {1: {"priceInCents": 10000, "name": "Nike Collab"}}
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "price_data": {
                        "currency": "sgd",
                        "product_data": {"name": item["collab_title"]},
                        "unit_amount": item["amount"],
                    },
                    "quantity": item["quantity"],
                }
                for item in data["items"]
            ],
            # success_url=f"{os.environ.get('CLIENT_URL')}",
            # cancel_url=f"{os.environ.get('CLIENT_URL')}/Collab"
            success_url="http://localhost:5173/Payment?cc_id="+cc_id+"&brand_id="+brand_id,
            cancel_url="http://localhost:5173",
        )
        print(2)
        return jsonify({"url": session.url})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
