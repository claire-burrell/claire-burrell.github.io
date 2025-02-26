import json

CONFIG_PATH = "data/config.json"
LOCATIONS_PATH = "data/locations.json"

def update_travel_data(data_file=LOCATIONS_PATH, new_entries={}):
    """
    Update the travel data JSON file with new entries.

    Parameters:
    - data_file (str): Path to the JSON file containing travel data.
    - new_entries (list of dict): List of new travel data entries. Each entry should be a dictionary 
      with keys 'location_name', 'latitude', and 'longitude'.

    Returns:
    - None (updates the file in place)
    """
    print("✅ Updating locations.json...")
    try:
        # Load existing data
        with open(data_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Append new entries
        if isinstance(data, list):
            data.extend(new_entries)
        else:
            print("Error: Data file format is incorrect. Expected a list of dictionaries.")
            return

        # Save updated data
        with open(data_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

        print(f"Successfully updated {data_file} with new travel entries.")

    except FileNotFoundError:
        print(f"Error: {data_file} not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON in {data_file}. Please check the file format.")

# Wrapper function to maintain compatibility
def update_map(data_file, new_entries):
    update_travel_data(data_file, new_entries)
