from scripts.data_loader import load_locations
from scripts.map_generator import generate_map
from scripts.map_updater import update_travel_data

def main():
    """Main function to update travel data and generate the map."""

    # Load existing locations
    locations = load_locations()    

    # Update the travel data file (if needed)
    update_travel_data()

    # Generate and save the updated travel map
    generate_map("travel_map.html")

if __name__ == "__main__":
    main()
