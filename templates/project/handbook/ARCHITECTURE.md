# Architecture

## How the pieces fit

Describe the flow from source to page in a few lines, or draw it:

```
source ──► scripts/fetch.py ──► data/raw/ ──► scripts/build.py ──► docs/data.json ──► docs/index.html
```

## The data contract

The file the page reads, its fields and what each means. Pages look columns up by name, so renaming a column is a breaking change.

| Field | Type | Meaning |
| --- | --- | --- |
| | | |

## Front-end conventions

Shared helpers, page structure, how filters are stored.
