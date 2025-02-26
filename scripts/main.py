from scripts.data_loader import load_locations
from scripts.map_generator import generate_map
from scripts.map_updater import update_travel_data

def main():

    # Load existing locations
    data_file = "data/locations.json"
    locations = load_locations()    

    # Update the map based on new data
    update_travel_data()

    # Save the updated map
    generate_map(data_file, "travel_map.html")

if __name__ == "__main__":
    main()
