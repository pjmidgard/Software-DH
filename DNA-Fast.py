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
    compressed_data = encode_data(data)
    return compressed_data

def extract_data(data):
    extracted_data = decode_data(data)
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

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()