from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from datetime import datetime
import os
from flask_cors import CORS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("dbURL")
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SWAGGER'] = {
    'title': 'Review Microservice API',
    'version': '1.0',
    'openapi': '3.0.2',
    'description': 'Manage reviews of content creators'
}
swagger = Swagger(app)

class Review(db.Model):
    __tablename__ = 'reviews'

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

@app.route("/reviews", methods=['POST'])
def create_review():
    """
    Create a new review
    ---
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        cc_id:
                            type: integer
                            description: The unique identifier of the content creator being reviewed.
                        brand_id:
                            type: integer
                            description: The unique identifier of the brand posting the review.
                        rating:
                            type: integer
                            description: The rating given to the content creator by the brand.
                        title:
                            type: string
                            description: The title of the review.
                        content:
                            type: string
                            description: The detailed content of the review.
    responses:
        201:
            description: Review successfully created. Returns the details of the newly added review.
            content:
                application/json:
                    schema:
                        $ref: '#/components/schemas/Review'
        500:
            description: An error occurred creating the review. Check the error details.
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

@app.route("/reviews/<int:cc_id>", methods=['GET'])
def get_reviews_by_content_creator(cc_id):
    """
    Get reviews by content creator ID
    ---
    parameters:
        - in: path
          name: cc_id
          required: true
          schema:
            type: integer
            description: The unique identifier of the content creator for whom reviews are being retrieved.
    responses:
        200:
            description: Successfully retrieved an array of reviews for the specified content creator.
            content:
                application/json:
                    schema:
                        type: array
                        items:
                            $ref: '#/components/schemas/Review'
        404:
            description: No reviews found for the specified content creator.
    """
    reviews_query = db.session.query(Review).filter(Review.cc_id == cc_id).all()
    if reviews_query:
        return jsonify({
            "code": 200,
            "data": [review.json() for review in reviews_query]
        })
    else:
        return jsonify({"code": 404,  "data": {"cc_id": cc_id, "message": "No reviews found for the specified content creator."}, "message": "No reviews found for the specified content creator."}), 404

@app.route("/reviews/<int:review_id>", methods=['PUT'])
def update_review(review_id):
    """
    Update a review
    ---
    parameters:
        - in: path
          name: review_id
          required: true
          schema:
            type: integer
            description: The unique identifier of the review to be updated.
    requestBody:
        required: true
        content:
            application/json:
                schema:
                    type: object
                    properties:
                        rating:
                            type: integer
                            description: Updated rating for the review.
                        title:
                            type: string
                            description: Updated title of the review.
                        content:
                            type: string
                            description: Updated detailed content of the review.
    responses:
        200:
            description: Review successfully updated. Returns the updated details of the review.
        404:
            description: Review not found. The specified review ID does not exist.
        500:
            description: An internal server error occurred while updating the review.
    """
    review_query = db.session.scalars(db.select(Review).filter_by(review_id=review_id)).first()
    if review_query:
        data = request.get_json()
        for key, value in data.items():
            setattr(review_query, key, value)
        db.session.commit()
        return jsonify({"code": 200, "data": review_query.json()})
    else:
        return jsonify({"code": 404, "data": {"review_id": review_id, "message": "Review not found."}, "message": "Review not found."}), 404

@app.route("/reviews/<int:review_id>", methods=['DELETE'])
def delete_review(review_id):
    """
    Delete a review
    ---
    parameters:
        - in: path
          name: review_id
          required: true
          schema:
            type: integer
            description: The unique identifier of the review to be deleted.
    responses:
        200:
            description: Review successfully deleted.
        404:
            description: Review not found. The specified review ID does not exist.
        500:
            description: An internal server error occurred while deleting the review.
    """
    review_query = db.session.scalars(db.select(Review).filter_by(review_id=review_id)).first()
    if review_query:
        db.session.delete(review_query)
        db.session.commit()
        return jsonify({"code": 200, "message": "Review successfully deleted."})
    else:
        return jsonify({"code": 404, "data":{"review_id": review_id, "message": "Review not found."}, "message": "Review not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
