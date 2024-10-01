const fs = require('fs');
const compressJson = require('compress-json');

// Step 1: Read the compressed JSON data from the file
fs.readFile('compressed_data.json', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading the compressed file:', err);
        return;
    }

    // Step 2: Parse the compressed data (it is stored as a string in an array)
    const compressedData = JSON.parse(data);

    // Step 3: Decompress the JSON data
    const decompressedData = compressJson.decompress(compressedData);

    // Step 4: Write the original data back to a new JSON file
    fs.writeFile('original_data.json', JSON.stringify(decompressedData, null, 2), (err) => {
        if (err) {
            console.error('Error writing the original data to file:', err);
            return;
        }
        console.log('Original data has been successfully reconstructed and saved as original_data.json');
    });
});
