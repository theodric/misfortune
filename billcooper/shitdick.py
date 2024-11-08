#!/usr/bin/env python3
import re

# Define the function to clean the file content
def remove_likes_pattern(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Join lines into one string so we can work with the entire content
    content = ''.join(lines)
    
    # Define the regex pattern
    # Pattern explanation:
    # - `\d+ likes\nLike\n` will match a line with "number + likes" followed by a line with "Like"
    # - `\d+ likes\nlike\n` will match the same pattern but with "like" in lowercase
    pattern = r"\d+ likes\nLike\n|\d+ likes\nlike\n"
    
    # Use re.sub to replace matched patterns with an empty string
    cleaned_content = re.sub(pattern, "", content)
    
    # Write the cleaned content back to the file
    with open(file_path, 'w') as file:
        file.write(cleaned_content)

# Use the function with your file
remove_likes_pattern('input.txt')

