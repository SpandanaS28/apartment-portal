from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

import os

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/apartment_portal"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    apartments = db.relationship("Apartment", back_populates="category")

class Apartment(db.Model):
    __tablename__ = "apartments"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    location = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    category = db.relationship("Category", back_populates="apartments")

def apartment_to_dict(a: Apartment):
    return {
        "id": a.id,
        "title": a.title,
        "price": a.price,
        "location": a.location,
        "category_id": a.category_id,
        "category_name": a.category.name if a.category else None,
        "created_at": a.created_at.isoformat() if a.created_at else None,
    }

@app.route("/")
def home():
    return jsonify(message="Backend is running successfully")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.order_by(Category.id.asc()).all()
    result = [{"id": c.id, "name": c.name} for c in categories]
    return jsonify(result)

@app.route("/apartments", methods=["GET"])
def get_apartments():
    apartments = Apartment.query.order_by(Apartment.id.asc()).all()
    return jsonify([apartment_to_dict(a) for a in apartments])

@app.route("/apartments/<int:apt_id>", methods=["GET"])
def get_apartment_by_id(apt_id):
    a = Apartment.query.get_or_404(apt_id)
    return jsonify(apartment_to_dict(a))

@app.route("/apartments", methods=["POST"])
def create_apartment():
    data = request.get_json(silent=True) or {}

    title = data.get("title")
    price = data.get("price")
    category_id = data.get("category_id")
    location = data.get("location")

    if not title or not isinstance(title, str):
        return jsonify(error="title is required"), 400

    if price is None:
        return jsonify(error="price is required"), 400

    try:
        price = int(price)
    except Exception:
        return jsonify(error="price must be a number"), 400

    if category_id is None:
        return jsonify(error="category_id is required"), 400

    try:
        category_id = int(category_id)
    except Exception:
        return jsonify(error="category_id must be a number"), 400

    category = Category.query.get(category_id)
    if not category:
        return jsonify(error="category_id does not exist"), 400

    a = Apartment(title=title.strip(), price=price, category_id=category_id, location=location)
    db.session.add(a)
    db.session.commit()

    return jsonify(apartment_to_dict(a)), 201

@app.route("/apartments/<int:apt_id>", methods=["PUT"])
def update_apartment(apt_id):
    a = Apartment.query.get_or_404(apt_id)
    data = request.get_json(silent=True) or {}

    if "title" in data:
        if not data["title"]:
            return jsonify(error="title cannot be empty"), 400
        a.title = str(data["title"]).strip()

    if "price" in data:
        try:
            a.price = int(data["price"])
        except Exception:
            return jsonify(error="price must be a number"), 400

    if "location" in data:
        a.location = data["location"]

    if "category_id" in data:
        try:
            new_cat = int(data["category_id"])
        except Exception:
            return jsonify(error="category_id must be a number"), 400

        category = Category.query.get(new_cat)
        if not category:
            return jsonify(error="category_id does not exist"), 400
        a.category_id = new_cat

    db.session.commit()
    return jsonify(apartment_to_dict(a))

@app.route("/apartments/<int:apt_id>", methods=["DELETE"])
def delete_apartment(apt_id):
    a = Apartment.query.get_or_404(apt_id)
    db.session.delete(a)
    db.session.commit()
    return jsonify(message="Deleted")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

