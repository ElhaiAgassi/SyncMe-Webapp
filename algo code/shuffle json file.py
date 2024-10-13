import json
import random

# Function to read the JSON lines from the file
def read_json_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# Function to shuffle the lines
def shuffle_lines(lines):
    random.shuffle(lines)
    return lines

# Function to write the shuffled lines back to a new file
def write_json_lines(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

# Path to your input and output files
input_file_path = 'data_pool_2/data4.json'
output_file_path = 'data_pool_2/suffle.json'

# Read, shuffle, and write the JSON lines
lines = read_json_lines(input_file_path)
shuffled_lines = shuffle_lines(lines)
write_json_lines(output_file_path, shuffled_lines)

print(f"Shuffled lines have been written to {output_file_path}")
