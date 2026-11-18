# Merge Conflict Resolution Report

## Overview
This document records the deliberate merge conflict simulation and its resolution conducted in the Student Task Manager repository.

---

## 1. What Caused the Conflict
1. A status line `Project status: Planning` was committed to `main`.
2. Two separate branches were branched from that commit:
   - `conflict-branch-a`: changed line to `Project status: Active Development`
   - `conflict-branch-b`: changed the identical line to `Project status: Testing and QA Phase`
3. `conflict-branch-a` was merged into `main` first.
4. When `conflict-branch-b` was merged into `main`, Git detected conflicting concurrent modifications on the exact same line in `README.md`, resulting in:
   ```
   CONFLICT (content): Merge conflict in README.md
   Automatic merge failed; fix conflicts and then commit the result.
   ```

---

## 2. Inspection of Conflict Markers
Git inserted standard conflict markers:
```markdown
<<<<<<< HEAD
Project status: Active Development
=======
Project status: Testing and QA Phase
>>>>>>> conflict-branch-b
```
- `<<<<<<< HEAD`: Points to the current state on `main` (from `conflict-branch-a`).
- `=======`: Divides the two conflicting changes.
- `>>>>>>> conflict-branch-b`: Points to the incoming change from `conflict-branch-b`.

---

## 3. Resolution Without Losing Unrelated Work
Instead of discarding either branch's contribution, both statuses were synthesized into a unified, accurate line:
```markdown
Project status: Active Development & Testing Phase (Core Features Implemented, QA Underway)
```

The file was staged using `git add README.md` and committed using:
```bash
git commit -m "merge: resolve merge conflict in README.md by combining status updates"
```
The merge was completed cleanly and pushed to the remote repository.
