import json
import os

class DataLoader:
    def __init__(self, config_path="data/config.json", locations_path="data/locations.json"):
        self.config_path = config_path
        self.locations_path = locations_path
        self.config = self.load_config()
        self.locations = self.load_locations()

    def load_config(self):
        """Loads map settings from config.json."""
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as file:
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

    def load_locations(self):
        """Loads travel locations from locations.json."""
        if os.path.exists(self.locations_path):
            with open(self.locations_path, "r", encoding="utf-8") as file:
                return json.load(file)
        else:
            print("⚠️ Warning: locations.json not found. No locations loaded.")
            return []

    def get_config(self):
        return self.config

    def get_locations(self):
        return self.locations
