import json
import pandas as pd

def load_data_from_json(file_path):
    """Load travel data from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return None

def process_data(data):
    """Process raw data into a structured format."""
    if not data:
        return None
    
    df = pd.DataFrame(data)
    
    # Ensure required columns exist
    required_columns = {'latitude', 'longitude', 'location_name'}
    if not required_columns.issubset(df.columns):
        print("Error: Missing required data fields.")
        return None
    
    return df
