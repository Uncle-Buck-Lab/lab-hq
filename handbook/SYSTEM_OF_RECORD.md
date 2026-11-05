# System of record

One home for each kind of information. A copy kept anywhere else drifts out of date, so copies aren't kept.

| What | Lives in | Never in |
| --- | --- | --- |
| Company rules, voice, standards | lab-hq `handbook/` | Copies in project repos or files uploaded to Claude Projects |
| Project instructions and decisions | The project repo: `CLAUDE.md`, `handbook/`, decision log | Chat history |
| Project list, stages, hours | lab-hq `registry/` | Docs or spreadsheets |
| Tasks and approvals | GitHub issues and pull requests | Notes apps |
| Lab-level decisions | lab-hq `decisions/` | Chat history |
| Briefings, spend, token expiry dates, inbound, private plans | `lab-desk` (private) | Public repos |
| Strategy: growth playbook, pricing, revenue targets, partner pipeline | `lab-desk/strategy/` (private) | Public repos |
| Secrets and logins | GitHub Actions secrets and the lab password vault | Files, chat, browser password stores |
| Published work | The project's repo and the lab site | Anywhere it can't be traced to its sources |

## Rules

- **Read by link, don't upload.** Claude Projects and other tools read handbook files through the raw links in [INDEX.md](../INDEX.md). An uploaded copy goes stale the day the file changes.
- **Point, don't copy.** When a project needs a company rule, its `CLAUDE.md` points to the lab-hq file.
- **Plans become decisions.** A planning doc is a working draft. Once its decisions are made, they move into `decisions/` and the doc stops being edited.
