# Conventions

## Repos

- Lab repos live in the `unclebuckslab` GitHub organization. Names are lowercase with hyphens: `congress-cards`, `lab-site`.
- New projects start from [templates/project/](../templates/project/).
- Public unless the data or plans are private. Public-good projects are always public.

## Branches and commits

- Branch names: `<role>/<short-description>`, for example `researcher/fec-source-recon` or `chief-of-staff/m1-foundation`.
- One pull request per task, linked to its issue.
- Commit messages say what changed and why, in plain words. First line under 72 characters.
- Commits made by agents end with a `Co-Authored-By:` line naming the model.

## Labels

Every lab repo uses the same labels.

| Label | Means |
| --- | --- |
| `idea` | Captured, not yet planned |
| `task` | Planned work, ready to pick up |
| `needs-approval` | Waiting in the Founder Desk queue |
| `publish` | Merging this makes something public |
| `ops` | Opened by the ops check: a failure, a stale dataset, an expiring token |
| `blocked` | Waiting on something outside the task |

## Files

- Dates are ISO: `2026-11-03`.
- Decision files: `decisions/YYYY-MM-DD-short-name.md`.
- Handbook files are `UPPERCASE.md`; everything else is lowercase.

## Hours

- Every milestone and task carries an estimate in focus hours.
- When a task closes, record the actual focus hours on the issue (`Actual hours: 2.5`).
- The registry holds estimated and actual hours per milestone. The founder logs his own time; agents log the session time they were directed for.
