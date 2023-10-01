import zstandard as zstd
import paq
#Author Jurijus Pacalovas 
# Function to find Pythagorean triples
def find_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c = (a**2 + b**2)
            if isinstance(c, float) and c.is_integer():
                triples.append((a, b, int(c)))
    return triples

# Function to convert Pythagorean triples to binary data
def triples_to_binary(triples):
    binary_data = b''
    for triple in triples:
        for component in triple:
            if 0 <= component <= 255:
                binary_data += bytes([component])
            else:
                raise ValueError("Triple component out of valid byte range (0-255)")
    return binary_data

# Function to convert binary data to Pythagorean triples
def binary_to_triples(binary_data):
    triples = []
    current_triple = []

    for value in binary_data:
        current_triple.append(value)
        if len(current_triple) == 3:
            triples.append(tuple(current_triple))
            current_triple = []

    return triples

# Initialize the 'triples' variable to an empty list
triples = []

# Ask the user for options
print("Options:")
print("1. Compression and Save")
print("2. Extraction and Save")
option = input("Select an option (1 or 2): ")

if option == "1":
    # Compression and Save
    input_file_name = input("Enter the name of the input file for compression: ")
    output_file_name = input("Enter the name of the output compressed file: ")

    try:
        with open(input_file_name, 'rb') as input_file:
            input_data = input_file.read()

        # Step 1: Find Pythagorean triples within a certain limit (2^24)
        limit = (2**24)-1 # Adjust the limit as needed
        triples = find_pythagorean_triples(limit)

        # Step 2: Convert Pythagorean triples to binary data
        binary_data = triples_to_binary(triples)

        # Step 3: Append binary data to the original input data
        input_data += binary_data

        # Step 4: Compress the combined data using Zstd
        cctx = zstd.ZstdCompressor()
        zstd_compressed_data = cctx.compress(input_data)

        # Step 5: Compress the Zstd compressed data using Paq
        paq_compressed_data = paq.compress(zstd_compressed_data)

        # Save the Paq compressed data to the specified file in binary mode ('wb')
        with open(output_file_name, 'wb') as compressed_file:
            compressed_file.write(paq_compressed_data)

        print(f"Data successfully compressed and saved to '{output_file_name}'.")
    except FileNotFoundError:
        print(f"Error: File not found.")

elif option == "2":
    # Extraction and Save
    input_file_name = input("Enter the name of the input compressed file for extraction: ")
    output_file_name = input("Enter the name of the output extracted file: ")

    try:
        with open(input_file_name, 'rb') as input_file:
            paq_compressed_data = input_file.read()

        # Step 1: Decompress the Paq compressed data
        zstd_compressed_data = paq.decompress(paq_compressed_data)

        # Step 2: Decompress the Zstd compressed data
        dctx = zstd.ZstdDecompressor()
        decompressed_data = dctx.decompress(zstd_compressed_data)

        # Step 3: Find binary data that represents Pythagorean triples
        binary_data = decompressed_data[-(len(triples) * 3):]  # Assuming each triple is 3 bytes

        # Step 4: Convert binary data back to Pythagorean triples
        extracted_triples = binary_to_triples(binary_data)

        # Save the extracted Pythagorean triples as a binary file
        with open(output_file_name, 'wb') as extracted_file:
            for triple in extracted_triples:
                extracted_file.write(bytes(triple))

        print(f"Data successfully extracted and saved to '{output_file_name}'.")
    except FileNotFoundError:
        print(f"Error: File not found.")

else:
    print("Invalid option. Please select 1 for Compression and Save or 2 for Extraction and Save.")
