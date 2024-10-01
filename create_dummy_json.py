import json
import random
import string

# Function to generate random strings
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Function to generate a large JSON structure
def generate_large_json(num_entries=100000, num_nested_entries=10):
    data = {}
    
    for i in range(num_entries):
        entry = {}
        
        # Creating nested entries
        for j in range(num_nested_entries):
            entry[f'nested_entry_{j}'] = {
                "id": i * j,
                "name": random_string(15),
                "value": random.uniform(0, 100),
                "description": random_string(50),
                "active": random.choice([True, False])
            }
        
        data[f'entry_{i}'] = entry
    
    return data

# Generate a large JSON with 100k entries, each having 10 nested entries
large_json = generate_large_json(num_entries=100000, num_nested_entries=10)

# Write the large JSON to a file
with open('large_data.json', 'w') as f:
    json.dump(large_json, f, indent=4)

print("Large JSON file created successfully!")
