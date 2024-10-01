from compress_json import compress, decompress
import json
import os
import zipfile

# Step 1: Read the original large JSON file
with open('large_data.json', 'r') as f:
    data = json.load(f)

# Step 2: Compress the JSON data
compressed = compress(data)  # The result is a compressed list (array)

# Step 3: Write the compressed data to a new JSON file
compressed_file = "compressed_data.json"
with open(compressed_file, "w") as fd:
    fd.write(json.dumps(compressed))  # Convert the compressed list to string and write to file

# Step 4: Get the sizes of both files (original and compressed)
original_file_size = os.path.getsize('large_data.json')  # Size in bytes
compressed_file_size = os.path.getsize(compressed_file)  # Size in bytes

# Convert sizes to MB
original_file_size_mb = original_file_size / (1024 * 1024)
compressed_file_size_mb = compressed_file_size / (1024 * 1024)

# Step 5: Create a ZIP file for the compressed JSON file
zip_file_name = "compressed_data.zip"
with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(compressed_file)

# Step 6: Get the size of the ZIP file
zip_file_size = os.path.getsize(zip_file_name)  # Size in bytes
zip_file_size_mb = zip_file_size / (1024 * 1024)

# Step 7: Print the sizes for comparison
print(f"Original JSON size: {original_file_size_mb:.2f} MB")
print(f"Compressed JSON size: {compressed_file_size_mb:.2f} MB")
print(f"ZIP file size: {zip_file_size_mb:.2f} MB")

# Step 8: Decompress and check if the data remains the same
decompressed = decompress(compressed)
print(f"Decompression successful: {data == decompressed}")  # Should print True
