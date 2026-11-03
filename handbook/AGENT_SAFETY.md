# Agent safety

Agents get real autonomy inside hard limits. These are the limits.

## 1. The read/act boundary

The biggest risk in an agent lab is an agent that reads untrusted text and can also act. A filing, a web page or an email can contain instructions written to hijack whatever reads it.

- **Readers have no tools.** Anything that reads untrusted text (filings, web pages, lobbying records, email, outside issue comments) runs with no tools and returns structured output.
- **Output is checked against a schema.** Fields, types and allowed values are validated before anything downstream sees them. Invalid output is rejected, not repaired.
- **Actors never see raw text.** Agents with write access work only from validated data.
- **Instructions found in data are reported, never followed.** An agent that finds text telling it to do something flags it in the run log and carries on with its task.

## 2. Least privilege

- Tokens are read-only by default.
- Write access is scoped to one repo and to branches. Only pre-authorized data bots write to `main`.
- Workflows declare the narrowest `permissions:` they need. The org default is read-only.
- No agent holds credentials for money, email sending or social posting.

## 3. Budgets

- Every scheduled agent run has a token budget and a cost cap set in its config; it stops when either is hit.
- The Anthropic Console holds a monthly spend limit for the lab.
- Model choices and limits live in one config file per project, so switching models is a config change plus an eval run.

## 4. Eval gates

- Every agent role has a gold set in `evals/`, built the way the AI Money Report's extractor evals are: real cases with known answers, including traps.
- Any change to a prompt, model or agent definition reruns its evals. A failed eval blocks the merge.
- Extraction runs at temperature 0 so the same input gives the same answer.

## 5. Scheduled agents

- Headless agents run in GitHub Actions on a schedule: the weekly briefing, ops triage, first drafts.
- Their output arrives as issues and pull requests. Nothing merges itself.

## 6. Logging

- Every agent run logs what it read, what it produced, its token use and its cost.
- The lab notebook on each project page is generated from these logs.
