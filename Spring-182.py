import paq

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
    count = 0  # Initialize count to 0
    prev_bit = data[0]

    for bit in data:
        if bit == prev_bit:
            count += 1
            if count == 256:  # Check if count reaches 256 (one-byte limit)
                compressed_data += bytes([prev_bit]) + bytes([255])
                count = 0  # Reset count after reaching 256
        else:
            compressed_data += bytes([prev_bit]) + bytes([count])  # Store the bit and count
            prev_bit = bit
            count = 1

        X1 += 1
        X3 += 1

        if X1 == 2**23:
            saved_X1 = X1
            saved_X2 = X2
            count = 0  # Reset count after saving values

        if X2 == 1:
            X2 = 0

        if X3 == 2**24:  # Check if X3 reaches the maximum value
            X3 = 0

    compressed_data += bytes([prev_bit]) + bytes([count])  # Store the final bit and count
    return compressed_data

# Algorithm for X3 with 24-bit blocks
def extract_X3(data):
    global X3  # Declare X3 as global

    extracted_data = b""
    i = 0

    while i < len(data):
        bit = data[i]
        i += 1
        count = data[i]
        i += 1

        extracted_data += bytes([bit]) * count

        X3 += 1

        if X3 == 2**24:  # Check if X3 reaches the maximum value
            X3 = 0

    return extracted_data

user_option = input("Choose an option: (1) Compress (2) Extract: ")

if user_option == '1':
    user_file_name = input("Enter the binary data file you want to compress: ")

    with open(user_file_name, 'rb') as file:
        data = file.read()

    compressed_data = compress_X1_X3(data)

    if compressed_data is not None:
        compressed_file_name = input("Enter the name of the compressed file: ")

        compressed_data = paq.compress(compressed_data)

        with open(f'{compressed_file_name}.compressed', 'wb') as compressed_file:
            compressed_file.write(compressed_data)

elif user_option == '2':
    user_file_name = input("Enter the name of the compressed file you want to extract: ")

    with open(user_file_name, 'rb') as file:
        compressed_data = file.read()

    decompressed_data = paq.decompress(compressed_data)

    extracted_data = extract_X3(decompressed_data)

    if extracted_data is not None:
        extracted_file_name = input("Enter the name of the extracted file: ")

        with open(f'{extracted_file_name}.extracted', 'wb') as extracted_file:
            extracted_file.write(extracted_data)

if saved_X1 is not None and saved_X2 is not None:
    print(f"Saved X1: {saved_X1}, Saved X2: {saved_X2}")