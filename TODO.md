# TODO

This repository tracks the active maintenance and delivery backlog for the Grünbeck softliQ MC Home Assistant integration.

## Working rules

- Keep this backlog updated as work progresses.
- Mark items complete when the related work is done; do not clear the list except after a major version release.
- Add new tasks when they meaningfully support a bug fix, feature, refactor, or release-readiness item.
- If a proposed item is uncertain, ambiguous, or likely to affect scope or priorities, ask for consensus before adding it.
- The checked-in repository instructions are the source of truth for release handling. In this repo, the authoritative guidance is in `.github/copilot-instructions.md` and `docs/RELEASING.md`. The PowerShell helper at `tools/release.ps1` may differ from the written instructions in minor implementation details; follow the documented repo instructions first and treat the script as a convenience helper, not as the authoritative policy.

## Ordered backlog

- [x] Establish the repository working rules and release-authority guidance.
- [x] Confirm the integration scope and architecture
  - Reviewed the Home Assistant integration entry points, manifest, config flow, and runtime modules under `custom_components/gruenbeck_softliq_mc/`.
  - Confirmed the repository is a HACS/Home Assistant integration and that compatibility expectations are documented in the repo guidance.

- [ ] Maintain the core device integration contract
  - Keep the library/API layer for the Grünbeck MC webserver stable and defensive.
  - Validate device responses and session state before writing settings or triggering actions.
  - Preserve existing entity names and configuration behavior.

- [ ] Review and improve entity coverage
  - Evaluate sensors, switches, and services for correctness, naming consistency, and missing edge-case handling.
  - Keep changes targeted to the root cause and avoid broad scope churn.

- [ ] Harden operational behavior and diagnostics
  - Check coordinator, diagnostics, and error handling paths for slow or single-threaded webserver constraints.
  - Prefer explicit validation of API results and service payloads before performing writes.

- [ ] Update user-facing documentation and release notes
  - Keep README, docs, and changelog entries aligned with behavior changes.
  - Add or update release notes for any feature, fix, or compatibility change.

- [ ] Prepare a release using the repository release instructions
  - Verify the working tree is clean and all release-ready changes are committed.
  - Ensure the diff is limited to `custom_components/` and `hacs.json` unless a documented exception is required.
  - Use the documented release procedure from `.github/copilot-instructions.md` / `docs/RELEASING.md` as the source of truth.

- [ ] Publish the release tag and verify automation
  - Run the release helper only after confirming the intended version and release contents.
  - Push the release commit/tag only when ready.
  - Confirm the GitHub Action release matches the changelog and manifest version.

## Current release process summary

The repository instructions specify:

1. Commit the intended changes.
2. Ensure the diff for the release is limited to `custom_components/` and `hacs.json`.
3. Run `pwsh -File .\tools\release.ps1 -Version 0.1.1`.
4. Use `-Push` only when ready to create and push the tag.
5. Let the GitHub Action in `.github/workflows/release.yml` create the GitHub Release from the tag.

This is the authoritative process for this repo. If the helper script differs from the written instructions, prefer the instructions and the checked-in release docs.
