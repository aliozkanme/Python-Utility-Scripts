> 🇹🇷 **[Türkçe Versiyon İçin Tıklayınız / Click for Turkish Version](README_TR.md)**


# Generate Folder Tree


## About the Tool

This utility is a lightweight Python automation script designed to map out folder structures. It scans the directory where it is located and generates a clear, visual text representation of all files and subfolders, similar to a recursive directory tree command. It is ideal for documenting project structures, archiving file hierarchies, or analyzing complex directory contents.

## Key Features

* **Visual Hierarchy:** Generates an organized tree structure using standard ASCII characters to represent branches and nested levels.
* **Smart Filtering:** Includes a user-interactive prompt to explicitly include or exclude hidden system files and dotfiles based on system attributes.
* **Recursive Scanning:** Capable of traversing unlimited depth of subdirectories to capture the complete file architecture.
* **Universal Compatibility:** Uses UTF-8 encoding to ensure all file names and special characters are rendered correctly.
* **Automatic Naming:** Automatically names the output text file based on the root directory's name for easy identification.

## How It Works

Upon execution, the script identifies its current working directory as the root. It prompts the user via the terminal to decide whether hidden files should be included in the scan. Based on this input, it traverses every file and folder, sorts them alphabetically, and constructs a formatted string. Finally, it saves this visual map into a text file within the same directory.

## Installation and Usage

1.  **Directory Setup:**
    Ensure that Python is installed on your system. No external libraries are required as the tool uses standard modules.

2.  **Add Tags:**
    Copy both the Python script and the Batch file into the specific folder or directory you wish to map.

3.  **Run the Tool:**
    * **Option A (Automatic):** Double-click the provided Batch file to launch the script in a terminal window automatically.
    * **Option B (Manual):** Open a command line interface in the target folder and execute the Python script manually.

## Supported Formats

The tool supports all file types and folder structures recognized by the operating system. It accurately indexes standard documents, system directories, development environments, and hidden configuration files without restriction.