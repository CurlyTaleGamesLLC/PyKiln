import json
import os
import subprocess
import sys
import glob
import time
import webbrowser
import serial.tools.list_ports

import socket
import netifaces
from random import randrange

print("WUTUP!!!")

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

# def install(package):
#     print("Installing " + package)
#     # printMessage("Installing " + package)
#     subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#     # print()

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



def Subnet2CIDR(argument):
    switcher = {
        "255.255.255.255": "/32",
        "255.255.255.254": "/31",
        "255.255.255.252": "/30",
        "255.255.255.248": "/29",
        "255.255.255.240": "/28",
        "255.255.255.224": "/27",
        "255.255.255.192": "/26",
        "255.255.255.128": "/25",
        "255.255.255.0": "/24",
        "255.255.254.0": "/22",
        "255.255.248.0": "/21",
        "255.255.240.0": "/20",
        "255.255.224.0": "/19",
        "255.255.192.0": "/18",
        "255.255.128.0": "/17",
        "255.255.0.0": "/16",
        "255.254.0.0": "/15",
        "255.252.0.0": "/14",
        "255.248.0.0": "/13",
        "255.240.0.0": "/12",
        "255.224.0.0": "/11",
        "255.192.0.0": "/10",
        "255.128.0.0": "/9",
        "255.0.0.0": "/8",
        "254.0.0.0": "/7",
        "252.0.0.0": "/6",
        "248.0.0.0": "/5",
        "240.0.0.0": "/4",
        "224.0.0.0": "/3",
        "192.0.0.0": "/2",
        "128.0.0.0": "/1",
        "0.0.0.0": "/0",
    }
    return switcher.get(argument, "Invalid Subnet Mask")

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


def GetIP():
    myIP = socket.gethostbyname(socket.gethostname())
    interface_list = netifaces.interfaces()
    # Get addresses, netmask, etc. information 
    address_entries = (netifaces.ifaddresses(iface) for iface in interface_list)
    address_entries2 = (netifaces.ifaddresses(iface) for iface in interface_list)
    # Only pay attention to ipv4 address types
    ipv4_address_entries = (address[netifaces.AF_INET] for address in address_entries if netifaces.AF_INET in address)
    ipv4_address_entries2 = (address2[netifaces.AF_INET] for address2 in address_entries2 if netifaces.AF_INET in address2)
    # Since multiple addresses can be associated, only look at the first ip address
    ipv4_addresses = [address[0]['addr'] for address in ipv4_address_entries]
    dns = [address2[0]['netmask'] for address2 in ipv4_address_entries2]

    print(ipv4_addresses)
    print(dns)

    ipCIDRList = []
    ipList = []
    for checkIP, checkDNS in zip(ipv4_addresses, dns):
        print("{}, {}".format(checkIP, checkDNS))
        if checkIP != "127.0.0.1":
            ipCIDRList.append(checkIP + Subnet2CIDR(checkDNS))

    ipCIDRString = ','.join(map(str,ipCIDRList))
    print(ipCIDRString)
    OpenBrowser("http://pykiln.com/?devices=" + ipCIDRString)

    CreatePyKilnShortcut("", "192.168.50.45")