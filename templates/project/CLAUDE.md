# PROJECT NAME: instructions

This is a project of Uncle Buck's Laboratory. Lab-wide rules come first:

1. Read the lab index: https://raw.githubusercontent.com/Uncle-Buck-Lab/lab-hq/main/INDEX.md
2. Read the lab instructions: https://raw.githubusercontent.com/Uncle-Buck-Lab/lab-hq/main/CLAUDE.md
3. Then this file and this repo's `handbook/`.

Where this file and the lab rules conflict, the stricter rule wins.

## What this project is

- **Purpose:** one sentence.
- **Type:** recurring report | dashboard | reference database | visual | brand | product | writing
- **Playbook:** link to the lab playbook it follows.
- **Point of view:** none, or the declared stance (see the lab's TRUST_RULES.md, rule 10).

## Where things are

- Coverage and scope: `scripts/config.py`
- Pulling data: `scripts/fetch.py`
- Cleaning and derived fields: `scripts/build.py`
- What people see: `docs/`

## Project-specific rules

- Add rules only this project needs: data quirks to respect, privacy steps, review thresholds.

## When something breaks

Guards stop the run and keep the last good data live. Diagnose with `handbook/DATA.md` and `handbook/OPERATIONS.md`, then tell the founder what changed.
