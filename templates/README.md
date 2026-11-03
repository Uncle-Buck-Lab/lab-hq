# Templates

`project/` holds the starting files for a new lab project repo.

## Starting a project

1. Add the project to `registry/projects.yaml` (stage `define`) and run `python registry/validate.py`.
2. Create the repo in the `unclebuckslab` org, empty.
3. Copy everything in `project/` into it, including `.github/`.
4. Replace every `PROJECT NAME` and fill in `CLAUDE.md` first: purpose, type, playbook, point of view.
5. Follow the playbook for the project's type.

From milestone M3, the `new-project` skill does steps 1, 3 and 4.
