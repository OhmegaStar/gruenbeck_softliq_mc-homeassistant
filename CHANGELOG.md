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
## [0.1.4] - 2026-09-05
### Changed
- tools cleanup, and enable test clients in tools to run in uv (3c61409)
- tooling fix - workflow updated to current github actions (d37d15c)

### Files changed
```text
 .github/workflows/release.yml                      |   4 +-
 .gitignore                                         |   1 +
 .../gruenbeck_softliq_mc/coordinator.py            |  11 +-
 pyproject.toml                                     |  12 +
 tools/device_probe.py                              | 130 +++++
 tools/gruenbeck_client.py                          |  43 --
 tools/gruenbeck_mc.py                              |  95 ----
 tools/mc32_dict_scanner.py                         | 323 ------------
 tools/mc32_full_param_scanner.py                   |  85 ----
 tools/mc32_param_scanner.py                        |  76 ---
 tools/mc32_test_client.py                          |  74 ---
 tools/smoke_test_api_modes.py                      |  34 ++
 tools/smoke_test_client.py                         |  35 ++
 tools/softliq_params.txt                           |   0
 tools/test_api_modes.py                            |  48 --
 tools/test_client.py                               | 115 -----
 uv.lock                                            | 540 +++++++++++++++++++++
 17 files changed, 759 insertions(+), 867 deletions(-)
```
## [0.1.5] - 2026-09-05
### Changed
- fix that each sensor was self poling, causing overload of requests to the device, and queue / lock contention on the request interface, should remove the may errors in the log from many polling sensors (2a01b3f)
- move lbrand resources to correct folder (9e11d38)

### Files changed
```text
 .../gruenbeck_softliq_mc/{ => brand}/icon.png      | Bin
 .../gruenbeck_softliq_mc/{ => brand}/logo.png      | Bin
 custom_components/gruenbeck_softliq_mc/const.py    |   2 -
 .../gruenbeck_softliq_mc/gruenbeck_mc.py           |   4 -
 custom_components/gruenbeck_softliq_mc/sensor.py   |  85 ++++++---------------
 custom_components/gruenbeck_softliq_mc/switch.py   |  50 ++++--------
 6 files changed, 37 insertions(+), 104 deletions(-)
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




