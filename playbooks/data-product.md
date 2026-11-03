# Playbook: data product

For any project where a public data source flows through a scheduled pipeline, gets cleaned and shaped with judgment about what matters, and lands on a live page. The first one was [Denver Neighborhood Sales](https://unclebuck20.github.io/denver-dashboard/): Denver's property-sales API in, a dashboard and a map out, refreshed every Monday for $0.

Adapted from the Data Product Starter in the denver-dashboard repo.

## The five layers

| Layer | What it is | Default |
| --- | --- | --- |
| 1. Instructions | How agents operate the project | `CLAUDE.md` pointing to lab-hq's `INDEX.md`, plus the project `handbook/` |
| 2. Repo | Code, data snapshots, docs: the source of truth | A repo in the `unclebuckslab` org, public unless the data is private |
| 3. Data flow | Scheduled pull from an API or feed | GitHub Actions cron, `scripts/fetch.py` writing to `data/raw/` |
| 4. Processing | Cleaning, joining, derived fields, the "so what" | `scripts/build.py` writing one JSON file with a documented contract |
| 5. Page | What people look at | Static HTML/JS on GitHub Pages reading that JSON, listed on the lab site |

The pattern stays fixed; the source, the processing and the page change each time.

## How the build runs

The founder directs; agents build. Confirm scope before anything substantial.

**Step 0: Frame.** Pin down four things, proposing answers rather than interviewing:
- What question or decision does this serve, and for whom?
- What's the smallest version worth using every week?
- Which sources?
- What does the page need to answer at a glance?

**Step 1: Source recon, before any code.** For each source, find the endpoint, auth needs, rate limits and page size, row counts, how far back history goes, how often it updates, and the licence or terms. Report surprises (missing history, broken fields) before building on them.

**Step 2: First pull in Actions.** Stand up the repo and workflow, pull a real slice and profile it: what's clean, what's junk, nulls and outliers, what keys join the tables.

**Step 3: Processing and the data contract.** Write the cleaning rules as a numbered funnel with counts at each step. Define the JSON the page reads: `meta` (built time, freshness, the funnel), a `columns` list, and rows as arrays. Pages look columns up by name. Keep personal names and secrets out. Every published number gets a provenance record (see `RESEARCH_STANDARDS.md`).

**Step 4: Page.** Answer the core question above the fold. Show the raw records, not just aggregates. Filters in one row above the content. Every chart gets a table view. Light and dark modes, phone width, and a link to the source of each record.

**Step 5: Harden.**
- Guards that fail closed: minimum row counts, match rates and a no-big-drop check before publishing.
- Pinned `requirements.txt` and a concurrency group on the workflow.
- A browser smoke test.
- The project handbook from `templates/project/`.

**Step 6: Register and publish.** Add the project to `registry/projects.yaml`, start its lab notebook and open a `publish` PR for its site page.

## Repo layout

```
repo/
  .github/workflows/refresh.yml   # cron + dispatch + push-on-code; concurrency group; pinned ubuntu; commit only if changed
  scripts/config.py               # what's covered: the one place to change scope
  scripts/fetch.py                # pull, guards, data/raw/ (report through ::notice:: and ::error:: annotations)
  scripts/build.py                # clean, funnel, docs/data.json (publish guard against the previous build)
  data/raw/                       # committed snapshots so build.py runs offline
  docs/index.html, docs/js/common.js, docs/vendor/   # static pages, shared helpers, self-hosted libraries
  tests/smoke_test.py             # Playwright: renders, filters work, no JS errors, no sideways scroll
  handbook/                       # from templates/project/
  CLAUDE.md
  requirements.txt
```

## Patterns worth reusing

- **Keyset pagination** (`WHERE id > last_id ORDER BY id`) instead of offset paging.
- A **pre-flight count** on each source before downloading.
- **Guards that `exit 1` before writing anything**, so a bad week leaves last week's data live.
- **Annotations for run results.** Agents can read annotations through the API more easily than full logs.
- **Privacy scrubbing in fetch.** Reduce personal names to flags before they touch disk.
- **Shared page helpers** in one `common.js`.
- **Maps when needed:** self-hosted MapLibre, keyless CARTO and Esri basemaps, HTML markers, and a fallback to a blank style if tiles fail.

## Gotchas already paid for

- Claude's cloud sandbox blocks most outside hosts. **Fetch in Actions; push through a repo attached to the session.**
- Public-data tables get reloaded or truncated without notice (Denver's bed/bath table was 90% missing for two months). Always check counts and fail closed.
- Catalog descriptions get history wrong ("2008 to present" meant 2015). Verify date ranges with a query.
- Two sources' "neighborhood" or "category" fields rarely match. Join on geometry or an official key.
- Attributes are often the current state, not the state at the time of the event (house size today vs. at sale). Say so on the page.
- Never commit a data file built locally in a sandbox that lacked a source. Let the Action build what ships.
