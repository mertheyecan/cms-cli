import argparse
from template_converter import convert_static_links
from termcolor import colored
import os 

def template_convert(directory):
    if os.path.exists(directory):
        convert_static_links(directory)
        print(colored("All files processed successfully!", 'blue', attrs=['bold']))
    else:
        print(colored(f"Directory {directory} does not exist!", 'red'))

def main():
    parser = argparse.ArgumentParser(description="CMS CLI Commands.")
    
    subparsers = parser.add_subparsers(dest="command", title="Commands", description="Available CLI commands")

    # Command: template_convert
    template_convert_parser = subparsers.add_parser("template_convert", help="Convert static links in HTML files to Django's static format.")
    template_convert_parser.add_argument('directory', type=str, help="Path to the directory containing the HTML files.")

    # Add more commands as needed
    # Example: another_command_parser = subparsers.add_parser("another_command", help="Description of another command.")
    
    args = parser.parse_args()

    if args.command == "template_convert":
        template_convert(args.directory)
    # elif args.command == "another_command":
    #     another_command_function(args.some_argument)

if __name__ == "__main__":
    main()