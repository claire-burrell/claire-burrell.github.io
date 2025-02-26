import folium
from scripts.data_loader import load_config, load_locations

def generate_map(output_path="travel_map.html"):
    """Generates an interactive travel map using folium."""

    print("✅ Regenerating travel_map.html...")
    # Load settings from config.json
    config = load_config()
    locations = load_locations()

    map_center = config.get("center_coordinates", [0, 0])
    default_zoom = config.get("default_zoom", 4)
    marker_color = config.get("marker_color", "blue")
    line_color = config.get("line_color", "red")

    # Create a map centered at the specified coordinates
    travel_map = folium.Map(location=map_center, zoom_start=default_zoom)

    # Add markers for each location
    travel_route = []
    for location in locations:
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

# Run the script only if executed directly
if __name__ == "__main__":
    generate_map()
