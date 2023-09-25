#DNA algorothm: Need to take 28 bits and compress 27 or 29 bits for 27  do it again two times need to find two-five 4 bits variation the same  count space before and after by save 0-7 in three bits or save 0-7 3-5  like this 0, 10,11 and three bits use the same for 28-256 bits on top that I was mean algorithm  before and 4 or 2-4 or 2-256 add 0,01,11 mean about 4 bits add 01-00000001 on the start for compression 000-111 size of block that compress from (28*1)-(28*8) size bits write code compression and extract add extra bits how many need use base of 10 range namber 0-256 in t to binary save options compress  or extract c or e to ask  what name name file compression and save write full code of compression and extract add afte predict 0-256 for compression variationns and befor predict 0-256 variations before full code Add for compression three 28-256 while get 25 use the for 28-256 bits Need to take 28 bits and compress 27 or 29 bits for 27  do it again two times need to find two-five 4 bits variation the same  count space before and after by save 0-7 in three bits or save 0-7 2-5  like this 0, 10,11 and three bits use the same for 28-256 bits on top that I was mean algorithm  before and 4 or 2-4 or 2-256 add 0,01,11 mean about 4 bits add 01-00000001 on the start for compression 000-111 size of block that compress from (28*1)-(28*8) size bits write code compression and extract add extra bits how many need use base of 10 range namber 0-256 in t to binary save options compress  or extract c or e to ask  what name name file compression and save write full code of compression and extract add afte predict 0-256 for compression variationns and befor predict 0-256 variations before full code ask name file and compress binary and extract options full code compression and extract in python.Add Use 28-256bits compression and 000-111 28*1-28*8 and 28-256 compression and extract full code 3 times compress 5 bytes 258*4 and 258 the data DNA algorithm and prng and calculus.
#@Author Jurijus Pacalovas 
import os

# Define a dictionary for encoding and decoding
encoding_dict = {
    b'0': b'000',
    b'1': b'111',
    b'00': b'010',
    b'01': b'001',
    b'10': b'110',
    b'11': b'101'
}

def encode_data(data):
    encoded_data = b""
    for byte in data:
        encoded_data += encoding_dict.get(bytes([byte]), bytes([byte]))
    return encoded_data

def decode_data(data):
    decoded_data = b""
    while data:
        for key in encoding_dict.keys():
            if data.startswith(key):
                decoded_data += encoding_dict[key]
                data = data[len(key):]
                break
        else:
            decoded_data += data[0:3]  # Append the first 3 characters (encoded '0' or '1')
            data = data[3:]
    return decoded_data

def compress_data(data):
    # Save original file size as metadata
    original_size = len(data).to_bytes(4, byteorder='big')
    compressed_data = original_size + encode_data(data)
    return compressed_data

def extract_data(data):
    # Extract original file size from metadata
    original_size = int.from_bytes(data[:4], byteorder='big')
    decoded_data = decode_data(data[4:])
    # Ensure the extracted data is cut to the correct size
    extracted_data = decoded_data[:original_size]
    return extracted_data

def main():
    while True:
        print("Options:")
        print("1. Compression")
        print("2. Extraction")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_filename = input("Enter the name of the file containing binary data for compression: ")

            try:
                with open(input_filename, 'rb') as file:
                    original_data = file.read()
            except FileNotFoundError:
                print(f"File '{input_filename}' not found. Please provide a valid file.")
                continue

            # Compress the data
            compressed_data = compress_data(original_data)

            output_filename = input("Enter the name of the compressed file (e.g., 111.bin): ")

            try:
                with open(output_filename, 'wb') as file:
                    file.write(compressed_data)
            except FileNotFoundError:
                print(f"Unable to save the compressed data to '{output_filename}'. Please provide a valid file path.")

            print(f"Compression complete. Data saved to '{output_filename}'.")
            print(f"Original file size: {len(original_data)} bytes")
            print(f"Compressed file size: {len(compressed_data)} bytes")

        elif choice == '2':
            input_filename = input("Enter the name of the file containing compressed data for extraction: ")

            try:
                with open(input_filename, 'rb') as file:
                    compressed_data = file.read()
            except FileNotFoundError:
                print(f"File '{input_filename}' not found. Please provide a valid file.")
                continue

            # Extract the data
            extracted_data = extract_data(compressed_data)

            output_filename = input("Enter the name of the extracted file (e.g., 111111111.bin): ")

            try:
                with open(output_filename, 'wb') as file:
                    file.write(extracted_data)
            except FileNotFoundError:
                print(f"Unable to save the extracted data to '{output_filename}'. Please provide a valid file path.")

            print(f"Extraction complete. Data saved to '{output_filename}'.")
            print(f"Original file size: {len(extracted_data)} bytes")

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
