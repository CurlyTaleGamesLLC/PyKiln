import os
import subprocess
import sys
import glob
import time
import webbrowser
from setup_utils import *

cls()

printMessage("PyKiln ESP32 Micropython Installation:")
print("Please make sure your ESP32 is unplugged from your computer.")
print()
print("press enter...")
input()
cls()

printMessage("Installing Required Python Packages:")
install("esptool")
install("micropy-cli")
install("rshell")
print()
cls()


serialPortsBefore = list_serial_options(True)
serialDevicesBefore = list_serial_options(False) 

printMessage("Scanning for ESP32:")
print("Please plug in your ESP32 into your computer and wait a few seconds for it to be recognized.")
print()
print("press enter...")
input()
cls()

serialPortsAfter = list_serial_options(True)
serialDevicesAfter = list_serial_options(False)
serialPortsDetected = Diff(serialPortsAfter, serialPortsBefore)
serialDevicesDetected = Diff(serialDevicesAfter, serialDevicesBefore)

printMessage("Detected Device:")
if len(serialPortsDetected) == 0:
    print("No serial device detected")
    print("Please unplug your ESP32 from your computer and run this script again")
    print()
    exit()

print("SELECTED: " + serialDevicesDetected[0])
print()
print("HOLD DOWN THE 'BOOT' button on the ESP32") 
print("you can stop holding it down after it starts erasing the chip")
print()
print("press enter to install MicroPython...")
input()
cls()

printMessage("Erasing ESP32 on " + serialPortsDetected[0])
print("If it's not connecting, make sure to hold down the 'BOOT' button on the ESP32")
print()

os.system("esptool.py --chip esp32 --port " + serialPortsDetected[0] + " erase_flash")
print()
    
printMessage("Flashing Micropython to ESP32")
os.system("esptool.py --chip esp32 --port " + serialPortsDetected[0] + " --baud 460800 write_flash -z 0x1000 esp32-idf3-20200902-v1.13.bin")
print()

cls()
printMessage("Enter your WiFi Network Name")
ssid = input("WiFi Name: ")

cls()
printMessage("Enter your WiFi Network Password")
password = input("WiFi Password: ")

cls()
printMessage("Local Host")
print("Enter the URL for your self hosted web server")
print("If you don't know that this is, leave it blank and press enter")
print()
host = input("Host URL: ")

writeWifiJSON(ssid, password, host)

cls()

printMessage("Connecting and Installing PyKiln to ESP32")
print("It will take a few minutes to copy all the files")
print()

os.system("rshell -p " + serialPortsDetected[0] + " rsync src/ /pyboard/ ; exit")
os.system("rshell -p " + serialPortsDetected[0] + " repl ~ import reset ~ ; exit")

cls()

printMessage("Getting IP Address")
# copy the ip address txt file off of the PyKiln and put it in the current folder, 
# then read that txt file and print it, then delete the file
dirPath = os.getcwd()
filePath = os.path.join(dirPath, 'ip.txt')

# convert path to forward slashes and remove the drive letter for REPL
filePathREPL = filePath.replace('\\', '/')
if os.name == 'nt':
    filePathREPL = filePathREPL.replace('C:', '')

copyCommand = "cp /pyboard/ip.txt " + filePathREPL
os.system("rshell -p " + "COM3" + " " + copyCommand + " ; exit")
os.system("rshell -p " + serialPortsDetected[0] + " repl ~ import reset ~ ; exit")

loading("Rebooting", 10)

cls()

printMessage("Set up Complete!")

print("Opening Web Browser, Remeber this URL to access PyKiln:")
ip = open("ip.txt", "r")
ipURL = "http://" + ip.read()
print("IP = " + ipURL)

if sys.platform == 'darwin':    # in case of OS X
    subprocess.Popen(['open', ipURL])
else:
    webbrowser.open(ipURL, new=0, autoraise=True)

print()
print("close this window or press enter to quit...")
input()
