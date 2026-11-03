# Research standards

Research quality is what the lab is known for, or nothing is. These standards apply to every project that publishes a claim.

## Before the research

Every significant piece of research writes these down first, in the project repo:

- The question, and what answer would change a decision.
- The method, the sources and why those sources.
- Definitions and assumptions, especially for numbers that sound similar but aren't.
- Known limits of the data.

## Sources

1. **Primary sources first.** A filing, a law, a dataset, an official record. News coverage is a lead, not a source.
2. **Record the retrieval.** Every source has a link and a retrieval date.
3. **Archive what might change.** Pages, filings and datasets that could be edited or removed get a snapshot saved with the project's data.
4. **Never fabricate a citation.** If a source can't be found, the claim doesn't run.

## The provenance record

Every published number or fact has a record in the project's data, in this shape:

```yaml
claim: "Example Corp spent $2.4B on buildings and equipment in the 12 months to September"
value: 2400000000
unit: USD
source_url: https://www.sec.gov/Archives/edgar/data/<cik>/<filing>.htm
source_title: Example Corp Form 10-Q, quarter ended Sep 30
retrieved: 2026-11-03
snapshot: data/snapshots/2026-11-03/example-corp-10q.htm
method: Sum of the last four quarters of PaymentsToAcquirePropertyPlantAndEquipment
label: fact          # fact | stated | estimate | our-read
```

A draft's numbers are checked against these records before review. A number with no record doesn't ship.

## Labels

Keep these apart in the data and in the writing:

- **Fact:** what the document shows.
- **Stated:** what a company or official says, in their own words.
- **Estimate:** a number the lab calculated or modeled, with its method.
- **Our read:** the lab's interpretation, clearly marked.

For money, also keep apart: announced, committed, actually spent and forecast. They are different numbers and are never summed together.

For political and financial research, keep different kinds of activity in separate categories rather than combining them into one misleading total.

## Checking

- Material claims are verified independently of the person or agent that found them.
- Claims the lab expects to be true get checked hardest.
- Important analyses are reproducible from the repo: the code, the inputs and the steps.
- Uncertainty is stated next to the claim it affects, not in a footnote nobody reads.
