from data_loader import load_data_from_json, process_data
from map_generator import generate_travel_map
from map_updater import update_travel_data

def main():
    data_file = 'travel_data.json'
    map_output = 'travel_map.html'
    
    # Load and process data
    data = load_data_from_json(data_file)
    processed_data = process_data(data)
    
    # Generate map
    generate_travel_map(processed_data, map_output)
    
    print("Travel map successfully generated.")

if __name__ == "__main__":
    main()
