from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ Import CORS
import json
from scripts.map_updater import update_travel_data
from scripts.map_generator import generate_map

app = Flask(__name__)

# ✅ STRONGER CORS CONFIGURATION
CORS(app, resources={r"/*": {"origins": "https://claire-burrell.github.io"}}, supports_credentials=True)

DATA_FILE = "data/locations.json"
MAP_FILE = "travel_map.html"

def load_locations():
    """Loads existing locations from JSON file, or returns an empty list if missing/corrupt."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            locations = json.load(file)
            if isinstance(locations, list):
                return locations
            else:
                print("⚠️ JSON data is not a list. Resetting to empty list.")
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠️ locations.json not found or unreadable. Resetting to empty list.")
        return []

def save_locations(locations):
    """Saves locations back to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(locations, file, indent=4)
        print("✅ Locations saved successfully.")
    except Exception as e:
        print(f"❌ Error saving locations: {str(e)}")

@app.route("/add_location", methods=["POST"])
def add_location():
    """Adds a new location and updates the map."""
    try:
        new_location = request.json
        if not all(k in new_location for k in ["name", "latitude", "longitude"]):
            return jsonify({"message": "❌ Missing fields: 'name', 'latitude', or 'longitude'"}), 400

        # ✅ Load existing locations to prevent overwriting
        locations = load_locations()

        # ✅ Format new entry
        new_entry = {
            "name": new_location["name"],
            "coordinates": [float(new_location["latitude"]), float(new_location["longitude"])]
        }

        # ✅ Add new location & save
        locations.append(new_entry)
        save_locations(locations)

        # ✅ Regenerate the map
        generate_map(MAP_FILE)

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
        locations = load_locations()

        # ✅ Update the existing entry
        for loc in locations:
            if loc["name"] == updated_entry["name"]:
                loc["coordinates"] = [float(updated_entry["latitude"]), float(updated_entry["longitude"])]
                loc["days"] = updated_entry["days"]
                loc["transport"] = updated_entry["transport"]
                break
        else:
            return jsonify({"message": "❌ Location not found!"}), 404

        # ✅ Save updated locations
        save_locations(locations)

        # ✅ Regenerate the map
        generate_map(MAP_FILE)

        print("✅ Map updated successfully!")
        return jsonify({"message": "✅ Location updated & map refreshed!"}), 200

    except Exception as e:
        print("❌ Server Error:", e)
        return jsonify({"message": f"❌ Error updating the map: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)


