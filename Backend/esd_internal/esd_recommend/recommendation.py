import requests
from flask import Flask, jsonify, request
from flasgger import Swagger
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SWAGGER'] = {
    'title': 'Recommendation Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'Provides recommendation for selected content creators upon brand view'
}
swagger = Swagger(app)

# URL to fetch content creators from the Account microservice
ACCOUNT_CREATOR_URL = "http://"+os.environ.get("externalService")+":3000"

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """
    Get Recommendations for Selected Content Creator
    ---
    parameters:
      - in: query
        name: creator_id
        required: true
        schema:
          type: string
          description: The unique identifier of the selected content creator for whom recommendations are being requested.
    responses:
      200:
        description: Successfully retrieved recommendations for similar content creators based on interests.
        content:
          application/json:
            schema:
              type: object
              properties:
                code:
                  type: integer
                  description: HTTP status code indicating the request was successful.
                similar_creators:
                  type: array
                  description: An array of similar content creators.
                  items:
                    type: object
                    properties:
                      user_id:
                        type: integer
                        description: The unique identifier of a similar content creator.
                      username:
                        type: string
                        description: The username of a similar content creator.
                      interests:
                        type: string
                        description: The interests of a similar content creator, matching or similar to the selected creator's interests.
      404:
        description: Failed to fetch similar content creators based on interests.
      500:
        description: Network error while contacting the Account Service.
    """
    selected_creator_id = request.get_json()['creator_id']
    
    try:
        # Fetch details of the selected content creator, including their interests
        selected_creator_response = requests.get(f"{ACCOUNT_CREATOR_URL}/users?user_id={selected_creator_id}")
        print(selected_creator_response)
        
        if selected_creator_response.status_code == 200:
            selected_creator_details = selected_creator_response.json()
            print(selected_creator_details)
            interests = selected_creator_details["data"]["interests"]
            print(interests)
            # Assuming interests are stored as a comma-separated string
            
            # Prepare a query to find creators with similar interests
            # This assumes the Account microservice can filter creators by interests
            similar_creators_response = requests.get(f'{ACCOUNT_CREATOR_URL}/users/interests/{interests}').json()
            
            temp=[]
            for account in similar_creators_response["data"]:
                if str(account["user_id"])!=str(selected_creator_id) and account["acc_type"]=="cc":
                    temp.append(account)
            similar_creators_response["data"]=temp
                
        
            print(similar_creators_response["code"])
            if similar_creators_response["code"] == 200:
                similar_creators = similar_creators_response
                
                # Further refine or rank the similar creators based on matching interests here if necessary
                
                return jsonify({"code": 200, "similar_creators": similar_creators}), 200
            else:
                return jsonify({"code": 404, "error": "Failed to fetch similar content creators based on interests"}), 404
        else:
            selected_creator_details = selected_creator_response.json()
            print(selected_creator_details["code"])
            return jsonify({"code": selected_creator_details["code"], "error": "Failed to fetch selected content creator details"}), selected_creator_details["code"]
    except requests.RequestException:
        return jsonify({"code": 500, "error": "Network error while contacting Account Service"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)