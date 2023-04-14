# OpenRGB Light After Keyboard Reconnect
By default OpenRGB doesn't automatically rescan after you reconnect your keyboard. So when you have a keyboard which doesn't have a memory for the RGB profile, then if you reconnect your keyboard (for me it's disconecting my laptop from docking station and connecting it after few hours), the OpenRGB software doesn't detect the reconnect and you need to open OpenRGB, click on rescan and then load profile. That's why I've made this python script restarts the OpenRGB software (https://openrgb.org) when you reconnect your keyboard.

<br/>


## How to modify the script
1. Replace the `C:/PATH_TO_DEVCON/devcon.exe` (line 5) with your own path to the devcon.exe file
    - You will need the **devcon.exe**. It's included in WDK and you can download it at microsoft's website (https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon) 
  

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
  
3. Replace the `C:\\PATH_TO_OPENRGB\\OpenRGB.exe` (line 37) with our own path to the OpenRGB software


<br/>

4. Replace the `RGB_PROFILE_NAME` (line 37) with our own profile name in the OpenRGB software

<br/>
<br/>

## How to run the script/program
A. You can run the script using python 
  - Use the command `python PROGRAM_NAME.py` to run the program

<br/>

B. You can run the script/program by creating .exe file
  - Download or copy the python script
  - Use the command `pyinstaller -w --onefile --noconsole PROGRAM_NAME.py` to create the .exe file (Don't forget to use the `-w --onefile --noconsole` attributes to run the program without any console window)


<br/>
<br/>

## How to make the script/program run on startup
1. Create a shortcut of the .exe program
2. Press **Windows key + R**, and type `shell:startup`
3. Copy and paste the shortcut for the .exe to the startup folder

<br/>
<br/>

## How to stop the script/program from running
1. Open Task Manager
2. Find the .exe and click on End Task
3. If you have it in the Startup folder, then remove it









