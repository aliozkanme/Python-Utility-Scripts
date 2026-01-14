# Markdown Code Embedder

---

## About the Tool
This tool automatically syncs your actual source code files with your Markdown documentation. Instead of manually copy-pasting code into your `README.md` or reports, this script reads the code directly from your source directory and embeds it into the document.

It is specifically designed for developers who want to maintain their code in runnable files (e.g., inside a `src` folder) while ensuring their documentation always displays the most recent version of that code. If you modify your source code, simply running this tool updates the Markdown file instantly.

## Key Features
* **Dynamic "In-Place" Updates:** The tool edits the Markdown file directly. It finds the specific tags, inserts the code, and if the code has changed, it intelligently replaces the old code block with the new one without duplicating content.
* **Invisible Markers:** It uses standard Markdown link syntax with empty text (e.g., `[](filename.ext)`), which acts as an invisible anchor. These markers remain in the document but are not visible in the final rendered view.
* **Automatic Syntax Highlighting:** The tool detects the file extension and applies the correct language tag to the Markdown code block (e.g., `python`, `matlab`, `cpp`) for proper coloring.
* **Batch Execution:** Includes a simple `.bat` file to run the update process with a single double-click.
* **Extensible Design:** Supported file formats are defined in a dictionary within the script, allowing users to easily add new extensions if needed.

## How It Works
The Python script scans the target Markdown document line by line, looking for specific trigger tags formatted as empty links, such as `[](Generator_G3_Time_Domain_Simulation.m)`.

When it finds a tag:
1.  It reads the corresponding filename from the `src` directory.
2.  It determines the correct programming language based on the file extension.
3.  It checks the lines immediately following the tag.
4.  If a code block already exists there, it is removed and replaced with the fresh content. If no code block exists, a new one is inserted immediately.

This ensures that the tag remains permanently in the file to guide future updates, while the visible code block is always kept in sync with the source file.

## Installation and Usage
Having a Python interpreter installed on the system is sufficient to use this tool.

1.  **Directory Setup:** Place `markdown-code-embedder.py` and `embed.bat` in the root directory. Place your source code files inside a folder named `src`.
2.  **Add Tags:** In your Markdown file, insert the reference tag where you want the code to appear. Use the format `[](YourFile.ext)`.
3.  **Run the Tool:**
    * **Option A (Automatic):** Double-click the `embed.bat` file. This will execute the Python script and close automatically.
    * **Option B (Manual):** Open a terminal and run `python markdown-code-embedder.py`.
4.  **Supported Formats:**
    The tool currently supports syntax highlighting for the following extensions. You can easily add more by editing the extension map in the script:
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