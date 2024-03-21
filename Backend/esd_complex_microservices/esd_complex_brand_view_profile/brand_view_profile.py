from flask import Flask, jsonify, request
from invokes import invoke_http
from flask_cors import CORS
import os
import os, sys

app = Flask(__name__)
CORS(app)

# Environment variables or replace with actual URLs of your microservices
VIEW_URL = "http://"+os.environ.get("complexServer")+":3004"
RECOMMENDATION_URL = "http://"+os.environ.get("simpleServer")+":3008/recommendation"

@app.route("/view/content_creator/<int:content_creator_id>", methods=['GET'])
def view_content_creator(content_creator_id):
    # Step 2: Retrieve view for the content creator from Review microservice
    view = invoke_http(f"{VIEW_URL}/view_profile", method='GET',json={"cc_id":content_creator_id})
    if view['code'] not in range(200, 300):
        # Return error response if view cannot be retrieved
        return jsonify(view), view['code']

    # Step 3: Get recommendation based on content creator's interests from Recommendation microservice
    recommendation = invoke_http(f"{RECOMMENDATION_URL}", method='GET',json={"creator_id":content_creator_id})
    print(recommendation)
    if recommendation['code'] not in range(200, 300):
        # Return error response if recommendation cannot be retrieved
        return jsonify(recommendation), recommendation['code']

    # Combine all the information into a single response object
    print(recommendation)
    result = {
        'view': view['data'],
        'recommendation': recommendation['similar_creators']['data']
    }

    return jsonify(result), 200


@app.route("/")
def check_flask_running():
    return "Flask is running!"



if __name__ == "__main__":
    print("11111111111111111This is flask " + os.path.basename(__file__) +
        " 1111111111111111111111111111...")
    app.run(host='0.0.0.0', port=5100, debug=True)
