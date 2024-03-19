import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# URL to fetch content creators from the Account microservice
ACCOUNT_CREATOR_URL = "http://172.28.110.113:3000"

@app.route('/recommendation', methods=['GET'])
def get_recommendations():
    selected_creator_id = request.get_json()['creator_id']
    
    try:
        # Fetch details of the selected content creator, including their interests
        selected_creator_response = requests.get(f"{ACCOUNT_CREATOR_URL}/get_user/{selected_creator_id}")
        print(selected_creator_response)
        
        if selected_creator_response.status_code == 200:
            selected_creator_details = selected_creator_response.json()
            print(selected_creator_details)
            interests = selected_creator_details["data"]["interests"]
            print(interests)
            # Assuming interests are stored as a comma-separated string
            
            # Prepare a query to find creators with similar interests
            # This assumes the Account microservice can filter creators by interests
            similar_creators_response = requests.get(f'{ACCOUNT_CREATOR_URL}/get_users_by_interests/{interests}').json()
            
            temp=[]
            for account in similar_creators_response["data"]:
                if str(account["user_id"])!=str(selected_creator_id):
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
            print(selected_creator_response["code"])
            return jsonify({"code": selected_creator_response["code"], "error": "Failed to fetch selected content creator details"}), selected_creator_response["code"]
    except requests.RequestException:
        return jsonify({"code": 500, "error": "Network error while contacting Account Service"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)

#return jsonify({"code": 404, "message": "Review not found."}), 404