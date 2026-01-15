# Markdown Multi-Pattern Sync

---

## About the Tool
This tool is a versatile automation script designed to keep your technical documentation seamlessly synchronized with your project's codebase and file structure. Instead of manually updating code snippets or directory lists in your documentation, this utility scans your Markdown files for specific patterns and dynamically injects the most current content.

It is built for developers who manage complex documentation requiring references to live code files and directory organizations. By separating your source content from your documentation, you ensure that your `README` or technical reports never contain outdated code or broken file lists.

## Key Features
* **Multi-Pattern Recognition:** Beyond just embedding code, this tool supports multiple synchronization patterns. It can inject file contents and generate dynamic directory indexes simultaneously.
* **Smart In-Place Updates:** The script modifies your Markdown files directly. It intelligently identifies existing generated content and replaces it with the fresh version without creating duplicates or disrupting the document structure.
* **Multi-Path Search Strategy:** You can configure multiple search directories. The tool will sequentially look for target files across these folders, allowing for flexible project organizations where source code might reside in different locations.
* **Dynamic Directory Indexing:** Uses HTML-style markers to automatically generate and maintain a bulleted list of files and folders from a specified directory, keeping your navigation links up to date.
* **Invisible Anchor Tags:** Utilizes standard Markdown link syntax and HTML attributes as invisible triggers. These markers stay in your document to guide future updates but do not clutter the final visual output.
* **Broad Format Support:** Comes with a predefined map of file extensions to ensure appropriate syntax highlighting is applied to every embedded code block.

## How It Works
The Python script processes the specified Markdown documents line by line, searching for distinct trigger patterns.

**For Code Embedding:**
The tool looks for empty link references containing a filename. When found, it searches through the configured paths to locate the file. Once located, the file's content is read and inserted immediately after the marker, wrapped in a code block with the correct language identifier.

**For Folder Indexing:**
The tool detects specific division tags that specify a target directory. Upon detection, it scans the actual file system at that location and generates a sorted, clickable list of all files and subdirectories, inserting this list directly into the documentation.

In both processes, the tool employs a "skip logic" to detect if content was previously generated. This ensures that old blocks are removed before new ones are inserted, maintaining a clean and accurate document.

## Installation and Usage
No complex installation is required; a standard Python environment is sufficient.

1.  **Configuration:** Open the script file to define the list of target Markdown files you wish to maintain and the search paths where your source code resides.
2.  **Placement:** Ensure the script and your target Markdown files are accessible within your project directory.
3.  **Adding Markers:**
    * To embed code, simply add a reference link with the filename in your Markdown text.
    * To index a folder, add the specific division tag pointing to the desired directory path.
4.  **Execution:**
    * **Automatic:** Run the provided batch file to execute the update process instantly.
    * **Manual:** Execute the Python script via your terminal. The tool will report the processing status of each file and confirm when updates are complete.
5.	**Supported Formats:**
    The tool currently supports syntax highlighting for the following extensions:
    * `.py` (Python)
    * `.m` (Matlab)
    * `.js` (JavaScript)
    * `.c` (C)
    * `.cpp` (C++)
    * `.java` (Java)
    * `.html` (HTML)
    * `.css` (CSS)
    * `.sh` (Bash)
    * `.json` (JSON)
    * `.xml` (XML)
    * `.md` (Markdown)
    * `.yml` / `.yaml` (YAML)