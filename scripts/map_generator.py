import folium
from data_class import TravelData

def generate_map():
    travel_data = TravelData("travel_data.pkl")
    locations = travel_data.data

    if not locations:
        print("No locations to display.")
        return

    first_location = list(locations.values())[0]
    travel_map = folium.Map(location=[first_location[1], first_location[2]], zoom_start=5)

    for name, details in locations.items():
        folium.Marker(
            location=[details[1], details[2]],
            popup=f"{name} ({details[0]}) - {details[3]} days",
            tooltip=name
        ).add_to(travel_map)

    travel_map.save("travel_map.html")
    print("✅ Travel map updated!")

if __name__ == "__main__":
    generate_map()
