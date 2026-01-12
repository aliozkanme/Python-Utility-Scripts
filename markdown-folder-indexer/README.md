# Markdown Folder Indexer

---

## About the Project
This tool scans the folders in its current directory and automatically lists them within a specified area of a target Markdown document. It is specifically designed for GitHub repositories containing numerous projects or subfolders to maintain an up-to-date index in the main file (README).

It eliminates the hassle of manually adding links and ensures the main list remains current with a single click as project folders are added or removed.

## Key Features
* **Automatic Scanning:** Detects all subfolders in the working directory.
* **Smart Filtering:** Automatically ignores system files and hidden folders (e.g., those starting with a dot).
* **Alphabetical Sorting:** Sorts listed folders from A to Z for easy readability.
* **Safe Writing:** Only modifies the area defined by specific markers within the document; never touches the rest of the text, headers, or descriptions.
* **Navigation Links:** Formats folder names as clickable links, providing direct access to the relevant folder from the list.

## How It Works
When the tool reads the target document, it searches for pre-defined "start" and "end" markers within the text. It clears any existing content between these two markers and rewrites the current list of folders into this space. This ensures that manual content located above and below the list is preserved.

## Installation and Usage
Having a Python interpreter installed on the system is sufficient to use this tool.

1.  Place the tool in the main directory you wish to list.
2.  Add the HTML-based start and end tags to the target Markdown document indicating where the list should be generated.
3.  **Run the tool:**
    * **Option A (Automatic):** A batch (`.bat`) file is included for convenience. Simply double-click this file to execute the Python script automatically without using the command line.
    * **Option B (Manual):** Open a terminal/command prompt and run the Python script directly.
4.  Once the process is complete, the list in the target document will be updated.