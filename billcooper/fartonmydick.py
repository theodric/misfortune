#!/usr/bin/env python3
import re

# Define the function to add a newline after specific lines
def add_newline_after_quote(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Define the pattern to match lines ending with "-Bill Cooper, 'Behold a Pale Horse'"
    # We use `$` to match the end of the line
    pattern = r"(                -Bill Cooper, 'Behold a Pale Horse')$"
    
    # Use re.sub to replace the match with itself followed by a newline
    # `\1\n` will insert a newline after the matched pattern
    updated_content = re.sub(pattern, r"\1\n", content, flags=re.MULTILINE)
    
    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(updated_content)

# Use the function with your file
add_newline_after_quote('input.txt')
