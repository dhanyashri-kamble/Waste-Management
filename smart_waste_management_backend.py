from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(name)
CORS(app)  # Enable CORS for frontend access

# Simulated eco points storage (in-memory)
eco_points = {"user": 0}

# Waste classification categories
waste_types = ["Plastic", "Organic", "Metal", "Paper", "E-waste"]

# Smart bin data
bin_data = [
    {"location": "Sector 5", "level": "75%", "status": "Almost Full"},
    {"location": "MG Road", "level": "30%", "status": "Available"},
    {"location": "Park Area", "level": "90%", "status": "Urgent"},
    {"location": "Main Square", "level": "50%", "status": "Moderate"},
]

# --- Routes ---

@app.route("/")
def home():
    return jsonify({"message": "Smart Waste Management API is running"})

@app.route("/classify", methods=["POST"])
def classify():
    # Simulate classification
    chosen_type = random.choice(waste_types)
    return jsonify({"waste_type": chosen_type})

@app.route("/bin-data", methods=["GET"])
def get_bin_data():
    return jsonify({"bins": bin_data})

@app.route("/eco-points", methods=["GET"])
def get_points():
    return jsonify({"points": eco_points["user"]})

@app.route("/eco-points", methods=["POST"])
def add_points():
    data = request.get_json()
    increment = data.get("add", 0)
    eco_points["user"] += increment
    return jsonify({"points": eco_points["user"]})

# Run server
if name == "main":
    app.run(debug=True)