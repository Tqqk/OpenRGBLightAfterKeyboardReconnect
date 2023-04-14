import subprocess
import time

# Path to the defcon file (you can download it at microsoft's website) - replace the "C:/PATH_TO_DEVCON/devcon.exe" with your own path to the devcon.exe
devcon_path = r"C:/PATH_TO_DEVCON/devcon.exe"

# Device ID of your keyboard, can be found in device manager -> KEYBOARDS -> disconnect your keyboard to find out which keyboard dissapears and which doesn't -> click on the keyboard that dissapeared when disconnected -> click on DETAILS -> find HARDWARE IDS in the dropdown menu -> copy the top one (if it doesn't work try the others) - replace "KEYBOARD_ID" with your own keyboard ID
keyboard_id = "KEYBOARD_ID"

# Initial state of keyboard
keyboard_connected = True

# Create startupinfo object
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

while True:
    devcon_find_cmd = [devcon_path, 'status', keyboard_id]

    try:
        output = subprocess.check_output(devcon_find_cmd, universal_newlines=True, startupinfo=startupinfo)
        if "No matching devices found" in output:
            if keyboard_connected:
                
                keyboard_connected = False
        else:
            if not keyboard_connected:
                
                keyboard_connected = True
                
                # Kill the OpenRGB task
                subprocess.run('taskkill /IM OpenRGB.exe /F', startupinfo=startupinfo)

                # Start the OpenRGB program with the desired attributes - replace the "C:\\PATH_TO_OPENRGB\\OpenRGB.exe" with you own OpenRGB.exe path and replace the "RGB_PROFILE_NAME" to the name of your profile in OpenRGB.

                process = subprocess.Popen(['C:\\PATH_TO_OPENRGB\\OpenRGB.exe', '--startminimized', '--profile', 'RGB_PROFILE_NAME'], stderr=subprocess.PIPE, startupinfo=startupinfo)

    except subprocess.CalledProcessError as e:
        print("Error running devcon:", e)

    time.sleep(1)
