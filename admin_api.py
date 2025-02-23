from flask import Flask, request, jsonify
from data_class import TravelData

app = Flask(__name__)
travel_data = TravelData("travel_data.pkl")  # Load travel data

@app.route("/update_map", methods=["POST"])
def update_map():
    data = request.json
    name = data.get("name")
    country = data.get("country")
    days = int(data.get("days", 0))
    transport = data.get("transport", "Unknown")

    if name and country and days:
        travel_data.add_location(name, country, days, transport)
        return jsonify({"message": "Travel data updated successfully."})
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
