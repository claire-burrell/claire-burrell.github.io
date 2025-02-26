from scripts.data_loader import load_data
from scripts.map_generator import generate_map
from scripts.map_updater import update_map

def main():
    # Load the data
    travel_data = load_locations()

    # Generate the initial map
    travel_map = generate_map(travel_data)

    # Update the map based on new data
    updated_map = update_map(travel_map)

    # Save the updated map
    updated_map.save("travel_map.html")

if __name__ == "__main__":
    main()
