PARAMETERS = {
    # ---------------------------------------------------------
    # READ/WRITE PARAMETERS
    # ---------------------------------------------------------
    "D_D_1":  {"name": "Raw water hardness", "unit": "°dH", "access": "rw"},
    "D_D_2":  {"name": "Target soft water hardness", "unit": "°dH", "access": "rw"},

    "D_A_4_1": {"name": "Installer name", "unit": None, "access": "rw"},
    "D_A_4_2": {"name": "Installer phone", "unit": None, "access": "rw"},
    "D_A_4_3": {"name": "Installer email", "unit": None, "access": "rw"},

    "D_C_1_1": {"name": "Language", "unit": None, "access": "rw"},
    "D_C_2_1": {"name": "Hardness unit", "unit": None, "access": "rw"},

    "D_C_4_2": {"name": "Clock time", "unit": "HH:MM", "access": "rw"},
    "D_C_5_2": {"name": "Date", "unit": "DD.MM.YYYY", "access": "rw"},
    "D_C_5_3": {"name": "DST auto-switch", "unit": None, "access": "rw"},

    "D_C_4_1": {"name": "Regeneration timing mode", "unit": None, "access": "rw"},
    "D_C_4_3": {"name": "Regeneration start 1", "unit": "HH:MM", "access": "rw"},
    "D_C_4_4": {"name": "Regeneration start 2", "unit": "HH:MM", "access": "rw"},
    "D_C_4_5": {"name": "Regeneration start 3", "unit": "HH:MM", "access": "rw"},

    "D_C_5_1": {"name": "Operating mode", "unit": None, "access": "rw"},

    "D_C_6_1": {"name": "Standby display active", "unit": None, "access": "rw"},
    "D_C_7_1": {"name": "Service interval", "unit": "days", "access": "rw"},

    "D_C_8_1": {"name": "LED ring behavior", "unit": None, "access": "rw"},
    "D_C_8_2": {"name": "LED blink on salt warning", "unit": None, "access": "rw"},

    # Base64 encoded fields
    "D_Y_8_1_1": {"name": "Email address 1", "unit": None, "access": "rw", "base64": True},
    "D_Y_8_1_2": {"name": "Email address 2", "unit": None, "access": "rw", "base64": True},
    "D_Y_8_1_3": {"name": "Email address 3", "unit": None, "access": "rw", "base64": True},

    "D_Y_8_2": {"name": "SMTP server", "unit": None, "access": "rw", "base64": True},
    "D_Y_8_3": {"name": "SMTP port", "unit": None, "access": "rw"},
    "D_Y_8_4": {"name": "SMTP username", "unit": None, "access": "rw", "base64": True},
    "D_Y_8_5": {"name": "SMTP password", "unit": None, "access": "rw", "base64": True},
    "D_Y_8_6": {"name": "Sender email", "unit": None, "access": "rw", "base64": True},
    "D_Y_8_7": {"name": "Phone number", "unit": None, "access": "rw", "base64": True},
    "D_Y_8_8": {"name": "Last name", "unit": None, "access": "rw", "base64": True},
    "D_Y_8_9": {"name": "Message text", "unit": None, "access": "rw"},
    "D_Y_8_10": {"name": "Send test email", "unit": None, "access": "rw"},

    # ---------------------------------------------------------
    # READ-ONLY PARAMETERS
    # ---------------------------------------------------------
    "D_A_1_7": {"name": "Total flow", "unit": "m3/h", "access": "r"},
    "D_A_2_3": {"name": "Salt range", "unit": "days", "access": "r"},
    "D_A_1_6": {"name": "Soft water hardness", "unit": "°dH", "access": "r"},

    "D_K_1": {"name": "Regeneration counter", "unit": None, "access": "r"},
    "D_K_2": {"name": "Soft water volume", "unit": "m3", "access": "r"},
    "D_A_2_2": {"name": "Days until next service", "unit": "days", "access": "r"},

    # Network
    "D_C_3_6_1": {"name": "IP address", "unit": None, "access": "r"},
    "D_C_3_6_2": {"name": "Default gateway", "unit": None, "access": "r"},
    "D_C_3_6_3": {"name": "Primary DNS", "unit": None, "access": "r"},
    "D_C_3_6_4": {"name": "Secondary DNS", "unit": None, "access": "r"},
    "D_C_3_6_5": {"name": "WLAN status", "unit": None, "access": "r"},

    # Water consumption
    "D_Y_1": {"name": "Water consumption yesterday", "unit": "L", "access": "r"},
    "D_Y_2_1": {"name": "Water consumption day -1", "unit": "L", "access": "r"},
    # ... up to D_Y_2_27
    "D_Y_3": {"name": "Salt consumption per year", "unit": "kg", "access": "r"},

    # Regeneration
    "D_Y_5": {"name": "Current regeneration step", "unit": None, "access": "r"},
    "D_Y_7": {"name": "Commissioning date", "unit": None, "access": "r"},
    "D_Y_14": {"name": "Next regeneration", "unit": None, "access": "r"},

    # MC-specific exchanger status
    "D_Y_10_1": {"name": "Remaining capacity exchanger 1", "unit": "%", "access": "r"},
    "D_Y_10_2": {"name": "Remaining capacity exchanger 2", "unit": "%", "access": "r"},
    "D_Y_13": {"name": "Exchanger in operation", "unit": None, "access": "r"},

    # ---------------------------------------------------------
    # CODE=005 PROTECTED PARAMETERS
    # ---------------------------------------------------------
    "D_A_1_1": {"name": "Current flow A1", "unit": "m3/h", "access": "r", "code": "005"},
    "D_A_1_2": {"name": "Remaining capacity A1", "unit": None, "access": "r", "code": "005"},
    "D_A_1_3": {"name": "Capacity number A1", "unit": None, "access": "r", "code": "005"},
    "D_A_2_1": {"name": "Remaining time/volume A1", "unit": None, "access": "r", "code": "005"},
    "D_A_3_1": {"name": "Last regeneration A1", "unit": None, "access": "r", "code": "005"},
    "D_A_3_2": {"name": "Percentage A1", "unit": "%", "access": "r", "code": "005"},

    # Exchanger 2 (MC32)
    "D_A_1_4": {"name": "Current flow A2", "unit": "m3/h", "access": "r", "code": "005"},
    "D_A_1_5": {"name": "Remaining capacity A2", "unit": None, "access": "r", "code": "005"},
    "D_A_1_8": {"name": "Capacity number A2", "unit": None, "access": "r", "code": "005"},
    "D_A_2_4": {"name": "Remaining time/volume A2", "unit": None, "access": "r", "code": "005"},
    "D_A_3_4": {"name": "Last regeneration A2", "unit": None, "access": "r", "code": "005"},
    "D_A_3_5": {"name": "Percentage A2", "unit": "%", "access": "r", "code": "005"},

    # Mixing valve (MC32)
    "D_A_1_9": {"name": "Mixing valve flow", "unit": "m3/h", "access": "r", "code": "005"},
    "D_A_1_6": {"name": "Soft water hardness", "unit": "°dH", "access": "r", "code": "005"},

    # Flow statistics
    "D_K_3": {"name": "Peak flow parallel", "unit": "m3/h", "access": "r", "code": "005"},
    "D_K_4": {"name": "Overload duration", "unit": "min", "access": "r", "code": "005"},
    "D_K_14": {"name": "Exchanger 1 peak flow", "unit": "m3/h", "access": "r", "code": "005"},
    "D_K_15": {"name": "Overload duration A1", "unit": "min", "access": "r", "code": "005"},
    "D_K_16": {"name": "Exchanger 2 peak flow", "unit": "m3/h", "access": "r", "code": "005"},
    "D_K_17": {"name": "Overload duration A2", "unit": "min", "access": "r", "code": "005"},
    "D_K_18": {"name": "Soft water volume A1", "unit": "m3", "access": "r", "code": "005"},
    "D_K_19": {"name": "Soft water volume A2", "unit": "m3", "access": "r", "code": "005"},
    "D_K_20": {"name": "Raw water mixing volume", "unit": "m3", "access": "r", "code": "005"},
    "D_K_21": {"name": "Refill volume", "unit": "L", "access": "r", "code": "005"},
}
