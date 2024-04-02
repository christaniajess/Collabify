from flask import Flask, jsonify, request
from invokes import invoke_http
from flask_cors import CORS
from flasgger import Swagger
import os
import os, sys

app = Flask(__name__)
CORS(app)

app.config['SWAGGER'] = {
    'title': 'Brand View Complex Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'View content creator profiles with recommendations'
}
swagger = Swagger(app)

# Environment variables or replace with actual URLs of your microservices
VIEW_URL = "http://host.docker.internal:3004"
RECOMMENDATION_URL = "http://"+os.environ.get("internalService")+":3008/recommendations"


@app.route("/view/cc/<int:cc_id>", methods=['GET'])
def view_content_creator(cc_id):
    """
    View Content Creator Profile with Recommendations
    ---
    parameters:
      - in: path
        name: cc_id
        required: true
        schema:
          type: integer
          description: The unique identifier of the content creator whose profile and recommendations are being requested.
    responses:
      200:
        description: Successfully retrieved content creator profile along with recommendations for similar creators.
        content:
          application/json:
            schema:
              type: object
              properties:
                view:
                  type: object
                  description: The profile details of the content creator.
                  properties:
                    # Specify the structure of the content creator's profile details
                recommendation:
                  type: array
                  description: A list of recommended similar content creators based on interests.
                  items:
                    type: object
                    properties:
                      # Specify the structure of a recommendation item
      400:
        description: Bad request. The request was not properly formatted.
      404:
        description: Content creator profile or recommendations not found.
      500:
        description: An internal server error occurred while fetching the profile or recommendations.
    """
    # Step 2: Retrieve view for the content creator from Review microservice
    view = invoke_http(f"{VIEW_URL}/profile?cc_id="+str(cc_id), method='GET')
    if view['code'] not in range(200, 300):
        # Return error response if view cannot be retrieved
        return jsonify(view), view['code']

    # Step 3: Get recommendation based on content creator's interests from Recommendation microservice
    recommendation = invoke_http(f"{RECOMMENDATION_URL}", method='GET',json={"creator_id":cc_id})
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
