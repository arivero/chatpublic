# One primary-source claim audit

**Model role:** GPT-6 Sol for retrieval and extraction; escalate a consequential technical interpretation to the parent research model only when needed.

**Inputs:** [workplan](../../notes/workplan.md), [draft comparison](../../notes/draft_comparison.md), `{{BASE_COMMIT}}`; parent supplies one exact `{{CLAIM_OR_SOURCE}}` (historical Schwarz 1971/Scherk, or an AI-paper claim). Write only `{{OUTPUT_PATH}}`.

**Task:** Retrieve or inspect the primary source for `{{CLAIM_OR_SOURCE}}`, and verify one consequential claim against the actual text, equation, page, and version. Distinguish an original proposal, later interpretation, and our own construction. If source access fails, record the attempted route and mark the claim unverified. For uploaded PDFs, check consequential equations on the original page rather than extracted text alone.

**Deliverable and stop:** A compact claim/evidence/provenance record with precise citation or access limitation in `{{OUTPUT_PATH}}`. Stop after one claim; do not turn the source audit into a scientific endorsement.

**Pitfall:** Similar words such as “quark–gluon,” “quark–diquark,” and “lepton–meson” do not identify the same historical model.
