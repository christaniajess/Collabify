from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
from datetime import datetime
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/review'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# CORS(app)

class Review(db.Model):
    __tablename__ = 'review'

    review_id = db.Column(db.Integer, primary_key=True)
    cc_id = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, cc_id, brand_id, rating, title, content, timestamp=None):
        self.cc_id = cc_id
        self.brand_id = brand_id
        self.rating = rating
        self.title = title
        self.content = content
        if timestamp is not None:
            self.timestamp = timestamp

    def json(self):
        return {
            "review_id": self.review_id,
            "cc_id": self.cc_id,
            "brand_id": self.brand_id,
            "rating": self.rating,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None
        }

@app.route("/review", methods=['POST'])
def create_review():
    """
    Create a review
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    required:
                      - cc_id
                      - brand_id
                      - rating
                      - title
                      - content
                    properties:
                        cc_id:
                            type: integer
                            description: ID of the content creator
                        brand_id:
                            type: integer
                            description: ID of the brand
                        rating:
                            type: integer
                            description: Rating given to the content creator
                        title:
                            type: string
                            description: Title of the review
                        content:
                            type: string
                            description: Content of the review
    responses:
        201:
            description: Review created
        500:
            description: Internal server error
    """
    data = request.get_json()
    new_review = Review(**data)
    try:
        db.session.add(new_review)
        db.session.commit()
        return jsonify({"code": 201, "data": new_review.json()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"code": 500, "message": "An error occurred creating the review.", "error": str(e)}), 500

@app.route("/review/<int:cc_id>", methods=['GET'])
def get_reviews_by_cc(cc_id):
    """Retrieve all reviews for a specified content creator
    ---
    parameters:
      - name: cc_id
        in: path
        required: true
        type: integer
        description: The content creator's ID
    responses:
      200:
        description: An array of reviews for the content creator
      404:
        description: No reviews found for the specified content creator
    """
    reviews_query = db.session.query(Review).filter(Review.cc_id == cc_id).all()
    if reviews_query:
        return jsonify({
            "code": 200,
            "data": [review.json() for review in reviews_query]
        })
    else:
        return jsonify({"code": 404, "message": "No reviews found for the specified content creator."}), 404

@app.route("/review/<int:review_id>", methods=['PUT'])
def update_review(review_id):
    """
    Update a review by its ID
    ---
    parameters:
        -   in: path
            name: review_id
            required: true
            schema:
                type: integer
                description: The review's unique identifier
    requestBody:
        description: Review's details to be updated
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        cc_id:
                            type: integer
                            description: Content Creator ID
                        brand_id:
                            type: integer
                            description: Brand ID
                        rating:
                            type: integer
                            description: Rating given to the content creator
                        title:
                            type: string
                            description: Title of the review
                        content:
                            type: string
                            description: Detailed content of the review
    responses:
        200:
            description: Review updated successfully
        404:
            description: Review not found
        500:
            description: Internal server error
    """
    review_query = db.session.scalars(db.select(Review).filter_by(review_id=review_id)).first()
    if review_query:
        data = request.get_json()
        for key, value in data.items():
            setattr(review_query, key, value)
        db.session.commit()
        return jsonify({"code": 200, "data": review_query.json()})
    else:
        return jsonify({"code": 404, "message": "Review not found."}), 404

@app.route("/review/<int:review_id>", methods=['DELETE'])
def delete_review(review_id):
    """
    Delete a review by its ID
    ---
    parameters:
        -   in: path
            name: review_id
            required: true
            schema:
                type: integer
                description: The review's unique identifier
    responses:
        200:
            description: Review deleted successfully
        404:
            description: Review not found
        500:
            description: Internal server error
    """
    review_query = db.session.scalars(db.select(Review).filter_by(review_id=review_id)).first()
    if review_query:
        db.session.delete(review_query)
        db.session.commit()
        return jsonify({"code": 200, "message": "Review successfully deleted."})
    else:
        return jsonify({"code": 404, "message": "Review not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
