"""
Student Task Manager - Interactive Console Interface
Provides a menu-driven CLI for managing student tasks.
"""

import sys
from task_manager import TaskManager


def show_menu():
    """Display the main application menu."""
    print("\n" + "=" * 42)
    print("       STUDENT TASK MANAGER")
    print("=" * 42)
    print("  1.  Add a new task")
    print("  2.  Display all tasks")
    print("  3.  Mark a task as completed")
    print("  4.  Delete a task")
    print("  5.  Exit")
    print("=" * 42)


def run():
    """Main application loop."""
    mgr = TaskManager()

    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            title = input("Task title: ").strip()
            desc = input("Description (press Enter to skip): ").strip()
            try:
                task = mgr.add_task(title, desc)
                print(f"  -> Task #{task.task_id} created: {task.title}")
            except ValueError as err:
                print(f"  ** Validation error: {err}")

        elif choice == "2":
            all_tasks = mgr.list_tasks()
            if not all_tasks:
                print("  No tasks recorded yet.")
            else:
                print(f"\n  {'ID':<5} {'Status':<14} {'Title'}")
                print("  " + "-" * 44)
                for t in all_tasks:
                    if t.completed:
                        badge = "[Completed]"
                    else:
                        badge = "[Pending]"
                    print(f"  {t.task_id:<5} {badge:<14} {t.title}")
                    if t.description:
                        print(f"        -> {t.description}")

        elif choice == "3":
            try:
                tid = int(input("Task ID to complete: ").strip())
                if mgr.complete_task(tid):
                    print(f"  -> Task #{tid} marked complete.")
                else:
                    print(f"  ** Task #{tid} not found.")
            except ValueError:
                print("  ** Please enter a numeric ID.")

        elif choice == "4":
            try:
                tid = int(input("Task ID to delete: ").strip())
                confirm = input(f"  Confirm deletion of task #{tid}? (y/n): ").strip().lower()
                if confirm != "y":
                    print("  Deletion cancelled.")
                elif mgr.delete_task(tid):
                    print(f"  -> Task #{tid} deleted.")
                else:
                    print(f"  ** Task #{tid} not found.")
            except ValueError:
                print("  ** Please enter a numeric ID.")

        elif choice == "5":
            print("Goodbye!")
            sys.exit(0)

        else:
            print("  ** Invalid option. Choose 1-5.")


if __name__ == "__main__":
    run()
