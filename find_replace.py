#!/usr/bin/env python

import sys

# Set the find and replace text for all occurrences
FIND_REPLACE = {
    'ABC': 'PQR',
    'BCD': 'XY',
    'DEF': 'DFT'
}

# Check if the input file is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python find_replace.py <input_file>")
    sys.exit()

input_file = sys.argv[1]
output_file = input_file + ".out"

# Open the input file for reading
with open(input_file, 'r') as infile:
    # Open the output file for writing
    with open(output_file, 'w') as outfile:
        # Loop through each line in the input file
        for line in infile:
            # Replace all occurrences in the line
            for find_text, replace_text in FIND_REPLACE.items():
                line = line.replace(find_text, replace_text)
            # Write the modified line to the output file
            outfile.write(line)

print("Find and replace operation completed. Output written to", output_file)
