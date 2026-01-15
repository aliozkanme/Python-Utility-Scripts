# Markdown Multi-Pattern Sync (Github Edition)

---

## About the Tool
This tool serves as a comprehensive automation solution for maintaining "living documentation" within your GitHub repository. By combining multiple synchronization strategies into a single workflow, it ensures that your technical documentation reflects the exact state of your project's codebase and directory structure at all times.

Designed for a "set it and forget it" experience, this utility runs entirely within GitHub Actions. It eliminates the need for manual updates by automatically scanning your Markdown files for specific triggers—whether they are requests to embed source code or to list file contents—and dynamically injecting the latest data whenever changes are pushed to the main branch.

## Key Features
* **Unified Automation Workflow:** The entire synchronization process is orchestrated by GitHub Actions. A single push to the repository triggers the script, which processes multiple distinct update patterns simultaneously without manual intervention.
* **Dual-Mode Synchronization:** Unlike simple embedders, this tool handles two critical documentation tasks: inserting source code content from various project paths and generating dynamic, clickable lists of files from specified directories.
* **Intelligent In-Place Editing:** The script modifies Markdown documents directly. It utilizes smart logic to identify previously generated content, remove it, and replace it with fresh data, ensuring no duplication occurs and the document structure remains clean.
* **Multi-Path Search Capability:** The tool is configured to search through a prioritized list of directories. This allows it to locate source files regardless of whether they reside in a source folder, the root directory, or a library subfolder.
* **Invisible Configuration:** The system uses standard Markdown and HTML syntax as "invisible hooks." These markers remain in the raw document to guide future updates but do not clutter the visual presentation of the rendered documentation.
* **Broad Language Support:** It automatically detects file extensions and applies appropriate syntax highlighting for a wide variety of programming languages and data formats.

## How It Works
The system is powered by a central Python script located in your repository's workflow directory. The process follows a linear execution path triggered by repository activity:

1.  **Trigger:** When a commit is pushed to the main branch, the GitHub Actions workflow initiates the synchronization job.
2.  **Pattern Scanning:** The script reads the target Markdown files line by line, looking for two distinct types of triggers: empty link references for code files and specific division tags for folder paths.
3.  **Execution & Content Retrieval:**
    * **For Code:** It searches the configured paths for the requested filename, reads its content, and embeds it with the correct language formatting.
    * **For Indexes:** It accesses the file system at the specified directory path, sorts the contents, and generates a bulleted list of links.
4.  **Smart Replacement:** Before inserting new content, the script checks the lines immediately following the trigger. If it detects existing code blocks or lists, it skips over them to prevent redundancy.
5.  **Commit:** If any changes were made to the documentation during this process, the workflow automatically commits and pushes the updated files back to the repository.

## Usage
Once the workflow is configured, maintaining your documentation becomes purely text-based:

1.  **Define Targets:** Ensure your script configuration lists the specific Markdown files you wish to keep synchronized and the directories where your source code resides.
2.  **Add Code Markers:** To embed a file, simply insert a reference link containing the filename into your Markdown text. The script will find this file and paste its contents below the link.
3.  **Add Index Markers:** To list the contents of a folder, insert the specific HTML division tag with a directory attribute pointing to the desired folder. The script will generate the file list below this tag.
4.  **Push Changes:** Commit your Markdown file with these text markers. The GitHub Action will execute, processing the markers and populating your document with the actual content and file structures.

## Supported Formats
The tool currently supports syntax highlighting for the following extensions.

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
  