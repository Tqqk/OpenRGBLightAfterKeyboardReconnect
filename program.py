import subprocess
import time
import psutil

# Set the devcon path to "devcon.exe" in the same folder
devcon_path = "devcon.exe"

# Device classes for keyboards and mice
keyboard_class = "HIDClass"
mouse_class = "Mouse"

# Path to OpenRGB executable and profile name in the same folder
openrgb_path = "OpenRGB.exe"  # Use just the executable name
profile_name = "color"

# Create startupinfo object
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

def count_hid_devices(device_class):
    try:
        output = subprocess.check_output([devcon_path, 'find', '='+device_class], universal_newlines=True, startupinfo=startupinfo)
        # Count the number of lines (each line corresponds to a device)
        device_count = len(output.split('\n'))
        return device_count
    except subprocess.CalledProcessError as e:
        print("Error running devcon:", e)
        return 0

def start_openrgb():
    # Check if OpenRGB is already running
    for proc in psutil.process_iter(['pid', 'name']):
        if 'OpenRGB.exe' in proc.info['name']:
            print('Killing OpenRGB...')
            proc.kill()

    # Start OpenRGB
    print('Starting OpenRGB...')
    subprocess.Popen([openrgb_path, '--startminimized', '--profile', profile_name], stderr=subprocess.PIPE, startupinfo=startupinfo)

# Initial state of device counts
prev_hid_device_count = count_hid_devices(keyboard_class) + count_hid_devices(mouse_class)

while True:
    # Check current HID device counts
    current_hid_device_count = count_hid_devices(keyboard_class) + count_hid_devices(mouse_class)

    # Print device count for debugging
    print("Current HID device count:", current_hid_device_count)

    # Check for HID device count change
    if current_hid_device_count != prev_hid_device_count:
        # Perform actions when the HID device count changes
        print("HID device count changed. Restarting OpenRGB.")
        start_openrgb()  # Restart OpenRGB when the HID device count changes

    prev_hid_device_count = current_hid_device_count
    time.sleep(1)
