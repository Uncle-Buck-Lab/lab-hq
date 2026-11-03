# Playbook: recurring report

For any project that publishes a sourced report on a schedule. Distilled from how the AI Money Report is built: public data through scheduled pipelines, an extraction layer that reads and explains it, and a human review of every issue before it ships.

## Define the report before the brand

1. **The promise.** One sentence on what every issue delivers to the reader.
2. **The recurring questions.** Three to five questions every issue answers. They decide which data gets built.
3. **The issue skeleton.** A fixed order of sections, so readers know where to look and the pipeline knows what to fill.
4. **The reader.** Who it's for and what they don't already know. That sets the voice file.
5. **The name comes last.** Lock it after three dry-run issues, once the product exists to describe.

## The pipeline

```
sources ──► pipelines/<source>/ ──► facts file ──► draft ──► number check ──► review PR ──► publish
              (Actions, scheduled)    (provenance     (agent)    (every number             (founder)
                                       records)                   matched to a fact)
```

- **One pipeline per source**, each with fail-closed guards and a run log.
- **Structured sources first.** Filings, official datasets and APIs beat scraping. A hand-kept, sourced table beats a fragile scraper for numbers that change once a year.
- **The facts file is the contract.** Every number the draft may use is a provenance record in it. The draft writer can't introduce a number that isn't there.
- **Issues assemble themselves.** On the schedule, an Action builds the facts file and opens a pull request with a starting draft. The founder edits and approves in that PR.
- **Snapshots are saved** to a branch or release assets, so any issue can be rebuilt from what was known at the time.

## The extraction layer

- **Readers have no tools** and return structured output checked against a schema (see `AGENT_SAFETY.md`).
- **Versioned prompts** live in the repo; each version is a file, never edited in place.
- **Gold sets with traps.** Hand-checked cases, including ones designed to mislead, score every extractor. A prompt or model change reruns them; anything below the bar blocks the merge.
- **Temperature 0** for extraction, with the setting in the cache key.
- **Quotes must match.** A figure counts only if its supporting quote appears word for word in the source and the figure appears in the quote. Otherwise it is flagged, never counted.
- **Confidence routes review.** High confidence is accepted, medium is accepted with a sampled spot check, low always goes to a human.
- **Per-run caps** on items and cost keep spend predictable.

## Before each issue ships

- Every number traces to a provenance record; the number check passes.
- [TRUST_RULES.md](../handbook/TRUST_RULES.md) and [WRITING_RULES.md](../handbook/WRITING_RULES.md) pass.
- Coverage gaps are stated next to the data they affect.
- Labels (fact, stated, our read) are applied.
- The corrections log is current.
- The PR carries the `publish` label and the founder's approval.

## Operations

- A daily health check keeps one "Pipeline health" issue current and comments only on breakage or recovery.
- Decisions go in the project's decision log with a date and a reason, newest first.
