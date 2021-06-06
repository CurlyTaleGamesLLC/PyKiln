import os
import subprocess
import sys
import json
import serial.tools.list_ports
from random import randrange


page = "splash"

serialPortsBefore = ""
serialDevicesBefore = ""
serialPortsDetected = ""
serialDevicesDetected = ""

parent = os.path.dirname(os.path.dirname(__file__))
src_folder = os.path.join(parent, 'src')


def SerialReset():
    global serialPortsBefore
    global serialDevicesBefore
    serialPortsBefore = list_serial_options(True)
    print(serialPortsBefore)
    serialDevicesBefore = list_serial_options(False)

def SerialSet():
    global serialPortsBefore
    global serialPortsDetected
    global serialDevicesBefore
    global serialDevicesDetected
    # global serialPortsAfter
    # global serialDevicesAfter

    serialPortsAfter = list_serial_options(True)
    print(serialPortsAfter)
    serialDevicesAfter = list_serial_options(False)
    serialPortsDetected = Diff(serialPortsAfter, serialPortsBefore)
    serialDevicesDetected = Diff(serialDevicesAfter, serialDevicesBefore)

def GetActiveSerialPort():
    global serialPortsDetected
    print("GET ")
    print(serialPortsDetected)
    if len(serialPortsDetected) == 0:
        return ""
    return serialPortsDetected[0]

def GetCurrentPage():
    global page
    return page

def SetCurrentPage(newPage):
    global page
    page = newPage

def install(package):
    print("Installing " + package)
    # printMessage("Installing " + package)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    # print()

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

def WifiLogin(ssid, password, host):
    wifiJSON = {
        "ssid": ssid,
        "password": password,
        "host": host
    }
    fpath = os.path.join(src_folder, 'wifi.json')
    f = open(fpath, "w")
    f.write(json.dumps(wifiJSON))
    f.close()

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def CreatePyKilnShortcut(host, ip):

    desktop = ""

    if sys.platform == 'darwin':
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    else:
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

    shortcutName = "PyKiln-" + ip + "-(" + str(randrange(99)) + ").url"
    shortcutURL = ""
    if host == "":
        shortcutURL = "http://pykiln.com/"
    else:
        shortcutURL = "http://" + host

    f = open(os.path.join(desktop, shortcutName), "w")
    f.write("[InternetShortcut]\n")
    f.write("URL=" + shortcutURL + "?ip=" + ip + "\n")
    f.write("\n")
    f.close()


def OpenBrowser(ipURL):
    if sys.platform == 'darwin':    # in case of OS X
        subprocess.Popen(['open', ipURL])
    else:
        webbrowser.open(ipURL, new=0, autoraise=True)

    # ip = open("ip.txt", "r")
    # ipURL = "http://" + ip.read()
    # print("IP = " + ipURL)