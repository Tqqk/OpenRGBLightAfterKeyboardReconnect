# OpenRGB Light After Keyboard Reconnect
By default OpenRGB doesn't automatically rescan after you reconnect your keyboard. So when you have a keyboard which doesn't have a memory for the RGB profile, then if you reconnect your keyboard (for me it's disconecting my laptop from docking station and connecting it after few hours), the OpenRGB software doesn't detect the reconnect and you need to open OpenRGB, click on rescan and then load profile. That's why I've made this python script restarts the OpenRGB software (https://openrgb.org) when you reconnect your keyboard.

<br/>


## How to modify the script
1. - You will need to obtain the **devcon.exe** 
(It's included in WDK and you can download it at Microsoft's website https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon) 
   - After you've downloaded the WDK, copy the **devcon.exe** to the same folder as the **OpenRGB.exe** file. (root folder of OpenRGB)
  
<br/>

2. Replace the `PROFILE_NAME` (line 4) with our own profile name in the OpenRGB software

<br/>
<br/>

## How to run the script/program
A. You can run the script using python 
  - Use the command `python program.py` to run the program, but that's going to run with a command line open, so that's not ideal (I recommend the option **B.**)

<br/>

B. You can run the script/program by creating .exe file
  - Download or copy the python script
  - Use the command `pyinstaller -w --onefile --noconsole program.py` to create the .exe file (Don't forget to use the `-w --onefile --noconsole` attributes to run the program without any console window)


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

<br/>
<br/>

####  v2.2







