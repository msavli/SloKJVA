import re

def modify_xml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the pattern to search for
    pattern = re.compile(r'(</verse></chapter>)\s*<div type="colophon"[^>]*>([^<]*)</div>', re.DOTALL)

    # Replace the pattern with the desired format
    modified_content = pattern.sub(r'\\cls \2\n\1', content)

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# Example usage
file_path = 'SloKJV_sword.xml'
modify_xml(file_path)

