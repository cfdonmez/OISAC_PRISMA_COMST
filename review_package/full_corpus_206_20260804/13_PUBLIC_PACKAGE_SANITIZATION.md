# Public-package sanitization note

Date: 2026-08-04
Scope: `phase_e/` and `phase_f/` copies inside this Git review package only.

The local canonical Phase-E and Phase-F checkpoints retain original runtime provenance. Before public Git publication, the copied builder/verifier scripts were parameterized with `OISAC_PHASE_D_WORKBOOK` and `OISAC_PHASE_E_CROSSWALK`, and absolute workstation paths in copied QA metadata were replaced by logical filenames.

This path-only sanitization does not change analytical records, classifications, scores, counts, assertions, or the recorded SHA-256 values of the scientific source workbook and frozen crosswalk. The Git-package `SHA256SUMS.txt` hashes the sanitized public copies; the canonical local checkpoint manifests continue to hash the unsanitized audit originals.
