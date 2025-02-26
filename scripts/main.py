from scripts.data_loader import DataLoader
from scripts.map_generator import MapGenerator
from scripts.map_updater import update_travel_data

def main():

    # Load existing locations
    data_file = "data/locations.json"
    locations = DataLoader.load_locations(data_file)


    
    # Load the data
    travel_data = DataLoader.load_locations()

    

    # Update the map based on new data
    update_travel_data(data_file, new_entries)

    # Save the updated map
    MapGenerator.generate_map(data_file, "travel_map.html")

if __name__ == "__main__":
    main()
