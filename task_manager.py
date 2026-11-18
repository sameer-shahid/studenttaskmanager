"""
Student Task Manager - Core Module
Handles task creation, storage, retrieval, and manipulation.
"""

import json
import os
from datetime import datetime


class Task:
    """Represents a single student task with metadata."""

    def __init__(self, task_id, title, description="", completed=False,
                 created_at=None, completed_at=None):
        self.task_id = int(task_id)
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()
        self.completed_at = completed_at

    def to_dict(self):
        """Serialize task to dictionary for JSON storage."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }

    @classmethod
    def from_dict(cls, data):
        """Reconstruct a Task instance from a dictionary."""
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            created_at=data.get("created_at"),
            completed_at=data.get("completed_at")
        )


class TaskManager:
    """Manages a collection of tasks with persistent JSON storage."""

    def __init__(self, storage_file="tasks.json"):
        self.storage_file = storage_file
        self.tasks = []
        self._load_tasks()

    def _next_id(self):
        """Generate the next available task ID."""
        if not self.tasks:
            return 1
        return max(t.task_id for t in self.tasks) + 1

    def add_task(self, title, description=""):
        """Create and store a new task. Returns the created Task object.

        Raises:
            ValueError: If the title is empty or contains only whitespace.
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty or whitespace.")
        title = title.strip()
        new_task = Task(self._next_id(), title, description)
        self.tasks.append(new_task)
        self._save_tasks()
        return new_task

    def list_tasks(self):
        """Return all tasks."""
        return list(self.tasks)

    def find_task(self, task_id):
        """Look up a task by its numeric ID. Returns None if not found."""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def complete_task(self, task_id):
        """Mark a task as completed. Returns True on success, False if not found."""
        task = self.find_task(task_id)
        if task is None:
            return False
        task.completed = True
        task.completed_at = datetime.now().isoformat()
        self._save_tasks()
        return True

    def delete_task(self, task_id):
        """Remove a task by ID. Returns True on success, False if not found."""
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        if len(self.tasks) < before:
            self._save_tasks()
            return True
        return False

    def _save_tasks(self):
        """Persist all tasks to the JSON storage file."""
        with open(self.storage_file, "w", encoding="utf-8") as fh:
            json.dump([t.to_dict() for t in self.tasks], fh, indent=2)

    def _load_tasks(self):
        """Load tasks from the JSON storage file if it exists."""
        if not os.path.exists(self.storage_file):
            self.tasks = []
            return
        try:
            with open(self.storage_file, "r", encoding="utf-8") as fh:
                data = json.load(fh)
                self.tasks = [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, KeyError):
            self.tasks = []
