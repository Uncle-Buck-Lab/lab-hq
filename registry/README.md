# Registry

The one place the lab's project list, stages and hours live. The site, the projects board and the weekly briefing read these files; nothing else keeps its own copy.

Run `python registry/validate.py` after any edit. It fails on a missing field, an unknown value or a broken reference.

## projects.yaml

| Field | Meaning |
| --- | --- |
| `id` | Short, permanent, lowercase with hyphens |
| `name` | Public name |
| `working_name` | `true` until the name is final |
| `endorsement` | The line under the name on the site |
| `type` | `recurring-report`, `dashboard`, `reference-database`, `visual`, `brand`, `product` or `writing` |
| `stage` | `idea`, `explore`, `define`, `build`, `review`, `launch`, `operate`, `improve` or `archived` |
| `status` | Public label: `in-the-lab`, `live`, `paused`, `archived` or `parked` (parked projects never show publicly) |
| `show_on_site` | Whether the site lists it |
| `priority` | 1 is highest |
| `repo` | `owner/name`, or `null` |
| `public_url` | Where the live thing is, or `null` |
| `summary` | One sentence for the project card; follows the writing rules |
| `playbook` | Path to its playbook, or `null` |
| `agents` | Squad roles that work on it |
| `next_milestone` | A milestone `id`, or `null` |
| `notes` | Anything the next session needs to know |

## milestones.yaml

| Field | Meaning |
| --- | --- |
| `id` | Short code: `S` setup, `M` lab, `B` brand, `P` project, `L` launch, `K` kit |
| `name` | What it delivers |
| `after` | Milestone ids that must be done first |
| `est_hours` | Estimated focus hours |
| `actual_hours` | Logged focus hours; `null` until work starts |
| `status` | `not-started`, `in-progress` or `done` |
| `done_means` | The test for calling it done |
