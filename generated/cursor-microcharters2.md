## Micro-charters for testing the E-Primer app (filtered: only not-yet-done ideas)

Scope: `eprimer/` single-page web app. Excludes items already covered by `tests/test_eprimer.py` and those explicitly listed in `docs-as-output/bugs.md`.

Note: Each micro-charter is a short, time-boxed mission with purpose, approach, and “done-when”.

### 1) Word boundary definition beyond ASCII
- Purpose: Characterize tokenization for non-ASCII and invisible separators.
- Start: NBSP (U+00A0), EM SPACE (U+2003), ZERO WIDTH JOINER (U+200D), emoji adjacent to words, punctuation from various Unicode categories.
- Heuristics: Contrast behavior vs ASCII space; verify counts and highlighting remain coherent.
- Done-when: Boundary rules for these characters are documented with examples.

### 2) Locale-specific casing pitfalls
- Purpose: Validate `.toLowerCase()` behavior under locales like Turkish (I/ı/İ/i) and Greek sigma.
- Start: Inputs containing "IS", "İS", "ıS", mixed-case variants of discouraged words.
- Risks: Missed matches due to locale rules; inconsistent detection across browsers.
- Done-when: Outcomes cataloged; decision recorded on whether to normalize differently.

### 3) Statistics update timing and race conditions
- Purpose: Ensure `wordCount`, `discouragedWordCount`, and `possibleViolationCount` update atomically after interactions.
- Start: Rapid repeated clicks, paste large text then immediately click, click while rendering long text.
- Heuristics: Look for transient mismatches between rendered highlights and numbers.
- Done-when: No observable race; otherwise, minimal repro documented.

### 4) International and bidirectional text handling
- Purpose: Explore behavior with RTL scripts and mixed-direction content.
- Start: Arabic/Hebrew sentences with discouraged words analogs, mixed LTR-RTL lines, CJK text without spaces, emoji sequences with ZWJ.
- Risks: Rendering or counting anomalies; cursoring/selection oddities in the textarea.
- Done-when: Differences vs LTR ASCII documented with examples.

### 5) Reset and state isolation between runs
- Purpose: Confirm per-run state is fully reset regardless of previous input size/content.
- Start: Alternate empty and very long inputs across multiple runs; interleave with inputs containing HTML-like text.
- Heuristics: Watch for stale highlights or counters; ensure `resetGlobalVariables` suffices.
- Done-when: No state leakage observed; repro steps captured if any.

### 6) Quantified performance thresholds
- Purpose: Determine practical input size where rendering or interaction becomes sluggish.
- Start: Increase input size in steps (e.g., 10k, 50k, 100k characters; long single-token lines vs many small tokens).
- Heuristics: Time to first paint of output, time to updated stats after click.
- Done-when: Thresholds summarized; opportunities for optimization listed.

## Ready-to-run micro-charters

The previous generic product charters were unrelated to this static demo app and have been removed to avoid noise.


