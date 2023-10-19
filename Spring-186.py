#Author Jurijus Pacalovas 
import paq

# Function to reverse specific bit patterns during compression and extraction
def reverse_bits(data):
    reversed_data = data.replace(b'000000000', b'111001101')
    reversed_data = reversed_data.replace(b'111001101', b'000000000')
    reversed_data = reversed_data.replace(b'01011', b'11111')
    reversed_data = reversed_data.replace(b'11111', b'01011')
    reversed_data = reversed_data.replace(b'00000', b'01100')
    reversed_data = reversed_data.replace(b'01100', b'00000')
    reversed_data = reversed_data.replace(b'00001', b'01101')
    reversed_data = reversed_data.replace(b'01101', b'00001')
    reversed_data = reversed_data.replace(b'00010', b'01110')
    reversed_data = reversed_data.replace(b'01110', b'00010')
    reversed_data = reversed_data.replace(b'00011', b'01111')
    reversed_data = reversed_data.replace(b'01111', b'00011')
    reversed_data = reversed_data.replace(b'00100', b'11100')
    reversed_data = reversed_data.replace(b'11100', b'00100')
    reversed_data = reversed_data.replace(b'10', b'11')
    reversed_data = reversed_data.replace(b'00', b'10')
    reversed_data = reversed_data.replace(b'01', b'00')
    reversed_data = reversed_data.replace(b'10', b'00')

    # Add 512 variations (you can extend as needed)
    for i in range(512):
        reversed_data = reversed_data.replace(f'{i:09b}'.encode(), f'{(511 - i):09b}'.encode())

    return reversed_data

# Function to find Pythagorean triples
def find_pythagorean_triples(limit):
    d = 4
    e = 4
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
            if 0 <= component <= 15:
                binary_data += bytes([component])
            else:
                raise ValueError("Triple component out of the valid byte range (0-15)")
    return binary_data

# Function to convert binary data to Pythagorean triples
def binary_to_triples(binary_data):
    triples = []
    current_triple = []

    for value in binary_data:
        current_triple.append(value)
        if len(current_triple) == 1:
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

        # Reverse the first 512 bits
        input_data = reverse_bits(input_data)

        # Step 1: Find Pythagorean triples within the specified limit (256 in this case)
        limit = 256
        triples = find_pythagorean_triples(limit)

        # Step 2: Apply your formula to each element of triples (if needed)

        # Step 3: Convert Pythagorean triples to binary data
        binary_data = triples_to_binary(triples)

        # Step 4: Append binary data to the original input data
        input_data += binary_data

        # Step 5: Compress the combined data using Paq
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

        # Reverse the first 512 bits
        decompressed_data = reverse_bits(decompressed_data)

        # Step 3: Find binary data that represents Pythagorean triples
        binary_data = decompressed_data[-(len(triples) * 1):]  # Assuming each triple is 1 byte

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
