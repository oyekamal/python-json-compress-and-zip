# Json compress and zip


# JSON Compression and Zipping Results

This project demonstrates the process of compressing a large JSON file, further compressing it by zipping, and comparing the sizes before and after compression.

## Project Overview

The steps in this project include:
1. **Reading a large JSON file (`large_data.json`)**.
2. **Compressing the JSON data** using the `compress_json` library.
3. **Writing the compressed JSON data** to a file (`compressed_data.json`).
4. **Creating a ZIP archive** of the compressed JSON file.
5. **Calculating the size** of the original, compressed, and zipped files.
6. **Ensuring data integrity** by verifying that the decompressed data matches the original.

## Compression Steps

1. **Original JSON**: The large JSON file is read from `large_data.json`.
2. **Compressing**: The `compress_json` library is used to compress the data into a more compact format, which is then written to `compressed_data.json`.
3. **Zipping**: The compressed JSON file is zipped using Python's `zipfile` module.
4. **Decompression**: The compressed data is decompressed to ensure it matches the original data.

## Findings

After following the steps above, here are the results for file sizes:

- **Original JSON size**: `242.76 MB`
- **Compressed JSON size**: `128.83 MB`
- **ZIP file size**: `77.73 MB`

## Conclusion

- Compressing the JSON using `compress_json` reduced the file size from 242.76 MB to 128.83 MB, approximately a **47% reduction**.
- Further zipping the compressed JSON reduced the file size to 77.73 MB, resulting in an overall reduction of approximately **68%** compared to the original size.

## Is This Compression Library Available in JavaScript?

Yes, the `compress-json` library is available for both **Python** and **JavaScript**.

- **Python Version**: You can find the Python version of the `compress-json` library on PyPI:
  [compress-json-python on PyPI](https://pypi.org/project/compress-json-python/)

- **JavaScript Version**: You can find the JavaScript version of the `compress-json` library on npm:
  [compress-json on npm](https://www.npmjs.com/package/compress-json)

## How to Run

1. Install the required library:
   ```bash
   pip install compress-json
