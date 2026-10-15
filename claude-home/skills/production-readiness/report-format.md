# Readiness report format

Use exactly these sections.

## Validated

List only controls supported by an observed file, command, test or deployment response. Include the evidence.

## P0 — release blocker

A likely compromise, data loss, unavailable critical path or unbounded cost. For each item: impact, evidence, smallest safe correction and owner or missing authority.

## P1 — correct before expected scale

A weakness that will likely fail under normal load, dependency failure or operational recovery. Include impact, evidence and correction.

## P2 — planned improvement

Important hardening, privacy, observability or maintainability work that does not block the immediate release.

## Not verified

State what was not checked and why: no production access, no test account, no load-test authorization, unavailable tooling or missing evidence.

End with: `Checked: … | Left: …`.
