import os
import re

# ==========================================
# CONFIGURATION
# ==========================================

# List of Markdown files to process.
TARGET_FILES = ["example_tr.md", "subfolder/example_eng.md"]

# List of directories to search for source code files.
# The script will look for the file in these folders sequentially.
SEARCH_PATHS = [".", "src"]

# Map file extensions to Markdown syntax highlighting tags.
EXT_MAP = {
    ".py": "python",
    ".m": "matlab",
    ".js": "javascript",
    ".c": "c",
    ".cpp": "cpp",
    ".java": "java",
    ".html": "html",
    ".css": "css",
    ".sh": "bash",
    ".json": "json",
    ".xml": "xml",
    ".md": "markdown",
    ".yml": "yaml",
    ".yaml": "yaml"
}

# ==========================================
# HELPER FUNCTIONS
# ==========================================

def get_language_tag(filepath):
    """
    Determines the Markdown language tag based on the file extension.
    """
    _, ext = os.path.splitext(filepath)
    return EXT_MAP.get(ext.lower(), "text")

def find_and_read_file(filename):
    """
    Searches for the filename in all SEARCH_PATHS.
    Returns the content of the first match found.
    """
    for path in SEARCH_PATHS:
        full_path = os.path.join(path, filename)
        if os.path.exists(full_path):
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    return f.read().strip()
            except Exception as e:
                print(f"[ERROR] Found but failed to read {full_path}: {e}")
                return f"> **ERROR:** Read permission failed for '{filename}'."
    
    # If loop finishes without returning
    print(f"[WARNING] File '{filename}' not found in any search path.")
    return f"> **ERROR:** File '{filename}' not found in search paths."

def generate_folder_index(target_dir):
    """
    Scans the specified target_dir and generates a Markdown list of files/folders.
    """
    # Remove quotes if present (e.g., from regex capture)
    target_dir = target_dir.strip('"\'')
    
    if not os.path.exists(target_dir):
        return f"> **ERROR:** Directory '{target_dir}' not found."

    try:
        items = sorted(os.listdir(target_dir))
    except Exception as e:
        return f"> **ERROR:** Could not list directory '{target_dir}': {e}"

    index_lines = []
    
    for item in items:
        # Ignore hidden files/folders
        if item.startswith("."):
            continue
            
        item_path = os.path.join(target_dir, item)
        
        # Add a trailing slash for directories to distinguish them visually
        display_name = item if os.path.isdir(item_path) else item
        
        # Create relative link
        index_lines.append(f"- [{display_name}]({item_path})")
    
    if not index_lines:
        return "_Directory is empty._"
        
    return "\n".join(index_lines)

# ==========================================
# CORE LOGIC
# ==========================================

def process_file(file_path):
    """
    Reads a Markdown file, processes patterns, and updates in-place.
    """
    if not os.path.exists(file_path):
        print(f"[SKIPPED] Target file '{file_path}' not found.")
        return

    print(f"--- Processing: {file_path} ---")

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    
    # ---------------------------------------------------------
    # PATTERN DEFINITIONS
    # ---------------------------------------------------------
    
    # Pattern 1: Code Embedding -> [](filename.ext)
    embed_pattern = re.compile(r"^\s*\[\]\((.*?)\)\s*$")
    
    # Pattern 2: Folder Indexing -> <div id="folder-index" dir="./path"></div>
    # Captures the directory path specified in the 'dir' attribute.
    # Defaults to '.' if dir attribute is missing is handled in logic but regex expects it here for precision.
    # Flexible regex to capture 'dir="value"'
    index_pattern = re.compile(r"^\s*<div\s+id=\"folder-index\"\s+dir=(.*?)>\s*</div>\s*$")

    # ---------------------------------------------------------
    # LINE PROCESSING
    # ---------------------------------------------------------
    
    while i < len(lines):
        line = lines[i]
        
        embed_match = embed_pattern.search(line)
        index_match = index_pattern.search(line)

        if embed_match:
            # --- CODE EMBEDDING ---
            filename = embed_match.group(1).strip()
            print(f"  [EMBED] Searching for: {filename}")

            new_lines.append(line) # Keep marker

            code_content = find_and_read_file(filename)
            lang_tag = get_language_tag(filename)
            new_block = f"```{lang_tag}\n{code_content}\n```\n"
            new_lines.append(new_block)

            # Skip existing block
            next_idx = i + 1
            if next_idx < len(lines) and lines[next_idx].strip().startswith("```"):
                i += 2
                while i < len(lines):
                    if lines[i].strip().startswith("```"):
                        i += 1
                        break
                    i += 1
                continue
            else:
                i += 1

        elif index_match:
            # --- HANDLER: FOLDER INDEXING ---
            # Extract the target directory path from the HTML attribute
            target_dir = index_match.group(1).strip()
            print(f"  [INDEX] Indexing directory: {target_dir}")

            # 1. Preserve the original marker line in the output
            new_lines.append(line)

            # 2. Generate and append the new file list
            index_content = generate_folder_index(target_dir)
            new_block = f"\n{index_content}\n\n"
            new_lines.append(new_block)

            # 3. Intelligent Skip: Detect and bypass existing index content
            #    to prevent duplication (overwrite mode).
            
            next_idx = i + 1

            # Step A: Skip any immediate empty lines following the marker
            # This ensures we find the list even if there is spacing.
            while next_idx < len(lines) and lines[next_idx].strip() == "":
                next_idx += 1

            # Step B: Check if the next content is a Markdown list (starting with - or *)
            if next_idx < len(lines) and (lines[next_idx].strip().startswith("- ") or lines[next_idx].strip().startswith("* ")):
                print(f"      -> Replacing existing index block.")
                
                # Step C: Skip all lines belonging to the old list
                # This loop continues as long as it sees list items or empty lines.
                while next_idx < len(lines):
                    line_content = lines[next_idx].strip()
                    
                    # Continue skipping if line is a list item OR empty
                    if line_content.startswith("- ") or line_content.startswith("* ") or line_content == "":
                        next_idx += 1
                    else:
                        # Stop skipping when a non-list line (e.g., Header, Text, Code) is found
                        break
                
                # Update main loop index to jump over the old section entirely
                i = next_idx
                continue
            else:
                # No existing list found; simply move to the next line
                print(f"      -> Inserting new index block.")
                i += 1
        else:
            new_lines.append(line) # Preserve normal line
            i += 1                 # Move to next line

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"[SUCCESS] Updated {file_path}")
    except Exception as e:
        print(f"[ERROR] Failed to write {file_path}: {e}")

def main():
    print("Starting Multi-Pattern Sync...")
    for target in TARGET_FILES:
        process_file(target)
    print("Completed.")

if __name__ == "__main__":
    main()