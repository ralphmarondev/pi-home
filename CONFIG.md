# Configuring PyCharm to Run `main.py`

This guide explains how to configure PyCharm to always run `main.py` regardless of the currently active file.

---

## Steps to Configure:

1. **Open PyCharm** and load your project.
2. Navigate to the top-right corner of the PyCharm window and locate the **Run/Debug Configurations** dropdown.
3. Click the dropdown and select **"Edit Configurations..."**.
4. In the configurations window:
    - Click the **"+" (Add)** button in the top-left corner.
    - Choose **"Python"** from the list of available configurations.
5. Fill in the following details:
    - **Name**: `Run main.py`
    - **Script Path**: Browse and select your `main.py` file.
    - **Working Directory**: Ensure this points to your project folder.
6. Click **OK** to save the configuration.
7. Ensure the newly created configuration (`Run main.py`) is selected in the dropdown menu.
8. Press **Shift + F10** (or click the green Run button) to run the configuration. PyCharm will now always run
   `main.py`, regardless of the active file.

---

## Testing the Configuration

- Open any file in your project (e.g., `home.py`).
- Press **Shift + F10** or the **Run** button. PyCharm should run `main.py` as expected.

---

By following these steps, you can ensure PyCharm consistently executes `main.py`, simplifying your workflow and avoiding
errors from running unintended files.
