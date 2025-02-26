from flask import Flask, request, jsonify
import json
from scripts.map_updater import update_travel_data
from scripts.map_generator import generate_map

app = Flask(__name__)

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

        # Update locations.json
        update_travel_data(DATA_FILE, [new_entry])

        # Regenerate the map
        generate_map(DATA_FILE, MAP_FILE)

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

        # Format update entry
        new_entry = {
            "name": updated_entry["name"],
            "coordinates": [updated_entry["latitude"], updated_entry["longitude"]],
            "days": updated_entry["days"],
            "transport": updated_entry["transport"]
        }

        # Update the data file
        update_travel_data(DATA_FILE, [new_entry])

        # Regenerate the map
        generate_map(DATA_FILE, MAP_FILE)

        print("✅ Map updated successfully!")
        return jsonify({"message": "✅ Location updated & map refreshed!"}), 200

    except Exception as e:
        print("❌ Server Error:", e)
        return jsonify({"message": f"❌ Error updating the map: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)


