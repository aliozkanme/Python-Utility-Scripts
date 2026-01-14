# Markdown Code Embedder (GitHub Actions Edition)

---

## About the Tool
This tool automatically syncs your actual source code files with your Markdown documentation using GitHub Actions. Instead of manually updating code blocks in your `README.md` or running local scripts, this workflow listens for changes in your repository and automatically embeds the latest code from your source directory into your documentation.

It is designed for developers who want a "set it and forget it" solution. Once configured, any code you push to the repository is instantly reflected in the documentation, ensuring your `README.md` is always up-to-date with your actual codebase.

## Key Features
* **Fully Automated Workflow:** Powered by GitHub Actions, the update process triggers automatically on every push to the main branch. No manual script execution is required.
* **Dynamic "In-Place" Updates:** The script edits the Markdown file directly. It detects changes in the source code and intelligently replaces old code blocks with fresh content without duplicating text.
* **Invisible Markers:** Uses standard Markdown link syntax with empty text (e.g., `[](filename.ext)`) as invisible anchors. These markers stay in the document to guide future updates but remain invisible in the rendered view.
* **Automatic Syntax Highlighting:** Detects file extensions and applies the correct language tags (e.g., `python`, `matlab`, `cpp`) for proper coloring.
* **Extensible Design:** Supports a wide range of file formats, which can be easily expanded by modifying the extension map in the Python script.

## How It Works
The system utilizes a Python script located at `.github/scripts/markdown-code-embedder.py`, which is triggered by the `.github/workflows/update-code.yml` workflow.

1.  **Trigger:** When you push changes to the repository, GitHub Actions initiates the workflow.
2.  **Scan:** The script scans `README.md` for trigger tags like `[](Generator_G3_Time_Domain_Simulation.m)`.
3.  **Fetch & Embed:** It reads the corresponding file from the `src` directory, determines the language, and inserts/updates the code block immediately after the tag.
4.  **Commit:** If changes are detected in the documentation, the GitHub Actions bot automatically commits and pushes the updated `README.md` back to the repository.

## Usage
Once the setup is complete, you simply write your documentation:

1.  **Add Tags:** Insert reference tags in your `README.md` where you want the code to appear:
    `[](YourFile.py)`
2.  **Push:** Commit and push your changes to GitHub.
3.  **Result:** The Action will run, and within moments, your `README.md` will display the code block from `src/YourFile.py` right below the tag.

## Supported Formats
The tool currently supports syntax highlighting for the following extensions (editable in `markdown-code-embedder.py`):
* `.py` (Python)
* `.m` (Matlab)
* `.js` (JavaScript)
* `.c` / `.cpp` (C / C++)
* `.java` (Java)
* `.html` / `.css` (Web)
* `.sh` (Bash)
* `.json` / `.xml` (Data)
* `.md` (Markdown)