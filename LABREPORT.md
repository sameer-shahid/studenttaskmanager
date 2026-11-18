# DevOps Lab Report: Student Task Manager Development & Version Control

- **Course:** DevOps for Cloud Computing (CSC418)
- **Student Name:** Sameer Shahid
- **Repository URL:** [https://github.com/sameer-shahid/studenttaskmanager](https://github.com/sameer-shahid/studenttaskmanager)
- **Release URL:** [https://github.com/sameer-shahid/studenttaskmanager/releases/tag/v1.0.0](https://github.com/sameer-shahid/studenttaskmanager/releases/tag/v1.0.0)

---

## Part 1: Conceptual Answers

### 1. Difference Between Git and GitHub; Purpose of Add, Commit, and Push
- **Git vs. GitHub**:
  - **Git** is an open-source, local, distributed version control system (DVCS) command-line utility. It runs on the developer's machine, records historical snapshots (commits) of files, and enables offline branching, merging, and tracking of changes.
  - **GitHub** is a cloud-hosted platform and collaboration service that hosts remote Git repositories. It layers team collaboration tooling on top of Git, such as Pull Requests, code reviews, Issues, GitHub Actions CI/CD workflows, project boards, and release management.
- **Purpose of `add`, `commit`, and `push`**:
  - **`git add`**: Moves modified or newly created files from the working directory into the staging area (index), preparing a curated set of changes ready to be snapshotted.
  - **`git commit`**: Takes the staged changes and records an immutable, cryptographic snapshot (commit) in the local Git repository history, associated with an author, timestamp, commit hash, and descriptive message.
  - **`git push`**: Transfers local commits from a branch on your machine to a remote repository (such as GitHub), synchronizing the remote-tracking branch and making your commits visible to collaborators.

---

### 2. Why Branches and Pull Requests are Used; What Causes Merge Conflicts
- **Why Branches are Used**:
  - Branches isolate active development, experimental ideas, bug fixes, or distinct features from the stable `main` branch.
  - Multiple developers can work concurrently on separate features without interfering with each other's code or destabilizing the production codebase.
- **Why Pull Requests (PRs) are Used**:
  - Pull Requests provide a structured mechanism for code review, collaboration, and automated quality assurance before code merges into the target branch.
  - Reviewers can comment on specific lines of diffs, suggest improvements, verify compliance with project standards, and automated CI tests can run automatically against the PR branch.
- **What Causes Merge Conflicts**:
  - A merge conflict occurs when two branches make different modifications to the exact same line(s) of a file since their common ancestor commit, or when one branch modifies a file that another branch deleted or renamed.
  - Because Git cannot safely make an arbitrary guess about which modification is correct, it halts the merge and inserts conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), delegating resolution to the human developer.

---

### 3. Difference Between Fetch vs. Pull, and Merge vs. Rebase
- **`git fetch` vs. `git pull`**:
  - **`git fetch`**: Contacts the remote repository and downloads new branches, tags, and commits into local remote-tracking branches (e.g., `origin/main`) without altering any files in your current working directory or active branch.
  - **`git pull`**: Performs a `git fetch` followed immediately by an automatic `git merge` (or rebase if configured), integrating remote changes directly into your checked-out local branch.
- **`git merge` vs. `git rebase`**:
  - **`git merge`**: Combines two branches by generating a dedicated "merge commit" that has two parent commits. This preserves the complete historical topology and branch lifecycles, showing exactly when and how the branch was integrated.
  - **`git rebase`**: Takes commits from the current branch and reapplies them sequentially on top of the tip of the target branch. This rewrites the commit hashes to form a straight, linear commit history, eliminating merge commits at the cost of rewriting history.

---

### 4. How GitHub Issues and Actions Help a Development Team
- **GitHub Issues**:
  - Acts as an integrated project management and bug-tracking database.
  - Allows teams to record bug reports, feature requests, and technical debt with descriptive labels (e.g., `enhancement`, `bug`, `documentation`), assignees, and milestones.
  - Can be linked to Pull Requests using closing keywords (e.g., `Closes #1`), which automatically marks issues as resolved when the PR is merged into `main`.
- **GitHub Actions**:
  - Provides built-in Continuous Integration and Continuous Deployment (CI/CD) automation directly within GitHub.
  - Workflows run on specified event triggers (e.g., `push` to main, `pull_request` creation).
  - Teams use Actions to automatically execute unit test suites across multiple operating systems and Python versions (matrix builds), run linters, build artifacts, and deploy services.
  - It catches syntax errors, failing tests, and regressions early in the lifecycle before broken code enters production.

---

### 5. Difficulty Faced and How It Was Solved
- **The Challenge**:
  - During Part D, a deliberate merge conflict was generated in `README.md` on the `Project status:` line between `conflict-branch-a` (status: `Active Development`) and `conflict-branch-b` (status: `Testing and QA Phase`).
  - Merging `conflict-branch-b` into `main` after `conflict-branch-a` had already been merged resulted in:
    ```
    CONFLICT (content): Merge conflict in README.md
    Automatic merge failed; fix conflicts and then commit the result.
    ```
- **The Resolution**:
  - Inspected `README.md` to locate Git's conflict markers (`<<<<<<< HEAD`, `=======`, `>>>>>>> conflict-branch-b`).
  - Instead of discarding one branch's changes in favor of the other, both updates were evaluated for context.
  - A synthesized status was authored: `Project status: Active Development & Testing Phase (Core Features Implemented, QA Underway)`.
  - The conflict markers were cleanly removed, the resolved file was staged using `git add README.md`, and the merge was completed with `git commit -m "merge: resolve merge conflict in README.md by combining status updates"`.
  - The resolution preserved all context without losing any unrelated work.

---

## Part 2: Repository Artifacts & Evidence Summary

| Item | Requirement | Implemented Count / Status | Notes / Links |
| :--- | :--- | :--- | :--- |
| **Public Repository** | Named `studenttaskmanager` | ✅ Verified Public | [Repo Link](https://github.com/sameer-shahid/studenttaskmanager) |
| **Meaningful Commits** | At least 12 commits | ✅ 16+ commits | Structured Conventional Commit format |
| **Feature Branches** | 3 feature branches | ✅ 3 branches | `feature/addtask`, `feature/completetask`, `feature/deletetask` |
| **GitHub Issues** | At least 4 Issues | ✅ 4 Issues | Issues #1, #2, #3, #4 with clear labels and descriptions |
| **Merged Pull Requests** | 5 merged Pull Requests | ✅ 5 Merged PRs | PRs #5, #6, #7, #8, #9 reviewed and merged |
| **Resolved Conflicts** | 1 deliberate conflict | ✅ 1 Resolved | `README.md` status line conflict documented |
| **Automated Tests** | At least 3 unit tests | ✅ 5 automated tests | `test_task_manager.py` (add, validation, complete, delete, lookup) |
| **GitHub Actions CI** | 1 CI workflow | ✅ 1 matrix workflow | Python 3.10, 3.11, 3.12 matrix on push & PR |
| **Failed & Pass Runs** | 1 failed, 1 pass run | ✅ Demonstrated | Failed run: #44260990393, Passed run: #44261354969 |
| **GitHub Release** | Tagged `v1.0.0` | ✅ Published v1.0.0 | Release notes, tag, and assets |
| **Screenshots Folder** | `labevidence/` folder | ✅ Fully populated | Terminal outputs, logs, and evidence screenshots |

---

## Part 3: Step-by-Step Evidence Reference

- `labevidence/conflict_before_resolution.txt`: Raw Git conflict markers before resolution.
- `labevidence/conflict_after_resolution.txt`: Staged resolution after synthesizing both statuses.
- `labevidence/ci_failure_log.txt`: GitHub Actions failed run output showing deliberate failure assertion.
- `labevidence/ci_success_log.txt`: GitHub Actions passing run output across all matrix versions.
- `labevidence/01_terminal_unittest.png`: Unit test execution showing 5 passing tests.
- `labevidence/02_git_graph.png`: Commit graph and branch history.
- `labevidence/03_github_repo.png`: Web capture of public GitHub repository homepage.
- `labevidence/04_github_issues.png`: Web capture of all 4 completed GitHub Issues.
- `labevidence/05_github_prs.png`: Web capture of all 5 merged Pull Requests.
- `labevidence/06_github_actions.png`: Web capture of GitHub Actions workflow history (failed and passed runs).
- `labevidence/07_github_release.png`: Web capture of published GitHub Release v1.0.0.
