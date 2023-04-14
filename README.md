# OpenRGBLightAfterKeyboardReconnect
This python script restarts the OpenRGB software (https://openrgb.org) when you reconnect your keyboard.

## How to use the script
1. Replace the `C:/PATH_TO_DEVCON/devcon.exe` (line 5) with your own path to the devcon.exe file
    - You will need the **devcon.exe**. It's included in WDK and you can download it at microsoft's website (https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon) 
  
<br/>
<br/>

2. Replace the `KEYBOARD_ID` (line 8) with your own keyboard ID 
    - You will need to get the **Hardware ID** of your keyboard 
      - Open **Device Manager**
      - Click on **Keyboards**
      - Find your keyboard (There may be more of them. It's the one that dissapears when you disconnect your keyboard)
      - Right-click the device and select **Properties**
      - Select the **Details** tab
      - In the **Property** dropdown menu select **Hardware Ids**
      - Choose the ID at the top (If it doesn't work try the other IDs)
    
 <br/>
 <br/>
  
3. Replace the `C:\\PATH_TO_OPENRGB\\OpenRGB.exe` (line 37) with our own path to the OpenRGB software

<br/>
<br/>

4. Replace the `RGB_PROFILE_NAME` (line 37) with our own profile name in the OpenRGB software

## How to run the script
A. You can run the script using python 
  - Use the command `python PROGRAM_NAME.py` to run the program
<br/>
<br/>

B. You can run the script by creating .exe file
  - Use the command `pyinstaller -w --onefile --noconsole PROGRAM_NAME.py` to create the .exe file






