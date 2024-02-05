import sys
import time

def convert_to_binary_and_hex(input_filename):
    """
    Converts numbers in a file to binary and hexadecimal representations.
    Args:
        input_filename (str): The name of the input file containing numbers.
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            data = input_file.readlines()
            data = [x.strip() for x in data]
            results = []
            for item in data:
                try:
                    num = int(item)
                    binary = bin(num)
                    hexadecimal = hex(num)
                    results.append((item, binary, hexadecimal))
                except ValueError:
                    print(f"Invalid data found: {item}. Skipping...")

            with open("ConversionResults.txt", 'w', encoding='utf-8') as output_file:
                for item, binary, hexadecimal in results:
                    output_file.write(f"{item}: Binary - {binary}, Hexadecimal - {hexadecimal}\n")
                    print(f"{item}: Binary - {binary}, Hexadecimal - {hexadecimal}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py file_with_data.txt")
        sys.exit(1)

    input_filename = sys.argv[1]
    convert_to_binary_and_hex(input_filename)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time elapsed: {elapsed_time} seconds.")
    with open("ConversionResults.txt", 'a', encoding='utf-8') as result_file:
        result_file.write(f"Time elapsed: {elapsed_time} seconds.\n")
