# Step 1: Create a file with the original dictionary
input_filename = 'input_dict.txt'  # Input file name where the original dictionary will be saved
output_filename = 'output_dict.txt'  # Output file name where the inverted dictionary will be written

# Original dictionary
original_dict = {
    'Apple': 'Red',
    'Banana': 'Yellow',
    'Cherry': 'Red',
    'Mango': 'Yellow',
    'Grapes': 'Black, Green'
}

# Write the original dictionary into a file
with open(input_filename, 'w') as file:  # Open the input file in write mode
    # Iterate through the dictionary and write each key-value pair into the file
    for key, value in original_dict.items():
        file.write(f'{key}: {value}\n')  # Write each key-value pair as "key: value" in the file

# Step 2: Read the dictionary from the file
try:
    with open(input_filename, 'r') as file:  # Open the input file in read mode
        input_dict = {}  # Initialize an empty dictionary to store the inverted data
        for line in file:
            # Split each line into key and value
            key, value = line.strip().split(': ')  # Remove extra spaces and split the line by ": "
            # If the value is already a key in the dictionary, append the current key to its value list
            if value in input_dict:
                input_dict[value].append(key)
            else:
                # If the value is not in the dictionary, add it as a new key with the current key in a list
                input_dict[value] = [key]
except FileNotFoundError as e:
    # If the input file is not found, display an error message
    print(f"Error: The file was not found. {e}")
except Exception as e:
    # If any other exception occurs, display the error message
    print(f"An error occurred: {e}")

# Step 3: Write the inverted dictionary to a new file
try:
    with open(output_filename, 'w') as file:  # Open the output file in write mode
        for key, value in input_dict.items():
            # Write each inverted key-value pair to the output file
            file.write(f'{key}: {", ".join(value)}\n')  # Join the list of values with commas and write it
except Exception as e:
    # If there is an error writing to the output file, display the error message
    print(f"Error writing to the file: {e}")

# Print the inverted dictionary to verify the result
print("Inverted Dictionary:")
for key, value in input_dict.items():
    print(f'{key}: {", ".join(value)}')  # Print each inverted key-value pair
