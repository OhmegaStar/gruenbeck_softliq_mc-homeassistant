# Releasing

This project uses Semantic Versioning. The Home Assistant integration version is stored in:

`custom_components/gruenbeck_softliq_mc/manifest.json`

Git release tags use the same version with a `v` prefix, for example:

- Manifest version: `0.1.3`
- Git tag: `v0.1.3`
- GitHub release: `v0.1.3`

## Prerequisites

- Windows PowerShell
- Git configured with permission to push to the repository
- A clean working tree
- All changes for the release committed to the current branch

The release script uses commits after the latest release tag to generate the new changelog entry. Do not leave uncommitted feature changes when running it.

## Release Procedure

1. Review the current state and confirm the branch is up to date:

   ```powershell
   git status
   git pull origin main
   ```

2. Commit the changes that should be included in the release:

   ```powershell
   git add .
   git commit -m "Describe the changes"
   ```

3. Run the release script without pushing:

   ```powershell
   .\tools\release.ps1 -Version 0.1.3
   ```

   The script will:
   - Verify that the working tree is clean.
   - Reject an existing `v0.1.3` tag.
   - Find the latest release tag.
   - Extract commit subjects since that tag.
   - Add a file-change summary since that tag.
   - Insert a dated `0.1.3` section into `CHANGELOG.md`.
   - Update `manifest.json` to `0.1.3`.
   - Create a `Release v0.1.3` commit and `v0.1.3` tag.

4. Review the generated release commit and changelog:

   ```powershell
   git show --stat --oneline HEAD
   git show HEAD:CHANGELOG.md
   git status
   ```

5. Push the release commit and tag:

   ```powershell
   git push origin main
   git push origin v0.1.3
   ```

   Or use the script's push option in step 3 to perform both pushes automatically:

   ```powershell
   .\tools\release.ps1 -Version 0.1.3 -Push
   ```

## GitHub Actions

Pushing a tag matching `v*.*.*` starts `.github/workflows/release.yml`.

The workflow:

1. Checks that the tag is a valid `vX.Y.Z` version.
2. Checks that the tag version matches `manifest.json`.
3. Extracts the matching version section from `CHANGELOG.md`.
4. Creates the GitHub release using that changelog section as its description.

If the tag and manifest versions do not match, or the changelog entry is missing, the workflow fails instead of publishing an inconsistent release.

## Troubleshooting

### The script says the working tree is not clean

Commit or remove all local changes before running the release script. This includes changes to the integration, documentation, workflow files, and `CHANGELOG.md`.

### The script says no commits were found

The script found no commits after the latest release tag. Commit the changes to be released first.

### The tag already exists

Choose a new version. Do not reuse or move a published release tag.

### GitHub Actions rejects the release

Check that all three values are identical:

- `manifest.json`: `"version": "0.1.3"`
- Git tag: `v0.1.3`
- Changelog heading: `## [0.1.3]`
