# Changelog
Alle væsentlige ændringer i dette projekt dokumenteres her.

Formatet følger **Keep a Changelog**  
og versionering følger **Semantic Versioning**.

---

## [0.1.3] - 2026-09-05
### Changed
- fix for missing icon and branding (ab1eabc)
- default scan interval is 90 seconds (c073d94)
- tooling - Release workflow automation (3a593e7)

### Files changed
```text
 .github/workflows/release.yml                   |  16 ++++
 README.md                                       |  14 +--
 custom_components/gruenbeck_softliq_mc/icon.png | Bin 2139956 -> 254614 bytes
 custom_components/gruenbeck_softliq_mc/logo.png | Bin 254614 -> 2139956 bytes
 docs/RELEASING.md                               | 108 ++++++++++++++++++++++++
 tools/release.ps1                               |  36 +++++++-
 6 files changed, 162 insertions(+), 12 deletions(-)
```
## [Unreleased]
### Added
- Intet endnu.

### Changed
- Intet endnu.

### Fixed
- Intet endnu.

---

## [0.1.0] – 2026-02-16
### Added
- Første officielle release af **Grünbeck softliQ MC Home Assistant integration**.
- Fuldt lokalt API via `/mux_http` uden cloud-afhængighed.
- 40+ sensorer genereret automatisk fra parameter‑mapping.
- Switches for:
  - Operating mode  
  - LED ring behavior  
  - LED blink on salt warning  
  - Send test email  
- Services:
  - `force_regeneration`
  - `send_test_email`
- DataUpdateCoordinator for effektiv polling.
- Diagnostics support.
- Dansk og engelsk oversættelse.
- HACS‑manifest.
- Logo og ikon (SVG/PNG).

---

## [0.0.1] – 2026-02-15
### Added
- Intern udviklingsversion.
- Grundlæggende Python‑klient til Grünbeck softliQ MC.
- Parameter‑mapping og test scripts.

---


