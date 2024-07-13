import os
import argparse
from InquirerPy import inquirer
import pyperclip

def list_directories(root_dir):
    directories = []
    for root, dirs, files in os.walk(root_dir):
        for dir in dirs:
            directories.append(os.path.join(root, dir))
    return directories

def generate_tree_and_extract_code(root_dir, include_dirs, output_file):
    tree_output = []
    code_output = []

    def traverse_directory(current_dir, indent=""):
        entries = sorted(os.listdir(current_dir))
        for i, entry in enumerate(entries):
            entry_path = os.path.join(current_dir, entry)
            if os.path.isdir(entry_path):
                if any(entry_path.startswith(include) for include in include_dirs):
                    tree_output.append(f"{indent}├── {entry}")
                    traverse_directory(entry_path, indent + "│   ")
            else:
                if entry.endswith(('.ts', '.tsx', '.js', '.jsx', '.mjs')):
                    tree_output.append(f"{indent}├── {entry}")
                    with open(entry_path, 'r') as file:
                        code_output.append(f"\n{entry_path}:\n{file.read()}")

    traverse_directory(root_dir)

    output_content = "\n".join(tree_output) + "\n" + "\n".join(code_output)
    
    with open(output_file, 'w') as output:
        output.write(output_content)
    
    pyperclip.copy(output_content)

def main():
    parser = argparse.ArgumentParser(description="Directory tree and code extractor.")
    parser.add_argument("root_dir", type=str, help="The root directory to start the extraction from.")
    parser.add_argument("output_file", type=str, help="The output file to save the result.")
    
    args = parser.parse_args()

    directories = list_directories(args.root_dir)
    selected_dirs = inquirer.checkbox(
        message="Select directories to include:",
        choices=directories
    ).execute()

    generate_tree_and_extract_code(args.root_dir, selected_dirs, args.output_file)
    print(f"Output saved to {args.output_file} and copied to clipboard.")

if __name__ == "__main__":
    main()
