import folium
from data_loader import DataLoader

class MapGenerator:
    def __init__(self):
        self.data_loader = DataLoader()
        self.config = self.data_loader.get_config()
        self.locations = self.data_loader.get_locations()

    def generate_map(self, output_path="travel_map.html"):
        """Generates an interactive travel map using folium."""
        # Load settings from config.json
        map_center = self.config.get("center_coordinates", [0, 0])
        default_zoom = self.config.get("default_zoom", 4)
        marker_color = self.config.get("marker_color", "blue")
        line_color = self.config.get("line_color", "red")

        # Create a map centered at the specified coordinates
        travel_map = folium.Map(location=map_center, zoom_start=default_zoom)

        # Add markers for each location
        travel_route = []
        for location in self.locations:
            lat, lon = location["coordinates"]
            name = location["name"]
            folium.Marker([lat, lon], popup=name, icon=folium.Icon(color=marker_color)).add_to(travel_map)
            travel_route.append([lat, lon])

        # Draw lines connecting travel locations
        if len(travel_route) > 1:
            folium.PolyLine(travel_route, color=line_color, weight=2.5, opacity=0.8).add_to(travel_map)

        # Save the generated map
        travel_map.save(output_path)
        print(f"✅ Travel map successfully generated: {output_path}")

# Run the script
if __name__ == "__main__":
    generator = MapGenerator()
    generator.generate_map()
