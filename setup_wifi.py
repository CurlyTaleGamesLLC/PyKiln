import json
import os
import serial.tools.list_ports
from setup_utils import *


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

# printMessage("PyKiln Installed, Reset the ESP32")
# print("Press the EN button on the ESP32 to reset it")
# print()
# print("press enter to connect to WiFi...")
# input()
