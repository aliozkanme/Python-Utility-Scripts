import stat
import os
from pathlib import Path

def generate_tree_structure(directory: Path, prefix: str = "", include_hidden: bool = False):
    """
    Recursively traverses the directory to generate a visual tree string.
    
    Logic:
    1. Fetches all entries in the current directory.
    2. Filters out hidden files (dotfiles) unless explicitly requested.
    3. Sorts entries alphabetically to ensure deterministic output.
    4. Iterates through entries, applying proper branch characters (├── or └──).
    5. Recursively calls itself when a directory is encountered to build nested branches.
    """
    tree_str = ""
    
    try:
        # Retrieve all items in the directory
        items = os.listdir(directory)
        
        # Sort items alphabetically for organized visualization
        items.sort()
        
        filtered_items = []
        for item in items:
            path = directory / item
            is_system_hidden = False
            
            try:
                # Retrieve file status to check system attributes
                attrs = os.stat(path)
                
                # Check if the specific FILE_ATTRIBUTE_HIDDEN bit is set (Windows logic)
                if hasattr(attrs, 'st_file_attributes'):
                    is_system_hidden = bool(attrs.st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
                else:
                    # Fallback for Unix-like systems relying on dot prefix convention
                    is_system_hidden = item.startswith('.')
            except OSError:
                # Proceed with default visibility if attribute retrieval fails
                pass

            # Conditional inclusion: Always include if hidden files are requested, otherwise exclude system-hidden files
            if include_hidden or not is_system_hidden:
                filtered_items.append(item)
        
        items = filtered_items
            
    except PermissionError:
        # Handle cases where the script lacks read permissions for a subdirectory
        return f"{prefix}└── [ACCESS DENIED]\n"

    total_items = len(items)
    
    for index, item in enumerate(items):
        path = directory / item
        is_last = (index == total_items - 1)
        
        # Determine the branch connector: └── for the last item, ├── for others
        connector = "└── " if is_last else "├── "
        
        # Append the current item to the tree string
        tree_str += f"{prefix}{connector}{item}\n"
        
        # If the item is a directory, recurse into it
        if path.is_dir():
            # Adjust prefix for the next level: add indentation or vertical bar
            extension = "    " if is_last else "│   "
            tree_str += generate_tree_structure(path, prefix + extension, include_hidden)
            
    return tree_str

def main():
    """
    Main execution flow.
    Handles user input, initializes the root path, and writes the output file.
    """
    # Initialize the current working directory path
    root_path = Path.cwd()
    root_name = root_path.name
    
    # Prompt user via terminal to determine hidden file visibility
    while True:
        user_input = input("Include hidden files (dotfiles)? [y/n]: ").strip().lower()
        if user_input == 'y':
            include_hidden = True
            break
        elif user_input == 'n':
            include_hidden = False
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

    print(f"Generating file tree for: {root_name}...")

    # Build the complete tree string starting with the root directory name
    tree_content = f"{root_name}/\n"
    tree_content += generate_tree_structure(root_path, include_hidden=include_hidden)

    # Define the output filename based on the root directory name
    output_filename = f"{root_name}_FileTree.txt"
    
    # Write the generated content to the file with UTF-8 encoding to support tree characters
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(tree_content)
        print(f"Success! File tree saved to: {output_filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()