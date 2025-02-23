import folium

def generate_travel_map(data, output_file="travel_map.html"):
    """
    Generate a travel map from processed data and save it as an HTML file.

    Parameters:
    - data (pd.DataFrame): DataFrame containing 'latitude', 'longitude', and 'location_name' columns.
    - output_file (str): Name of the output HTML file.
    """
    if data is None or data.empty:
        print("Error: No valid data provided to generate the map.")
        return
    
    # Determine the center of the map
    center_lat = data["latitude"].mean()
    center_lon = data["longitude"].mean()
    
    # Initialize the map
    travel_map = folium.Map(location=[center_lat, center_lon], zoom_start=5)

    # Add markers
    for _, row in data.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=row["location_name"],
            tooltip=row["location_name"]
        ).add_to(travel_map)
    
    # Save the map to an HTML file
    travel_map.save(output_file)
    print(f"Map saved as {output_file}.")
