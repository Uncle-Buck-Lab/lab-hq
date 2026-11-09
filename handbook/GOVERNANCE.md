# Governance

The founder directs; agents execute within clear permissions. This file says what agents may do alone, what needs sign-off and how to stop everything.

## What needs sign-off

| Action | Agents may | Needs approval | How |
| --- | --- | --- | --- |
| Research, collect public data, analyze | Yes | No | Work happens in the project repo |
| Draft writing, code, charts | Yes, on a branch | Merging to main | Pull request |
| Scheduled refresh in an approved pipeline | Yes | Changes to the pipeline itself | The data bot commits data; code changes go through a PR |
| Publish anything public (site page, report issue, post) | No | Always | PR labelled `publish` with the pre-publish checklist |
| New paid service, subscription, API key, any spending | No | Always | Issue labelled `needs-approval` |
| Delete data, repos or files; change permissions or secrets | No | Always | Founder only |
| External communication (email, DMs, outreach) | No | Always | Founder only |

## Approval tiers

Three tiers keep review from becoming the lab's speed limit.

| Tier | Covers | How it's approved |
| --- | --- | --- |
| **Pre-authorized** | Data refreshes in approved pipelines, typo and link fixes, dashboard data, registry updates | Ships without review; listed in the weekly briefing |
| **Batched** | Drafts, new pages, code changes, Field Notes posts | Reviewed in one weekly Founder Desk session, about an hour |
| **Explicit** | Every "Always" row above: publishing a project or report issue, money, deletions, permissions, outside communication | The founder approves each one on its own |

When an agent can't tell which tier applies, it treats the work as Explicit.

## The Founder Desk

- **The queue** is every open issue or PR labelled `needs-approval` across lab repos.
- **The session** happens once a week. Batched items are reviewed together; Explicit items can be approved any time.
- **Wait time** is recorded by the ops check. Anything waiting more than 7 days is flagged in the weekly briefing.
- **A merge is an approval.** The `publish` label on a merged PR makes it public.
- **A merge instruction in chat is an approval too.** When the founder tells an agent to merge a specific PR, the agent merges it and notes that in the PR. Permission changes are the exception: the founder merges those himself.

## Records

- **Audit log:** git history, Actions logs and the decision records.
- **Decisions:** lab-level ones go in `decisions/`, one dated file each. Project ones go in the project's decision log. A decision isn't reopened without a new reason.
- **Spending:** capped in the Anthropic Console and recorded monthly in `lab-desk/spend.md`, with a budget per project in the registry.

## Credentials

- Secrets live in GitHub Actions secrets and the lab password vault. Never in files, never in chat.
- Tokens are fine-grained, scoped to one repo where possible, and expire within 30 days.
- Every token's expiry date (never its value) is listed in `lab-desk/token-expiry.md`.

## Kill switch

- **Stop a pipeline:** disable its workflow in the repo's Actions tab.
- **Stop an agent:** revoke its token or remove the Claude app's access to the org.
- **Stop everything:** both of the above across the org. `lab-desk/RUNBOOK_AWAY.md` lists the exact steps, doable from a phone.

## Agents and permissions

Agents never expand their own permissions. Changes to permission files, workflow `permissions:` blocks or token scopes arrive as a PR the founder merges.
