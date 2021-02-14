import json
import os
import subprocess
import sys
import glob
import time
import webbrowser
import serial.tools.list_ports


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

def writeWifiJSON(ssid, password, host):
    wifiJSON = {
        "ssid": ssid,
        "password": password,
        "host": host
    }
    f = open("wifi.json", "w")
    f.write(json.dumps(wifiJSON))
    f.close()

def loading(loadingMessage, seconds):
    block = "#"
    progress = ""
    for x in range(seconds * 4):
        printMessage(loadingMessage)
        progress = progress + block
        print(progress)
        time.sleep(0.25)
        cls()