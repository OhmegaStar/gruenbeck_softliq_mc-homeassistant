import asyncio
from gruenbeck_mc import GruenbeckMC

async def main():
    client = GruenbeckMC("192.168.0.195")

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

#    print("Reading System Data Record (D_J_1)...")
#    print(await client.get_param("D_F_6", code="290"))


 #   print("Reading System Data Record (D_K_5)...")
 #   for i in range(141,1000):
 #       code = f"{i:03d}"  # formats 0 → "000", 5 → "005", etc.
 #       response = await client.get_param("D_K_5", code=code)
 #       # Defensive check: ensure response is a dict and contains the expected structure
 #       if isinstance(response, dict):
 #           data = response.get("data", {})
 #           if isinstance(data, dict) and data.get("code") == "ok":
 #               print(f"Valid code found: {code}")
 #               break
 #       print(f"Tried {code}, result: {response}")


    print("Reading Software Version (D_Y_6)...")
    print(await client.get_param("D_Y_6"))

    print("Reading soft water hardness target (D_D_2)...")
 #   print(await client.get_param("D_D_2"))

    print("Reading flow (D_A_1_7)...")
#    print(await client.get_param("D_A_1_7"))

    print("Reading exchanger info (requires code=005)...")
 #   print(await client.get_param("D_A_1_1", code="005"))

    print("Reading multiparams..1.")
#    print(await client.get_params(["D_H_2","D_H_3","D_H_4","D_H_5|D_H_6","|D_H_7|D_H_8|D_H_9|D_H_11|D_H_12|D_H_13|D_H_15], code="005"))

    PARAMETERS = {
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
    }

    ALL_PARAMS = list(PARAMETERS.keys())

    print("Reading multiparams..2.")
#    print(await client.get_params(ALL_PARAMS, code="005"))

    PARAMETERS = {
"D_G_1": {"name": "Voltage-free Contact Function", "unit": "enum", "type": "String", "dict": {"0": "Reg.-message", "1": "Reg. water delivery pump", "2": "Release residual hardness monitoring", "3": "Forwarding of fault messages"}, "access": "rw", "base64": False, "code": "005"},
    "D_G_2": {"name": "Voltage-free Contact Function Mode", "unit": None, "type": "string", "dict": {"0": "N.C", "1": "N.O"}, "access": "rw", "base64": False, "code": "005"},
    "D_G_3": {"name": "Function Programmable Input", "unit": None, "type": "string", "dict": {"0": "Reg. Release", "1": "Reg. Lock", "2": "Forwarding of fault messages"}, "access": "rw", "base64": False, "code": "005"},
    "D_Y_8_9": {"name": "Text for Email Forrading of Fault Message", "unit": None, "type": "String", "dict": None, "access": "rw", "base64": True, "code": "005"},
    "D_G_4": {"name": "Modbus Connection", "unit": None, "type": "string", "dict": {"0": "Deactivated", "1": "Activated"}, "access": "rw", "base64": False, "code": "005"},
  }

    ALL_PARAMS = list(PARAMETERS.keys())

    print("Reading multiparams..3.")
 #   print(await client.get_params(ALL_PARAMS, code="005"))


    await client.close()

asyncio.run(main())
