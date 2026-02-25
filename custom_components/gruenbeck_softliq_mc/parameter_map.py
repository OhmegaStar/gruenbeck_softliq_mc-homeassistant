PARAMETERS = {
    # ---------------------------------------------------------
    # SoftLiq MC:32 parameters as Organized as in the WEB UI
    # ---------------------------------------------------------
    # The Dict format is: "PARAM": {"name": "userfriendly name", type: "datatype", "unit": "°dH", dict: {}, "access": "rw", "base64": True, code: "XXX"},

    #UI menus and calls:
    #Current Values In General:
    #id=943&show=D_A_1_7|D_A_2_3|D_A_1_6|D_A_2_2|D_K_1|D_K_2|D_Y_5|D_Y_13~
    #Current Values Exchanger Tank:
    #id=943&show=D_A_1_1|D_A_1_3|D_A_1_2|D_Y_10_1|D_A_2_1|D_A_3_1|D_A_1_4|D_A_1_8|D_A_1_5|D_Y_10_2|D_A_2_4|D_A_3_4~
    #Contact Person:
    #id=943&show=D_A_4_1|D_A_4_2|D_A_4_3~
    #Manual REgeneration / Last Regeneration:
    #id=943&show=D_B_1|D_Y_4_1|D_Y_4_2|D_Y_4_3|D_Y_4_4|D_Y_4_5|D_Y_4_6|D_Y_4_7|D_Y_4_8|D_Y_4_9|D_Y_4_10|D_Y_4_11|D_Y_4_12|D_Y_4_13|D_Y_4_14~
    #Water Consumption:
    #id=943&show=D_Y_2_1|D_Y_2_2|D_Y_2_3|D_Y_2_4|D_Y_2_5|D_Y_2_6|D_Y_2_7|D_Y_2_8|D_Y_2_9|D_Y_2_10|D_Y_2_11|D_Y_2_12|D_Y_2_13|D_Y_2_14|D_Y_2_15|D_Y_2_16|D_Y_2_17|D_Y_2_18|D_Y_2_19|D_Y_2_20|D_Y_2_21|D_Y_2_22|D_Y_2_23|D_Y_2_24|D_Y_2_25|D_Y_2_26|D_Y_2_27~
    #Salt Consumption:
    #id=943&show=D_Y_3_1|D_Y_3_2|D_Y_3_3|D_Y_3_4|D_Y_3_5|D_Y_3_6|D_Y_3_7|D_Y_3_8|D_Y_3_9|D_Y_3_10|D_Y_3_11|D_Y_3_12|D_Y_3_13|D_Y_3_14|D_Y_3~
    #System Parameters:
    #id=943&show=D_C_1_1|D_C_4_2|D_C_5_2|D_C_5_3|D_C_6_1|D_C_8_1|D_C_8_2|D_D_1|D_D_2|D_E_1|D_Y_9|D_Y_9_8|D_Y_9_24|D_C_7_1|D_Y_15~
    #Regeneration:
    #id=943&show=D_C_4_1|D_C_4_3|D_C_4_4|D_C_4_5|D_Y_14|D_C_5_1|D_C_6_3|D_C_6_4|D_C_6_5|D_C_6_6|D_C_6_7|D_C_6_8|D_C_6_9~
    #Wi-fi Configuration:
    #id=943&show=D_C_3_7_1|D_C_3_7_2|D_C_3_7_3|D_C_3_1|D_Y_8_1_1|D_Y_8_1_2|D_Y_8_1_3|D_Y_8_2|D_Y_8_3|D_Y_8_4|D_Y_8_5|D_Y_8_6|D_Y_8_7|D_Y_8_8|D_Y_8_10|D_Y_8_11|D_Y_8_12|D_Y_12~
        #UI Code Protected Area:
        # System Data Record: code 290
        #id=943&code=290&show=D_F_6~
        # Installer Level: code 005
        #id=943&code=005&show=D_F_1|D_F_3_1|D_F_3_2|D_F_3_3|D_F_3_4|D_F_3_5|D_F_3_6|D_F_3_7|D_F_4_1|D_F_4_2|D_F_4_3|D_F_4_4|D_F_4_5|D_F_4_6|D_F_4_7|D_F_5_1|D_F_5_2|D_F_5_3|D_F_5_4|D_F_5_5|D_F_5_6|D_F_5_7|D_F_7|D_F_8|D_F_9|D_G_5|D_K_18|D_K_19|D_K_20|D_K_21|D_K_3|D_K_4|D_K_14|D_K_15|D_K_16|D_K_17|D_F_10|D_F_11~
        # Programmable Input and Output: code 005
        #id=943&code=005&show=D_G_1|D_G_2|D_G_3|D_Y_8_9|D_G_4~
        # Control Parameters: code
        # id=943&code=XXX&show=D_H_2|D_H_3|D_H_4|D_H_5|D_H_6|D_H_7|D_H_8|D_H_9|D_H_11|D_H_12|D_H_13|D_H_15~
        # Hydraulic Values: code
        #id=943&code=XXX&show=D_I_1|D_I_2|D_I_4|D_I_5|D_I_6|D_I_7|D_I_8|D_I_9|D_I_10|D_I_11|D_I_12|D_I_15|D_I_16|D_I_17|D_I_19|D_I_18|D_I_20~
        # Step Intervals: code
        #id=943&code=XXX&show=D_J_1|D_J_3|D_J_4|D_J_5|D_J_6|D_J_7|D_J_8|D_J_9~
        # Counter Readings: code
        #id=943&code=XXX&show=D_K_5|D_K_6|D_K_7|D_K_8_1|D_K_8_2|D_K_8_3|D_K_8_4|D_K_8_5|D_K_8_6|D_K_8_7|D_K_9_1|D_K_9_2|D_K_9_3|D_K_9_4|D_K_9_5|D_K_9_6|D_K_9_7~
        # Error Memory & Change History: code 005
        #id=943&code=005&show=D_K_10_1|D_K_10_2|D_K_10_3|D_K_10_4|D_K_10_5|D_K_10_6|D_K_10_7|D_K_10_8|D_K_10_9|D_K_10_10|D_K_10_11|D_K_10_12|D_K_10_13|D_K_10_14|D_K_10_15|D_K_10_16|D_K_13|D_B_2|D_K_11_1|D_K_11_2|D_K_11_3|D_K_11_4|D_K_11_5|D_K_11_6|D_K_11_7|D_K_11_8|D_K_11_9|D_K_11_10|D_K_11_11|D_K_11_12|D_K_11_13|D_K_11_14|D_K_11_15|D_K_11_16~
        # Reset Error Memory: code
        #id=943&code=XXX&show=D_M_3_3~
    #Units:
    #Seems to be UI Setting nothing really happens in the gruenbech.js javascript here.

    # ---------------------------------------------------------
    # Current Values In General:
    # ---------------------------------------------------------
    #id=943&show=D_A_1_7|D_A_2_3|D_A_1_6|D_A_2_2|D_K_1|D_K_2|D_Y_5|D_Y_13~
    "D_A_1_7": {"name": "Current flow total", "unit": "m3/h", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_2_3": {"name": "Salt range", "unit": "days", "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_1_6": {"name": "Actual value soft water hardness", "unit": "°dH", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_2_2": {"name": "Days till Maintenance Due", "unit": "days", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_K_1": {"name": "Number of Regenerations", "unit": None, "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_K_2": {"name": "Soft Water Volume", "unit": "m3", "type": "number", "dict": None, "access": "r", "base64": False, "code": None, "device_class": "water", "state_class": "total_increasing"},
    "D_Y_5": {"name": "Current Regeneration Step", "unit": None, "type": "String", "dict": {"0": "No Regeneration", "1": "Fill Brine Tank", "2": "Salting", "3": "Slow Rinsing", "4": "Backwashing", "5": "Washing Out"}, "access": "r", "base64": False, "code": None},
    "D_Y_13": {"name": "Exchange Tank In Operation", "unit": None, "type": "String", "dict": {"0": "Both Exchange Tanks Disrupted", "1": "Only Exchange Tank 1", "2": "Only Exchange Tank 2", "3": "Both Exchanger Tanks"}, "access": "r", "base64": False, "code": None},
    #{'data': {'code': 'ok', 'D_A_1_7': '0.00', 'D_A_2_3': '99', 'D_A_1_6': '4', 'D_A_2_2': '242', 'D_K_1': '6940', 'D_K_2': '2534', 'D_Y_5': '0', 'D_Y_13': '3'}}
    #Added these that do not belong on a page, but exists in the footer
    "D_Y_6": {"name": "Software Version", "unit": None, "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
    "D_Y_7": {"name": "Unit Startup Date", "unit": None, "type": "string", "dict": None, "access": "r", "base64": False, "code": None},

    # ---------------------------------------------------------
    # Current Values Ecchanger Tank:
    # ---------------------------------------------------------
    #id=943&show=D_A_1_1|D_A_1_3|D_A_1_2|D_Y_10_1|D_A_2_1|D_A_3_1|D_A_1_4|D_A_1_8|D_A_1_5|D_Y_10_2|D_A_2_4|D_A_3_4~
    #Tank 1
    "D_A_1_1": {"name": "Tank 1 Current Flow", "unit": "m3/h", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_1_3": {"name": "Tank 1 Capacity Rate", "unit": "m3 x °dH", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_1_2": {"name": "Tank 1 Residual Capacity", "unit": "m3", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_Y_10_1": {"name": "Tank 1 Capacity Remanining %", "unit": "%", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_2_1": {"name": "Tank 1 Remanining Duration ro Residual Quantity Current Step", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_3_1": {"name": "Tank 1 Time of Last Regeneration", "unit": "date-time", "type": "string", "dict": None, "access": "r", "base64": False, "code": None},

    #Tank 2
    "D_A_1_4": {"name": "Tank 2 Current Flow", "unit": "m3/h", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_1_8": {"name": "Tank 2 Capacity Rate", "unit": "m3 x °dH", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_1_5": {"name": "Tank 2 Residual Capacity", "unit": "m3", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_Y_10_2": {"name": "Tank 2 Capacity Remanining %", "unit": "%", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_2_4": {"name": "Tank 2 Remanining Duration ro Residual Quantity Current Step", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    "D_A_3_4": {"name": "Tank 2 Time of Last Regeneration", "unit": "date-time", "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
    #{'data': {'code': 'ok', 'D_A_1_1': '0.00', 'D_A_1_3': '6.87', 'D_A_1_2': '0.26', 'D_Y_10_1': '61', 'D_A_2_1': '0.0l', 'D_A_3_1': '18.02.2026 09:02Uhr', 'D_A_1_4': '0.00', 'D_A_1_8': '6.87', 'D_A_1_5': '0.28', 'D_Y_10_2': '65', 'D_A_2_4': '0.0l', 'D_A_3_4': '18.02.2026 09:25Uhr'}}

    # ---------------------------------------------------------
    # Contact Person:
    # ---------------------------------------------------------
    #id=943&show=D_A_4_1|D_A_4_2|D_A_4_3~
    "D_A_4_1": {"name": "Installer Name", "unit": None, "type": "string", "dict": None, "access": "rw", "base64": True, "code": None},
    "D_A_4_2": {"name": "Installer Phone NUmber", "unit": None, "type": "string", "dict": None, "access": "rw", "base64": True, "code": None},
    "D_A_4_3": {"name": "Installer Email", "unit": None, "type": "string", "dict": None, "access": "rw", "base64": True, "code": None},

    # ---------------------------------------------------------
    # Manual Regeneration / Last Regeneration:
    # ---------------------------------------------------------
    #id=943&show=D_B_1|D_Y_4_1|D_Y_4_2|D_Y_4_3|D_Y_4_4|D_Y_4_5|D_Y_4_6|D_Y_4_7|D_Y_4_8|D_Y_4_9|D_Y_4_10|D_Y_4_11|D_Y_4_12|D_Y_4_13|D_Y_4_14~
    "D_B_1": {"name": "Start Manual Generation", "unit": None, "type": "string", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": None},
    "D_Y_4_1": {"name": "Latest Regeneration", "unit": None, "type": "string", "dict": None, "access": "r", "base64": True, "code": None},
    #theres 13 more generations kept in the unit, but not exposed as is..  D_Y_4_1..D_Y_4_14

    # ---------------------------------------------------------
    # Water Consumption:
    # ---------------------------------------------------------
    #id=943&show=D_Y_2_1|D_Y_2_2|D_Y_2_3|D_Y_2_4|D_Y_2_5|D_Y_2_6|D_Y_2_7|D_Y_2_8|D_Y_2_9|D_Y_2_10|D_Y_2_11|D_Y_2_12|D_Y_2_13|D_Y_2_14|D_Y_2_15|D_Y_2_16|D_Y_2_17|D_Y_2_18|D_Y_2_19|D_Y_2_20|D_Y_2_21|D_Y_2_22|D_Y_2_23|D_Y_2_24|D_Y_2_25|D_Y_2_26|D_Y_2_27~
    "D_Y_2_1": {"name": "Daily Water Consumption - Yesterday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    #theres 26 more Water Consumptionm Records Kept in the unit, but not exposed as is..  D_Y_2_1..D_Y_2_27
 
    # ---------------------------------------------------------
    # Salt Consumption:
    # ---------------------------------------------------------
    #id=943&show=D_Y_3_1|D_Y_3_2|D_Y_3_3|D_Y_3_4|D_Y_3_5|D_Y_3_6|D_Y_3_7|D_Y_3_8|D_Y_3_9|D_Y_3_10|D_Y_3_11|D_Y_3_12|D_Y_3_13|D_Y_3_14|D_Y_3~
    "D_Y_3_1": {"name": "Daily Salt Consumption - Yesterday", "unit": "g", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    #theres 13 more Salt Consumptionm Records Kept in the unit, but not exposed as is..  D_Y_3_1..D_Y_3_14
    "D_Y_3": {"name": "Salt Consumption/year", "unit": "kg", "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
    #{'data': {'code': 'ok', 'D_Y_3_1': '173', 'D_Y_3': '160'}}

    # ---------------------------------------------------------
    # System Parameters:
    # ---------------------------------------------------------
    #id=943&show=D_C_1_1|D_C_4_2|D_C_5_2|D_C_5_3|D_C_6_1|D_C_8_1|D_C_8_2|D_D_1|D_D_2|D_E_1|D_Y_9|D_Y_9_8|D_Y_9_24|D_C_7_1|D_Y_15~
 #   "D_C_1_1": {"name": "Operating Language", "unit": None, "type": "String", "dict": {"0": "Deutsch", "1": "English", "2": "Français", "3": "Italiano", "4": "Nederlands", "5": "Испанский", "6": "Español", "7": "中文"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_4_2": {"name": "Unit Time", "unit": "time", "type": "string", "dict": None, "access": "rw", "base64": False, "code": None},
 #   "D_C_5_2": {"name": "Unit Date", "unit": "date", "type": "string", "dict": None, "access": "rw", "base64": False, "code": None},
 #   "D_C_5_3": {"name": "Automatic Switching Daylight Saving", "unit": None, "type": "String", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_6_1": {"name": "Display In Standby Active", "unit": None, "type": "string", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_8_1": {"name": "Illuminated Ring Function", "unit": None, "type": "String", "dict": {"0": "deactivated", "1": "in case of fault", "2": "in case of operation, fault", "3": "in case of water treatment, operation, fault", "4": "constantly illuminated"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_8_2": {"name": "Ring Light Flash on Salt Advance Warning", "unit": None, "type": "String", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": None},
 #   "D_D_1": {"name": "Raw water hardness", "unit": "°dH", "type": "number", "dict": None, "access": "rw", "base64": False, "code": None},
 #   "D_D_2": {"name": "Target Soft water hardness", "unit": "°dH", "type": "number", "dict": None, "access": "rw", "base64": False, "code": None},
 #   "D_E_1": {"name": "Begin Startup Process", "unit": None, "type": "String", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": None},
 #   "D_Y_9": {"name": "Startup Current Index Comission Program", "unit": None, "type": "number", "dict": None, "access": "r", "base64": False, "code": None},
 #   "D_Y_9_8": {"name": "Startup Countdown Time Venting Program", "unit": "hours", "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
 #   "D_Y_9_24": {"name": "Startup Remaining Duration of Test Generation", "unit": "hours", "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
 #   "D_C_7_1": {"name": "Set Service Interval", "unit": "dayn", "type": "number", "dict": None, "access": "rw", "base64": False, "code": None},
 #   "D_Y_15": {"name": "Hardware ID", "unit": None, "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
    #{'data': {'code': 'ok', 'D_C_1_1': '1', 'D_C_4_2': '19:14', 'D_C_5_2': '18.02.2026', 'D_C_5_3': '1', 'D_C_6_1': '0', 'D_C_8_1': '3', 'D_C_8_2': '0', 'D_D_1': '16.0', 'D_D_2': '4.0', 'D_E_1': '0', 'D_Y_9': '24', 'D_Y_9_8': '00:00', 'D_Y_9_24': '00:00', 'D_C_7_1': '368', 'D_Y_15': '0xaaaaaaaa'}}

    # ---------------------------------------------------------
    # Regeneration:
    # ---------------------------------------------------------
    #id=943&show=D_C_4_1|D_C_4_3|D_C_4_4|D_C_4_5|D_Y_14|D_C_5_1|D_C_6_3|D_C_6_4|D_C_6_5|D_C_6_6|D_C_6_7|D_C_6_8|D_C_6_9~
 #   "D_C_4_1": {"name": "Regeneration Time", "unit": None, "type": "String", "dict": {"0": "Automatic", "1": "Fixed", "2": "Weekly Timer"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_4_3": {"name": "Daily Generation Time 1", "unit": "time", "type": "string", "dict": None, "access": "rw", "base64": False, "code": None},
 #   "D_C_4_4": {"name": "Daily Generation Time 2", "unit": "time", "type": "string", "dict": None, "access": "rw", "base64": False, "code": None},
 #   "D_C_4_5": {"name": "Daily Generation Time 3", "unit": "time", "type": "string", "dict": None, "access": "rw", "base64": False, "code": None},
    "D_Y_14": {"name": "Estimated Time of Next Regeneration", "unit": "date-time", "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
 #   "D_C_5_1": {"name": "Function", "unit": None, "type": "String", "dict": {"0": "Eco Mode", "1": "Power Mode", "2": "Comfort Mode", "3": "Individual"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_6_3": {"name": "Timer Function - Monday", "unit": None, "type": "String", "dict": {"0": "Eco Mode", "1": "Power Mode", "2": "Comfort Mode"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_6_4": {"name": "Timer Function - Tuesday", "unit": None, "type": "String", "dict": {"0": "Eco Mode", "1": "Power Mode", "2": "Comfort Mode"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_6_5": {"name": "Timer Function - Wendesday", "unit": None, "type": "String", "dict": {"0": "Eco Mode", "1": "Power Mode", "2": "Comfort Mode"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_6_6": {"name": "Timer Function - Thusrday", "unit": None, "type": "String", "dict": {"0": "Eco Mode", "1": "Power Mode", "2": "Comfort Mode"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_6_7": {"name": "Timer Function - Friday", "unit": None, "type": "String", "dict": {"0": "Eco Mode", "1": "Power Mode", "2": "Comfort Mode"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_6_8": {"name": "Timer Function - Saturdayy", "unit": None, "type": "String", "dict": {"0": "Eco Mode", "1": "Power Mode", "2": "Comfort Mode"}, "access": "rw", "base64": False, "code": None},
 #   "D_C_6_9": {"name": "Timer Function - Sunday", "unit": None, "type": "String", "dict": {"0": "Eco Mode", "1": "Power Mode", "2": "Comfort Mode"}, "access": "rw", "base64": False, "code": None},
    #{'data': {'code': 'ok', 'D_C_4_1': '0', 'D_C_4_3': '02:00', 'D_C_4_4': '10:00', 'D_C_4_5': '18:00', 'D_Y_14': '19.02.2026 00:15Uhr', 'D_C_5_1': '2', 'D_C_6_3': '2', 'D_C_6_4': '0', 'D_C_6_5': '0', 'D_C_6_6': '0', 'D_C_6_7': '2', 'D_C_6_8': '1', 'D_C_6_9': '1'}}

    # ---------------------------------------------------------
    # Wi-fi Configuration:
    # ---------------------------------------------------------
    #id=943&show=D_C_3_7_1|D_C_3_7_2|D_C_3_7_3|D_C_3_1|D_Y_8_1_1|D_Y_8_1_2|D_Y_8_1_3|D_Y_8_2|D_Y_8_3|D_Y_8_4|D_Y_8_5|D_Y_8_6|D_Y_8_7|D_Y_8_8|D_Y_8_10|D_Y_8_11|D_Y_8_12|D_Y_12~
    #This secrtion has lots of params that are not exposed, they are listed but commented out for now. the dict entries are not tested for now
 #   "D_C_3_7_1": {"name": "AP IP Address", "unit": None, "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
 #   "D_C_3_7_2": {"name": "AP SSID", "unit": None, "type": "string", "dict": None, "access": "r", "base64": False, "code": None},
 #   "D_C_3_7_3": {"name": "AP Status", "unit": None, "type": "String", "dict": {"0": "Not Connected", "1": "Connected"}, "access": "r", "base64": False, "code": None},
 #   "D_C_3_1": {"name": "WLAN IP Address", "unit": None, "type": "string", "dict": None, "access": "r", "base64": True, "code": None},
 #   "D_Y_8_1_1": {"name": "WLAN Default Gateway", "unit": None, "type": "string", "dict": None, "access": "r", "base64": True, "code": None},
 #   "D_Y_8_1_2": {"name": "WLAN Primary DNS", "unit": None, "type": "string", "dict": None, "access": "r", "base64": True, "code": None},
 #   "D_Y_8_1_3": {"name": "WLAN Secondary DNS", "unit": None, "type": "string", "dict": None, "access": "r", "base64": True, "code": None},
 #   "D_Y_8_2": {"name": "WLAN Status ", "unit": None, "type": "String", "dict": {"0": "Not Connected", "1": "Connected"}, "access": "r", "base64": False, "code": None},
    #"D_Y_8_3": {"name": "Deactivate WLAN", "unit": None, "type": "String", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": None},
    #"D_Y_8_4": {"name": "Search WLAN", "unit": None, "type": "String", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": None},
 #   "D_Y_8_5": {"name": "Active Network", "unit": None, "type": "string", "dict": None, "access": "r", "base64": True, "code": None},
 #   "D_Y_8_6": {"name": "Email Address 1 for Forwarding", "unit": None, "type": "string", "dict": None, "access": "rw", "base64": True, "code": None},
 #   "D_Y_8_7": {"name": "Email Address 2 for Forwarding", "unit": None, "type": "string", "dict": None, "access": "rw", "base64": True, "code": None},
 #   "D_Y_8_8": {"name": "Email Address 3 for Forwarding", "unit": None, "type": "string", "dict": None, "access": "rw", "base64": True, "code": None},
 #   "D_Y_8_10": {"name": "SMTP Server", "unit": None, "type": "string", "dict": None, "access": "rw", "base64": True, "code": None},
 #   "D_Y_8_11": {"name": "SMTP Server Port", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": None},
 #   "D_Y_12": {"name": "SMTP Password", "unit": None, "type": "secret", "dict": None, "access": "rw", "base64": True, "code": None},
    "D_Y_8_12": {"name": "Last Testmail Sent", "unit": "date-time", "type": "string", "dict": None, "access": "rw", "base64": False, "code": None},
    #Theres something wrong in this screen, there should be smtp username, sender email, phone number, surname, test email send button test email status transmission, time of last test send and a network reset param
    #{'data': {'code': 'ok', 'D_C_3_7_1': '192.168.0.1/24', 'D_C_3_7_2': 'softliQ:MC_cfddc7', 'D_C_3_7_3': '1', 'D_C_3_1': '1', 'D_Y_8_1_1': 'aGVucmlrQG9obWVyaWtzZW4uZGs=', 'D_Y_8_1_2': '-', 'D_Y_8_1_3': '-', 'D_Y_8_2': 'cmF6b3Iub2htZWdhc3Rhci5kaw==', 'D_Y_8_5': 'KioqKioqKioqKio=', 'D_Y_8_6': 'c29mdGxpcUBvaG1lZ2FzdGFyLmRr', 'D_Y_8_7': '-', 'D_Y_8_8': '-', 'D_Y_8_10': '0', 'D_Y_8_11': '0', 'D_Y_8_12': '01.01.2018 00:00', 'D_Y_12': '0'}}

    # ---------------------------------------------------------
    # Code Protected Area
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # System Data Record: code 290
    # ---------------------------------------------------------
    #id=943&code=290&show=D_F_6~
    #This is actiually RW, but set to R
    "D_F_6": {"name": "System Type", "unit": None, "type": "String", "dict": {"0": "Free twin system", "1": "softliQ:MC32", "2": "softliQ:MC38"}, "access": "r", "base64": False, "code": "290"},

    # ---------------------------------------------------------
    # Installer Level: code 005
    # ---------------------------------------------------------
    #id=943&code=005&show=D_F_1|D_F_3_1|D_F_3_2|D_F_3_3|D_F_3_4|D_F_3_5|D_F_3_6|D_F_3_7|D_F_4_1|D_F_4_2|D_F_4_3|D_F_4_4|D_F_4_5|D_F_4_6|D_F_4_7|D_F_5_1|D_F_5_2|D_F_5_3|D_F_5_4|D_F_5_5|D_F_5_6|D_F_5_7|D_F_7|D_F_8|D_F_9|D_G_5|D_K_18|D_K_19|D_K_20|D_K_21|D_K_3|D_K_4|D_K_14|D_K_15|D_K_16|D_K_17|D_F_10|D_F_11~
 #   "D_F_1": {"name": "Select Regeneration Time", "unit": None, "type": "String", "dict": {"0": "Automatic", "1": "Fixed", "2": "Weekly Timer"}, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_3_1": {"name": "Weekly Timer 1 Monday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_3_2": {"name": "Weekly Timer 1 Tuesday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_3_3": {"name": "Weekly Timer 1 Wendesday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_3_4": {"name": "Weekly Timer 1 Thursday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_3_5": {"name": "Weekly Timer 1 Friday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_3_6": {"name": "Weekly Timer 1 Saturday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_3_7": {"name": "Weekly Timer 1 Sunday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_4_1": {"name": "Weekly Timer 2 Monday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_4_2": {"name": "Weekly Timer 2 Tuesday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_4_3": {"name": "Weekly Timer 2 Wendesday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_4_4": {"name": "Weekly Timer 2 Thursday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_4_5": {"name": "Weekly Timer 2 Friday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_4_6": {"name": "Weekly Timer 2 Saturday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_4_7": {"name": "Weekly Timer 2 Sunday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_5_1": {"name": "Weekly Timer 3 Monday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_5_2": {"name": "Weekly Timer 3 Tuesday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_5_3": {"name": "Weekly Timer 3 Wendesday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_5_4": {"name": "Weekly Timer 3 Thursday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_5_5": {"name": "Weekly Timer 3 Friday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_5_6": {"name": "Weekly Timer 3 Saturday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_5_7": {"name": "Weekly Timer 3 Sunday", "unit": "time", "type": "String", "dict": None, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_7": {"name": "Start Test Regeneration", "unit": None, "type": "String", "dict": {"0": "No", "1": "Only Exchanger Tank 1", "2": "Only Exchanger Tank 2", "3": "Both Exchanger Tanks"}, "access": "rw", "base64": False, "code": "005"},
    #"D_F_8": {"name": "Find Reference Position Exchange Tank 1", "unit": None, "type": "string", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": "005"},
    #"D_F_9": {"name": "Find Reference Position Exchange Tank 1", "unit": None, "type": "string", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": "005"},
 #   "D_G_5": {"name": "Fill Brine Tank Operating Vater Volume", "unit": None, "type": "string", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": "005"},
    "D_K_18": {"name": "Soft Water Volume Exchanger 1", "unit": "m3", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_19": {"name": "Soft Water Volume Exchanger 2", "unit": "m3", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_20": {"name": "Raw Water Volume Blending", "unit": "m3", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_21": {"name": "Make-up Water Volume", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_3": {"name": "Flow Rate Peak Value Parallel Operation", "unit": "m3/h", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_4": {"name": "Time Counter Nominal Flow Exceeded Parallel Operation", "unit": "Min", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_14": {"name": "Flow Rate Peak Value Exchanger 1", "unit": "m3/h", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_15": {"name": "Time Counter Nominal Flow Exceeded Exchanger 1", "unit": "Min", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_16": {"name": "Flow Rate Peak Value Exchanger 2", "unit": "m3/h", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
    "D_K_17": {"name": "Time Counter Nominal Flow Exceeded Exchanger 2", "unit": "Min", "type": "number", "dict": None, "access": "r", "base64": False, "code": "005"},
 #   "D_F_10": {"name": "Soft Water Sample Tank 1", "unit": None, "type": "string", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": "005"},
 #   "D_F_11": {"name": "Soft Water Sample Tank 2", "unit": None, "type": "string", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": "005"},
    #{'data': {'code': 'ok', 'D_F_1': '0', 'D_F_3_1': '07:00', 'D_F_3_2': '07:00', 'D_F_3_3': '07:00', 'D_F_3_4': '07:00', 'D_F_3_5': '07:00', 'D_F_3_6': '--:--', 'D_F_3_7': '--:--', 'D_F_4_1': '07:00', 'D_F_4_2': '07:00', 'D_F_4_3': '07:00', 'D_F_4_4': '07:00', 'D_F_4_5': '07:00', 'D_F_4_6': '--:--', 'D_F_4_7': '--:--', 'D_F_5_1': '07:00', 'D_F_5_2': '07:00', 'D_F_5_3': '07:00', 'D_F_5_4': '07:00', 'D_F_5_5': '07:00', 'D_F_5_6': '--:--', 'D_F_5_7': '--:--', 'D_F_7': '0', 'D_G_5': '0', 'D_K_18': '1260', 'D_K_19': '1273', 'D_K_20': '571', 'D_K_21': '2826', 'D_K_3': '2.83', 'D_K_4': '0', 'D_K_14': '1.84', 'D_K_15': '9', 'D_K_16': '1.84', 'D_K_17': '6', 'D_F_10': '0', 'D_F_11': '0'}}

    # ---------------------------------------------------------
    # Programmable Input and Output: code 005
    # ---------------------------------------------------------
    #id=943&code=005&show=D_G_1|D_G_2|D_G_3|D_Y_8_9|D_G_4~
 #   "D_G_1": {"name": "Voltage-free Contact Function", "unit": None, "type": "String", "dict": {"0": "Reg.-message", "1": "Reg. water delivery pump", "2": "Release residual hardness monitoring", "3": "Forwarding of fault messages"}, "access": "rw", "base64": False, "code": "005"},
 #   "D_G_2": {"name": "Voltage-free Contact Function Mode", "unit": None, "type": "string", "dict": {"0": "N.C", "1": "N.O"}, "access": "rw", "base64": False, "code": "005"},
 #   "D_G_3": {"name": "Function Programmable Input", "unit": None, "type": "string", "dict": {"0": "Reg. Release", "1": "Reg. Lock", "2": "Forwarding of fault messages"}, "access": "rw", "base64": False, "code": "005"},
 #   "D_Y_8_9": {"name": "Text for Email Forrading of Fault Message", "unit": None, "type": "String", "dict": None, "access": "rw", "base64": True, "code": "005"},
 #   "D_G_4": {"name": "Modbus Connection", "unit": None, "type": "string", "dict": {"0": "Deactivated", "1": "Activated"}, "access": "rw", "base64": False, "code": "005"},
    #{'data': {'code': 'ok', 'D_G_1': '1', 'D_G_2': '0', 'D_G_3': '0', 'D_Y_8_9': '-', 'D_G_4': '0'}}

    # ---------------------------------------------------------
    # Control Parameters: code 142
    # ---------------------------------------------------------
    # id=943&code=XXX&show=D_H_2|D_H_3|D_H_4|D_H_5|D_H_6|D_H_7|D_H_8|D_H_9|D_H_11|D_H_12|D_H_13|D_H_15~
 #   "D_H_2": {"name": "Power Failure Reaction", "unit": None, "type": "String", "dict": {"0": "No reaction", "2": "Message text+fault alarm contact", "3": "Message text+fault alarm contact+regeneration"}, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_3": {"name": "System Overload Reaction", "unit": None, "type": "String", "dict": {"0": "No reaction", "2": "Message text+fault alarm contact"}, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_4": {"name": "Disinfection Monitoring", "unit": None, "type": "string", "dict": {"0": "Deactivated", "1": "Activated"}, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_5": {"name": "Chlorine Cell", "unit": None, "type": "string", "dict": {"0": "Deactivated", "1": "Activated"}, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_6": {"name": "Regeneration Water Meter Monitoring Time", "unit": "Min", "type": "number", "dict": None, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_7": {"name": "Salting Monitoring Time", "unit": "Min", "type": "number", "dict": None, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_8": {"name": "Daily Interval for Compulsory Regeneration", "unit": "Days", "type": "number", "dict": None, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_9": {"name": "Nominal Flow Monitoring", "unit": None, "type": "string", "dict": {"0": "Deactivated", "1": "Activated"}, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_11": {"name": "Residual Capacity Limit Value", "unit": "%", "type": "number", "dict": None, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_12": {"name": "Monitoring Blending", "unit": None, "type": "String", "dict": {"0": "No Message, No reaction", "1": "Message text+fault alarm contact"}, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_13": {"name": "Brightness Led Strip", "unit": "%", "type": "number", "dict": None, "access": "rw", "base64": False, "code": "142"},
 #   "D_H_14": {"name": "Monitoring Water Loss and Flow Direction", "unit": None, "type": "string", "dict": {"0": "Deactivated", "1": "Activated"}, "access": "rw", "base64": False, "code": "142"},

    # ---------------------------------------------------------
    # Hydraulic Values: code 121
    # ---------------------------------------------------------
    #id=943&code=121&show=D_I_1|D_I_2|D_I_4|D_I_5|D_I_6|D_I_7|D_I_8|D_I_9|D_I_10|D_I_11|D_I_12|D_I_15|D_I_16|D_I_17|D_I_19|D_I_18|D_I_20~
    #Not Implemented, looks dangerous to change without knowledge

    # ---------------------------------------------------------
    # Step Intervals: code 302
    # ---------------------------------------------------------
    #id=943&code=302&show=D_J_1|D_J_3|D_J_4|D_J_5|D_J_6|D_J_7|D_J_8|D_J_9~
 #   "D_J_1": {"name": "Steps reference point - washing out", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": "302"},
 #   "D_J_3": {"name": "Steps washing out - operation", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": "302"},
 #   "D_J_4": {"name": "Steps operation - fill brine tank", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": "302"},
 #   "D_J_5": {"name": "Steps fill brine tank - salting", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": "302"},
 #   "D_J_6": {"name": "Steps salting - purging", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": "302"},
 #   "D_J_7": {"name": "Steps purging - backwashing", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": "302"},
 #   "D_J_8": {"name": "Steps backwashing - reverse position", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": "302"},
 #   "D_J_9": {"name": "Steps reference point searcht", "unit": None, "type": "number", "dict": None, "access": "rw", "base64": False, "code": "302"},

    # ---------------------------------------------------------
    # Counter Readings: code 245
    # ---------------------------------------------------------
    #id=943&code=245&show=D_K_5|D_K_6|D_K_7|D_K_8_1|D_K_8_2|D_K_8_3|D_K_8_4|D_K_8_5|D_K_8_6|D_K_8_7|D_K_9_1|D_K_9_2|D_K_9_3|D_K_9_4|D_K_9_5|D_K_9_6|D_K_9_7~
    "D_K_5": {"name": "Chlorine Current", "unit": "mAh", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_6": {"name": "Steps Display Exhanger Tank 1", "unit": None, "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_7": {"name": "Steps Display Exhanger Tank 2", "unit": None, "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_8_1": {"name": "Average consumption - Monday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_8_2": {"name": "Average consumption - Tuesday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_8_3": {"name": "Average consumption - Wendesday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_8_4": {"name": "Average consumption - Thursday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_8_5": {"name": "Average consumption - Friday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_8_6": {"name": "Average consumption - Saturday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_8_7": {"name": "Average consumption - Sunday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_9_1": {"name": "Standart Deviation - Monday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_9_2": {"name": "Standart Deviation - Tuesday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_9_3": {"name": "Standart Deviation - Wendesday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_9_4": {"name": "Standart Deviation - Thursday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_9_5": {"name": "Standart Deviation - Friday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_9_6": {"name": "Standart Deviation - Saturday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},
    "D_K_9_7": {"name": "Standart Deviation - Sunday", "unit": "l", "type": "number", "dict": None, "access": "r", "base64": False, "code": "245"},

    # ---------------------------------------------------------
    # Error Memory & Change History: code 005
    # ---------------------------------------------------------
    #id=943&code=005&show=D_K_10_1|D_K_10_2|D_K_10_3|D_K_10_4|D_K_10_5|D_K_10_6|D_K_10_7|D_K_10_8|D_K_10_9|D_K_10_10|D_K_10_11|D_K_10_12|D_K_10_13|D_K_10_14|D_K_10_15|D_K_10_16|D_K_13|D_B_2|D_K_11_1|D_K_11_2|D_K_11_3|D_K_11_4|D_K_11_5|D_K_11_6|D_K_11_7|D_K_11_8|D_K_11_9|D_K_11_10|D_K_11_11|D_K_11_12|D_K_11_13|D_K_11_14|D_K_11_15|D_K_11_16~
    "D_K_10_1": {"name": "Error Memory 1 (Last Error)", "unit": None, "type": "string", "dict": None, "access": "r", "base64": False, "code": "005"},
    #There are 16 Memories for Error D_K_10_1..D_K_10_16
    "D_K_13": {"name": "Error Memory Deleted On", "unit": "date-time", "type": "string", "dict": None, "access": "r", "base64": False, "code": "005"},
 #   "D_B_2": {"name": "Reset Pending Error", "unit": None, "type": "string", "dict": {"0": "No", "1": "Yes"}, "access": "rw", "base64": False, "code": "005"},
    "D_K_11_1": {"name": "Last Change", "unit": None, "type": "string", "dict": None, "access": "r", "base64": False, "code": "005"},
    #There are 16 Memories for Changes D_K_11_1..D_K_11_16






        # Reset Error Memory: code
        #id=943&code=XXX&show=D_M_3_3~
    #Units:
    #Seems to be UI Setting nothing really happens in the gruenbech.js javascript here.







}