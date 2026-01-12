# GitHub Action Auto Indexer

---

## About the Project
This project provides a complete automation solution for maintaining dynamic project lists in GitHub repositories. Instead of running scripts manually, this solution utilizes **GitHub Actions** to automatically detect, index, and update the list of folders in your `README.md` file whenever a new project is pushed to the repository.

It is designed to create a "set it and forget it" workflow, ensuring your repository documentation is always synchronized with your actual folder structure without any human intervention.

## Key Features
* **Fully Automated Workflow:** The indexing process is triggered automatically by every `push` command to the main branch.
* **Continuous Integration (CI):** Runs entirely on GitHub's cloud infrastructure; no local Python installation is required for other contributors.
* **Smart Detection & Filtering:** Scans the repository, ignores system files (like `.git` or `.github`), and sorts content alphabetically.
* **Auto-Commit Capability:** If the index changes, the workflow automatically commits and pushes the updated `README.md` back to the repository using a bot.
* **Safe Injection:** Updates only the specific section defined by HTML markers, preserving the rest of your documentation.

## How It Works
1.  **Trigger:** You push a new folder or changes to the repository.
2.  **Execution:** GitHub Actions spins up a virtual environment and runs the indexing script.
3.  **Update:** The script regenerates the list of links based on the current folder structure.
4.  **Verification:** The system checks if the `README.md` file has changed.
5.  **Push Back:** If changes are detected, a system bot commits the new version back to the repository (skipping further CI triggers to prevent loops).

## Installation and Setup Guide
To integrate this automation into your repository, follow these structural steps:

1.  **Script Placement:**
    Place the Python indexing script within the `.github/scripts/` directory of your repository. This keeps the root directory clean and organized.

2.  **Workflow Configuration:**
    Create a YAML workflow file inside the `.github/workflows/` directory. This file defines the trigger rules (e.g., on push to main) and the instructions to run the script.

3.  **Prepare the README:**
    Add the required HTML "start" and "end" markers to your main `README.md` file where you want the list to appear.

4.  **Activate:**
    Push these changes to GitHub. The action will trigger for the first time, and your list will be populated automatically.