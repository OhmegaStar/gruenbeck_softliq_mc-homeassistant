# Grünbeck softliQ MC – Home Assistant Integration

A fully local, zero‑cloud Home Assistant integration for **Grünbeck softliQ:MC** water softeners.


Supports:
- MC16
- MC32
- MC variants using the xPico Webserver (`/mux_http`)

## Features

### ✔ Sensors (40+)
- Raw water hardness
- Soft water hardness
- Flow rate
- Salt range (days)
- Regeneration status
- Exchanger status (MC only)
- Water consumption (daily history)
- Salt consumption
- Network status
- Service interval
- Remaining exchanger capacity
- Peak flow statistics (MC32)

### ✔ Switches
- Operating mode
- LED ring behavior
- LED blink on salt warning
- Send test email

### ✔ Services
- `gruenbeck_softliq_mc.force_regeneration`
- `gruenbeck_softliq_mc.send_test_email`

### ✔ Local API
Uses the built‑in Grünbeck Webserver:

http://[your-device-local-ip]/mux_http


No cloud. No external dependencies.

---

## Installation (HACS Custom Repository)

1. Go to **HACS → Integrations → Custom Repositories**
2. Add: https://github.com/ohmegastar/gruenbeck_softliq_mc-homeassistant
3. Category: **Integration**
4. Install
5. Restart Home Assistant
6. Add integration: **Grünbeck softliQ MC**

---

## Configuration

Enter:
- Device IP
- Scan interval (default: 30s)

The integration will automatically:
- Discover all readable parameters
- Create sensors
- Create switches
- Handle code=005 protected parameters

---

## Credits

Based on Grünbeck Webserver documentation and reverse engineering of the `/mux_http` API.
Cloned off https://github.com/tizianodeg/gruenbeck_softliQ_SC

Developed by **@ohmegastar**.
