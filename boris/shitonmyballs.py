#!/usr/bin/env python3
# Define file paths
input_file = 'input.txt'  # Replace with your input file name
output_file = 'output.txt'  # Output file name

# Open input file for reading and output file for writing
with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Loop through each line in the input file
    for line in infile:
        # Write the original line to the output file
        outfile.write(line)
        # Add the additional text and newline after each line
        outfile.write("\n            -Boris Johnson\n\n")

print("written to output.txt.")
