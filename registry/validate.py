"""Validate registry/projects.yaml and registry/milestones.yaml.

Run from the repo root: python registry/validate.py
Exits 1 and lists every problem if anything is wrong.
"""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

PROJECT_FIELDS = {
    "id", "name", "working_name", "endorsement", "type", "stage", "status",
    "show_on_site", "priority", "repo", "public_url", "summary", "playbook",
    "agents", "next_milestone", "notes",
}
TYPES = {"recurring-report", "dashboard", "reference-database", "visual", "brand", "product", "writing"}
STAGES = {"idea", "explore", "define", "build", "review", "launch", "operate", "improve", "archived"}
STATUSES = {"in-the-lab", "live", "paused", "archived", "parked"}

MILESTONE_FIELDS = {"id", "name", "after", "est_hours", "actual_hours", "status", "done_means"}
MILESTONE_STATUSES = {"not-started", "in-progress", "done"}


def load(name):
    with open(ROOT / "registry" / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_milestones(problems):
    milestones = load("milestones.yaml")["milestones"]
    ids = [m.get("id") for m in milestones]
    if len(ids) != len(set(ids)):
        problems.append("milestones: duplicate ids")
    for m in milestones:
        where = f"milestone {m.get('id')}"
        missing = MILESTONE_FIELDS - m.keys()
        extra = m.keys() - MILESTONE_FIELDS
        if missing:
            problems.append(f"{where}: missing {sorted(missing)}")
        if extra:
            problems.append(f"{where}: unknown fields {sorted(extra)}")
        if m.get("status") not in MILESTONE_STATUSES:
            problems.append(f"{where}: status '{m.get('status')}' not in {sorted(MILESTONE_STATUSES)}")
        for dep in m.get("after") or []:
            if dep not in ids:
                problems.append(f"{where}: depends on unknown milestone '{dep}'")
        est = m.get("est_hours")
        if not isinstance(est, (int, float)) or est <= 0:
            problems.append(f"{where}: est_hours must be a positive number")
        actual = m.get("actual_hours")
        if actual is not None and (not isinstance(actual, (int, float)) or actual < 0):
            problems.append(f"{where}: actual_hours must be null or a number >= 0")
        if m.get("status") == "done" and m.get("est_hours") is None:
            problems.append(f"{where}: done milestones need an estimate")
    return set(ids)


def check_projects(problems, milestone_ids):
    projects = load("projects.yaml")["projects"]
    ids = [p.get("id") for p in projects]
    if len(ids) != len(set(ids)):
        problems.append("projects: duplicate ids")
    for p in projects:
        where = f"project {p.get('id')}"
        missing = PROJECT_FIELDS - p.keys()
        extra = p.keys() - PROJECT_FIELDS
        if missing:
            problems.append(f"{where}: missing {sorted(missing)}")
        if extra:
            problems.append(f"{where}: unknown fields {sorted(extra)}")
        if p.get("type") not in TYPES:
            problems.append(f"{where}: type '{p.get('type')}' not in {sorted(TYPES)}")
        if p.get("stage") not in STAGES:
            problems.append(f"{where}: stage '{p.get('stage')}' not in {sorted(STAGES)}")
        if p.get("status") not in STATUSES:
            problems.append(f"{where}: status '{p.get('status')}' not in {sorted(STATUSES)}")
        if p.get("status") == "parked" and p.get("show_on_site"):
            problems.append(f"{where}: parked projects can't show on the site")
        if p.get("next_milestone") is not None and p["next_milestone"] not in milestone_ids:
            problems.append(f"{where}: next_milestone '{p['next_milestone']}' isn't in milestones.yaml")
        playbook = p.get("playbook")
        if playbook is not None and not (ROOT / playbook).exists():
            problems.append(f"{where}: playbook '{playbook}' doesn't exist")


def main():
    problems = []
    milestone_ids = check_milestones(problems)
    check_projects(problems, milestone_ids)
    if problems:
        print("Registry problems:")
        for line in problems:
            print(f"  - {line}")
        sys.exit(1)
    print("Registry OK")


if __name__ == "__main__":
    main()
