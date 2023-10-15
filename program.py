import subprocess
import time

profile_name = "PROFILE_NAME"

# Variables
openrgb_path = "OpenRGB.exe"  
devcon_path = "devcon.exe"
keyboard_class = "HIDClass"
mouse_class = "Mouse"

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

def count_hid_devices(device_class):
    try:
        # Devices counted by devcon
        process = subprocess.Popen([devcon_path, 'find', '='+device_class], stdout=subprocess.PIPE, universal_newlines=True, startupinfo=startupinfo)
        device_count = sum(1 for _ in process.stdout) 
        process.stdout.close()
        return device_count
    except subprocess.CalledProcessError as e:
        print("Error running devcon:", e)
        return 0

def start_openrgb():
    # Restart OpenRGB
    subprocess.run(['taskkill', '/IM', openrgb_path, '/F'], startupinfo=startupinfo)

    print('Starting OpenRGB...')
    subprocess.Popen([openrgb_path, '--startminimized', '--profile', profile_name], stderr=subprocess.PIPE, startupinfo=startupinfo)

# Device counts
prev_hid_device_count = count_hid_devices(keyboard_class) + count_hid_devices(mouse_class)

while True:
    # HID device counts
    current_hid_device_count = count_hid_devices(keyboard_class) + count_hid_devices(mouse_class)

    # Debug
    print("Current HID device count:", current_hid_device_count)

    # HID device count change
    if current_hid_device_count != prev_hid_device_count:
        
        print("HID device count changed. Restarting OpenRGB.")
        start_openrgb()  

    prev_hid_device_count = current_hid_device_count
    time.sleep(2)