import os
import subprocess
import sys
import glob


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def printMessage(message):
    # print()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(message)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print()

def install(package):
    printMessage("Installing " + package)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print()

def list_serial_options(isPort):
	ports = serial.tools.list_ports.comports()
	available_ports = []
	available_names = []

	for p in ports:
		available_ports.append(p.device)
		available_names.append(str(p))	
	
	if isPort:
		return available_ports
	else:
		return available_names
	

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

import serial.tools.list_ports

print()
printMessage("Finished Installing Python Packages:")

print("press enter...")
input()
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
	
printMessage("Connecting and Installing PyKiln to ESP32")
print("It will take a few minutes to copy all the files")
print()
os.system("rshell -p " + serialPortsDetected[0] + " rsync src/ /pyboard/ ; exit")

print()
printMessage("PyKiln Setup Complete!")
print("Press the EN button, or unplug your ESP32 and plug it back in to restart it.")
print()
print("close this window or press enter to quit...")
input()
