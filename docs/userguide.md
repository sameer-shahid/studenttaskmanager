# Student Task Manager - User Guide

## Introduction
Student Task Manager is a Python-based command-line utility created to help students track academic tasks, deadlines, and project deliverables with ease. It features persistent storage in JSON format and comprehensive input validation.

---

## Prerequisites
- **Python**: Version 3.10, 3.11, or 3.12
- **Git**: Version 2.20+

---

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sameer-shahid/studenttaskmanager.git
   cd studenttaskmanager
   ```

2. **Verify Python environment**:
   ```bash
   python3 --version
   ```

3. **Launch the console application**:
   ```bash
   python3 main.py
   ```

---

## Application Walkthrough

When you start the application, you are presented with the main menu:

```
==========================================
       STUDENT TASK MANAGER
==========================================
  1.  Add a new task
  2.  Display all tasks
  3.  Mark a task as completed
  4.  Delete a task
  5.  Exit
==========================================
```

### 1. Add a New Task
- Select option `1`.
- Enter a task title (e.g., `Prepare DevOps Lab 4 Report`).
- Enter an optional description (e.g., `Complete merge conflict and CI sections`).
- **Validation**: If an empty or whitespace-only title is entered, the application rejects it with an informative message (`** Validation error: Task title cannot be empty or whitespace.`).

### 2. Display All Tasks
- Select option `2`.
- The application displays a formatted table with:
  - **ID**: Unique numeric identifier
  - **Status**: `[Completed]` or `[Pending]`
  - **Title**: Task title
  - **Description**: Optional additional details

Example output:
```
  ID    Status         Title
  --------------------------------------------
  1     [Completed]    DevOps Assignment 4
        -> Submit report and evidence
  2     [Pending]      Cloud Computing Quiz
        -> Review Docker and Kubernetes
```

### 3. Mark a Task as Completed
- Select option `3`.
- Enter the numeric ID of the task you wish to complete.
- The system marks the task as completed and automatically records an ISO timestamp.
- If the ID does not exist, an error is reported: `** Task #ID not found.`

### 4. Delete a Task
- Select option `4`.
- Enter the numeric ID of the task to delete.
- The system asks for confirmation: `Confirm deletion of task #ID? (y/n): `
- If confirmed (`y`), the task is permanently removed from storage.

### 5. Exit
- Select option `5`.
- Saves state cleanly and exits the program.

---

## Running Automated Unit Tests
To run the automated test suite locally:
```bash
python3 -m unittest discover -s tests -v
```

Expected output:
```
test_add_task_success (test_task_manager.TestTaskManager.test_add_task_success) ... ok
test_add_task_validation_error (test_task_manager.TestTaskManager.test_add_task_validation_error) ... ok
test_complete_task_success (test_task_manager.TestTaskManager.test_complete_task_success) ... ok
test_delete_task_non_existent (test_task_manager.TestTaskManager.test_delete_task_non_existent) ... ok
test_delete_task_success (test_task_manager.TestTaskManager.test_delete_task_success) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```
