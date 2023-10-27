import os
import re
import argparse
from termcolor import colored

def convert_static_links(directory):
    # Define a pattern to find static file links in HTML
    patterns = [
        (r'="(assets/.+?\.(jpg|jpeg|png|gif|svg|ico))"', r'="{% static \'assets/\1\' %}"'),
        (r'="(assets/.+?\.(mp4|webm|ogg))"', r'="{% static \'assets/\1\' %}"'),
        (r'="(assets/.+?\.(js|css))"', r'="{% static \'assets/\1\' %}"')
    ]
    
    # Walk through the directory to get all HTML files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r') as f:
                    content = f.read()
                    
                    # Replace links with Django static format
                    for pattern, replacement in patterns:
                        content = re.sub(pattern, replacement, content)
                
                # Write the modified content back to the file
                with open(filepath, 'w') as f:
                    f.write(content)
                print(colored(f"Processed {filepath}", 'green'))

def main():
    parser = argparse.ArgumentParser(description="Convert static links in HTML files to Django's static format.")
    parser.add_argument('directory', type=str, help="Path to the directory containing the HTML files.")
    
    args = parser.parse_args()
    
    if os.path.exists(args.directory):
        convert_static_links(args.directory)
        print(colored("All files processed successfully!", 'blue', attrs=['bold']))
    else:
        print(colored(f"Directory {args.directory} does not exist!", 'red'))

if __name__ == "__main__":
    main()
