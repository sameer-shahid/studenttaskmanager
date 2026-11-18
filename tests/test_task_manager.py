"""
Automated Unit Tests for Student Task Manager
Tests task creation, input validation, completion, and deletion.
"""

import os
import unittest
from task_manager import TaskManager, Task


class TestTaskManager(unittest.TestCase):
    """Test suite covering core TaskManager operations."""

    def setUp(self):
        """Prepare an isolated temporary JSON storage file for each test."""
        self.test_file = "test_tasks_data.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.manager = TaskManager(storage_file=self.test_file)

    def tearDown(self):
        """Clean up the temporary storage file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task_success(self):
        """Test adding a task with valid title and description."""
        task = self.manager.add_task("Prepare DevOps Presentation", "Cover Git and CI/CD")
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.title, "Prepare DevOps Presentation")
        self.assertEqual(task.description, "Cover Git and CI/CD")
        self.assertFalse(task.completed)
        self.assertIsNone(task.completed_at)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_validation_error(self):
        """Test that empty or whitespace-only titles raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.add_task("")
        with self.assertRaises(ValueError):
            self.manager.add_task("    ")

    def test_complete_task_success(self):
        """Test marking a task as completed."""
        task = self.manager.add_task("Lab Assignment 4", "Version control exercises")
        self.assertFalse(task.completed)
        
        result = self.manager.complete_task(task.task_id)
        self.assertTrue(result)
        
        updated = self.manager.find_task(task.task_id)
        self.assertTrue(updated.completed)
        self.assertIsNotNone(updated.completed_at)

    def test_delete_task_success(self):
        """Test deleting an existing task by identifier."""
        task1 = self.manager.add_task("Task One")
        task2 = self.manager.add_task("Task Two")
        self.assertEqual(len(self.manager.list_tasks()), 2)
        
        result = self.manager.delete_task(task1.task_id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.list_tasks()), 1)
        self.assertIsNone(self.manager.find_task(task1.task_id))
        self.assertIsNotNone(self.manager.find_task(task2.task_id))

    def test_delete_task_non_existent(self):
        """Test deleting a non-existent task returns False."""
        self.assertFalse(self.manager.delete_task(9999))

    def test_intentional_failure_for_ci_demonstration(self):
        """Deliberate failing assertion to demonstrate CI failure reporting."""
        self.assertEqual("devops_green_ci", "devops_red_ci_failure",
                         "Deliberate test failure for CI failure demonstration")


if __name__ == "__main__":
    unittest.main()
