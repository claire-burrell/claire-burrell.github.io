import json
import os

CONFIG_PATH = "data/config.json"
LOCATIONS_PATH = "data/locations.json"

def load_config(config_path=CONFIG_PATH):
    """Loads map settings from config.json."""
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        print("⚠️ Warning: config.json not found. Using default settings.")
        return {
            "map_title": "My Travel Map",
            "default_zoom": 4,
            "center_coordinates": [0, 0],  # Default to world view
            "marker_color": "blue",
            "line_color": "red",
            "update_frequency": "daily",
            "backup_enabled": True
        }

def load_locations(locations_path=LOCATIONS_PATH):
    """Loads travel locations from locations.json."""
    if os.path.exists(locations_path):
        with open(locations_path, "r", encoding="utf-8") as file:
            return json.load(file)
    else:
        print("⚠️ Warning: locations.json not found. No locations loaded.")
        return []

def save_config(config, config_path=CONFIG_PATH):
    """Saves updated map settings to config.json."""
    try:
        with open(config_path, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        print(f"❌ Error: Could not save config.json: {e}")

def save_locations(locations, locations_path=LOCATIONS_PATH):
    """Saves updated travel locations to locations.json."""
    try:
        with open(locations_path, "w", encoding="utf-8") as file:
            json.dump(locations, file, indent=4)
    except Exception as e:
        print(f"❌ Error: Could not save locations.json: {e}")


    def get_locations(self):
        return self.locations
