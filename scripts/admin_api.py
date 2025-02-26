from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Import CORS
import json
from scripts.map_updater import update_travel_data
from scripts.map_generator import generate_map

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://claire-burrell.github.io"}})


DATA_FILE = "data/locations.json"
MAP_FILE = "travel_map.html"


@app.route("/add_location", methods=["POST"])
def add_location():
    """Adds a new location and updates the map."""
    try:
        new_location = request.json
        if not all(k in new_location for k in ["name", "latitude", "longitude"]):
            return jsonify({"message": "❌ Missing fields: 'name', 'latitude', or 'longitude'"}), 400

        # Format new entry
        new_entry = {
            "name": new_location["name"],
            "coordinates": [new_location["latitude"], new_location["longitude"]]
        }

        # ✅ Load existing locations to prevent overwriting
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                locations = json.load(file)
                if not isinstance(locations, list):
                    locations = []  # Ensure it's a list
        except (FileNotFoundError, json.JSONDecodeError):
            locations = []

        update_travel_data(DATA_FILE, [new_entry])

        # ✅ Regenerate the map with the correct function call
        generate_map(MAP_FILE)  # 🔥 FIXED

        return jsonify({"message": "✅ Location added successfully!"}), 200

    except Exception as e:
        return jsonify({"message": f"❌ Error: {str(e)}"}), 500


@app.route("/update_map", methods=["POST"])
def update_map():
    """Updates an existing location with new details and regenerates the map."""
    try:
        updated_entry = request.get_json()
        print("📥 Received data:", updated_entry)  # Debugging

        if not all(k in updated_entry for k in ["name", "latitude", "longitude", "days", "transport"]):
            return jsonify({"message": "❌ Missing required fields!"}), 400

        # ✅ Load existing locations
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                locations = json.load(file)
                if not isinstance(locations, list):
                    locations = []
        except (FileNotFoundError, json.JSONDecodeError):
            locations = []

        # ✅ Update the existing entry
        for loc in locations:
            if loc["name"] == updated_entry["name"]:
                loc["coordinates"] = [updated_entry["latitude"], updated_entry["longitude"]]
                loc["days"] = updated_entry["days"]
                loc["transport"] = updated_entry["transport"]
                break
        else:
            return jsonify({"message": "❌ Location not found!"}), 404

        # ✅ Save updated locations
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(locations, file, indent=4)

        # ✅ Regenerate the map with the correct function call
        generate_map(MAP_FILE)  # 🔥 FIXED

        print("✅ Map updated successfully!")
        return jsonify({"message": "✅ Location updated & map refreshed!"}), 200

    except Exception as e:
        print("❌ Server Error:", e)
        return jsonify({"message": f"❌ Error updating the map: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)



