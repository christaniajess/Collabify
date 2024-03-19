import os
import stripe
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

stripe.api_key = os.environ.get('STRIPE_PRIVATE_KEY')

storeItems = {
    1: {'priceInCents': 10000, 'name': 'Nike Collab'}
}


@app.route('/')
def home():
    return "Server is running"



@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        data = request.get_json()
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'price_data': {
                        'currency': 'sgd',
                        'product_data': {
                            'name': storeItems[item['id']]['name']
                        },
                        'unit_amount': storeItems[item['id']]['priceInCents'],
                    },
                    'quantity': item['quantity']
                }
                for item in data['items']
            ],
            success_url=f"{os.environ.get('CLIENT_URL')}/success.html",
            cancel_url=f"{os.environ.get('CLIENT_URL')}/cancel.html"
        )
        return jsonify({'url': session.url})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)


