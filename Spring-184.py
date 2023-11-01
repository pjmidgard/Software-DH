#Author Jurijus Pacalovas 
import paq

# Function to reverse specific bit patterns during compression and extraction
def reverse_bits(data):
    reversed_data = data.replace(b'00000000', b'111001001')
    reversed_data = reversed_data.replace(b'11010', b'11111')
    reversed_data = reversed_data.replace(b'11111', b'11010')
    reversed_data = reversed_data.replace(b'111001001', b'00000000')
    return reversed_data

# Function to find Pythagorean triples
def find_pythagorean_triples(limit):
    d = 2
    e = 2
    f = 1
    g = 1
    triples = []
    for a in range(1, limit - f):
        for b in range(a, limit + g):
            c = (a ** d + b ** e)
            f += 1
            g += 1
            d += 1
            e += 1
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
                raise ValueError("Triple component out of the valid byte range (0-255)")
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
    output_file_name = input_file_name + ".bin"

    try:
        with open(input_file_name, 'rb') as input_file:
            input_data = input_file.read()

        # Reverse specific bit patterns
        input_data = reverse_bits(input_data)

        # Set the limit for finding Pythagorean triples to 7
        limit = 256 # Adjust the limit as needed

        # Step 1: Find Pythagorean triples within the specified limit
        triples = find_pythagorean_triples(limit)

        # Step 2: Convert Pythagorean triples to binary data
        binary_data = triples_to_binary(triples)

        # Step 3: Append binary data to the original input data
        input_data += binary_data

        # Step 4: Compress the combined data using Paq
        paq_compressed_data = paq.compress(input_data)

        # Save the Paq compressed data to the specified file in binary mode ('wb')
        with open(output_file_name, 'wb') as compressed_file:
            compressed_file.write(paq_compressed_data)

        print(f"Data successfully compressed and saved to '{output_file_name}'.")
    except FileNotFoundError:
        print(f"Error: File not found.")

elif option == "2":
    # Extraction and Save
    input_file_name = input("Enter the name of the input compressed file for extraction: ")
    input_file_name_long = len(input_file_name)
    if input_file_name[input_file_name_long - 4:] != ".bin":
        print("Sorry, This is not a binary file!")
    else:
        output_file_name = input_file_name[:input_file_name_long - 4]

    try:
        with open(input_file_name, 'rb') as input_file:
            paq_compressed_data = input_file.read()

        # Step 1: Decompress the Paq compressed data
        decompressed_data = paq.decompress(paq_compressed_data)

        # Reverse specific bit patterns
        decompressed_data = reverse_bits(decompressed_data)

        # Set the limit for finding Pythagorean triples to 7
        limit = 256  # Adjust the limit as needed

        # Step 3: Find binary data that represents Pythagorean triples
        binary_data = decompressed_data[-(len(triples) * 3):]  # Assuming each triple is 3 bytes

        # Step 4: Convert binary data back to Pythagorean triples
        extracted_triples = binary_to_triples(binary_data)

        # Print the extracted triples
        print("Extracted Pythagorean Triples:")
        #for triple in extracted_triples:
            #print(triple)

        print("Data successfully extracted.")
    except FileNotFoundError:
        print(f"Error: File not found.")
else:
    print("Invalid option. Please select 1 for Compression and Save or 2 for Extraction and Save.")
