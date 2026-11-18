# Student Task Manager

[![Python Unit Tests CI](https://github.com/sameer-shahid/studenttaskmanager/actions/workflows/python-tests.yml/badge.svg)](https://github.com/sameer-shahid/studenttaskmanager/actions/workflows/python-tests.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/sameer-shahid/studenttaskmanager)](https://github.com/sameer-shahid/studenttaskmanager/releases)

A Python console application for managing student tasks, built with standard Git workflows and GitHub DevOps practices.

---

## Project Status
Project status: Active Development & Testing Phase (Core Features Implemented, QA Underway)

---

## Features
- **Task Creation & Validation**: Rejects empty or whitespace-only task titles and raises informative validation feedback.
- **Task Status Management**: Toggle task completion with automated timestamp tracking.
- **Safe Task Deletion**: ID verification and interactive `y/n` confirmation to prevent accidental data loss.
- **Persistent Storage**: Lightweight JSON storage file preserving task state across runs.
- **Automated Testing**: Comprehensive Python `unittest` suite covering all core operations.
- **Continuous Integration (CI)**: GitHub Actions workflow testing matrix across Python 3.10, 3.11, and 3.12 on Ubuntu runners.

---

## Setup & Quickstart

### Prerequisites
- Python 3.10 or higher
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/sameer-shahid/studenttaskmanager.git
cd studenttaskmanager

# Launch application
python3 main.py
```

---

## Running Tests
Run the automated test suite locally:
```bash
python3 -m unittest discover -s tests -v
```

---

## Git Workflow & Branching Strategy
This repository adheres to a feature-branch workflow:
- `main`: Production-ready, stable codebase protected with automated CI checks.
- `feature/addtask`: Input validation and rejection of empty task titles (Merged via PR #5).
- `feature/completetask`: Task completion logic and status indicators (Merged via PR #6).
- `feature/deletetask`: Safe task deletion by identifier with confirmation (Merged via PR #7).
- `feature/conflict-documentation`: Merge conflict simulation and resolution report (Merged via PR #8).
- `feature/ci-workflow-and-tests`: GitHub Actions CI pipeline and unit test suite (Merged via PR #9).

---

## Documentation Links
- [User Guide](docs/userguide.md) - Detailed usage guide and CLI walkthrough.
- [Merge Conflict Resolution](docs/conflict_resolution.md) - Detailed analysis of conflict markers and resolution.
- [Lab Report](LABREPORT.md) - Comprehensive DevOps report with concept answers and workflow evidence.
- [License](LICENSE) - MIT License.
