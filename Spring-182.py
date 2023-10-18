import paq

# Function to find Pythagorean triples
def find_pythagorean_triples(limit):
    d = 2
    e = 2
    f = 1
    g = 1
    triples = []
    for a in range(1, limit - f):
        for b in range(a, limit + g):
            c = (a**d + b**e)
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
            if 0 <= component <= 15:
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

# Initialize X1, X2, and X3
X1 = 0
X2 = 0
X3 = 0

# Variables to store saved values
saved_X1 = None
saved_X2 = None

# Algorithm for X1-X3 with 24-bit blocks
def compress_X1_X3(data):
    global X1, X2, X3, saved_X1, saved_X2  # Declare the variables as global

    compressed_data = b""
    count = 1
    prev_bit = data[0]

    for bit in data[1:]:
        if bit == prev_bit:
            count += 1
        else:
            compressed_data += bytes([prev_bit]) + bytes([count])  # Store the bit and count
            prev_bit = bit
            count = 1

        X1 += 1
        X3 += 1

        if X1 == 2**23:
            saved_X1 = X1
            saved_X2 = X2
            count = 1  # Reset count after saving values

        if X2 == 1:
            X2 = 0

        if X3 == 2**24:  # Check if X3 reaches the maximum value
            X3 = 0

    compressed_data += bytes([prev_bit]) + bytes([count])  # Store the final bit and count
    return compressed_data

# Function to convert Pythagorean triples to binary data
def triples_to_binary(triples):
    binary_data = b''
    for triple in triples:
        for component in triple:
            if 0 <= component <= 15:
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
        if len(current_triple) == 4:
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
    output_file_name = input_file_name + ".compressed"

    try:
        with open(input_file_name, 'rb') as input_file:
            input_data = input_file.read()

        # Step 1: Find Pythagorean triples within a certain limit (2^24)
        limit = 15  # Adjust the limit as needed
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

        print("Data successfully compressed and saved to '{0}'.".format(output_file_name))
    except IOError:
        print("Error: File not found.")

elif option == "2":
    # Extraction and Save
    input_file_name = input("Enter the name of the compressed file for extraction: ")
    output_file_name = input("Enter the name for the extracted file: ")

    try:
        with open(input_file_name, 'rb') as input_file:
            paq_compressed_data = input_file.read()

        # Step 1: Decompress the Paq compressed data
        decompressed_data = paq.decompress(paq_compressed_data)
    
        # Step 2: Extract binary data representing Pythagorean triples
        binary_data = decompressed_data[-(len(triples) * 4):]  # Assuming each triple is 3 bytes

        # Step 3: Convert binary data back to Pythagorean triples
        extracted_triples = binary_to_triples(binary_data)

        # Save the extracted Pythagorean triples as a binary file
        with open(output_file_name, 'wb') as extracted_file:
            for triple in extracted_triples:
                extracted_file.write(bytes(triple))

        print("Data successfully extracted and saved to '{0}'.".format(output_file_name))
    except IOError:
        print("Error: File not found.")

else:
    print("Invalid option. Please select 1 for Compression and Save or 2 for Extraction and Save.")