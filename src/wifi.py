import network
import uio
import ujson

import settings

class wifi:

    ip = ""
    login = {
        "ssid":"",
        "password":""
    }

    def __init__(self):
        self.ssid = ""
        self.password = ""
        self.ip = ""

        # Open Wifi Settings created from PyKiln Setup Utility
        with uio.open("wifi.json") as fp:
            login = ujson.load(fp)
            print(ujson.dumps(login))

        # If the SSID is valid, try to connect to it
        if len(login["ssid"]) > 0:
            print(login["ssid"])
            self.ssid = login["ssid"]
            self.password = login["password"]
            self.Connect()


    def Connect(self):
        # Set the ESP32 WiFi into client mode, where it connects to an access point 
        station = network.WLAN(network.STA_IF)
        if station.isconnected() == True:
            print("Already connected")
            self.ip = station.ifconfig()[0]
            return

        # If the ESP32 isn't connected to wifi try to connect
        station.active(True)
        station.connect(self.ssid, self.password)
        while station.isconnected() == False:
            pass

        # Connection was successful
        station.config(dhcp_hostname='PyKiln')
        print(station.config('dhcp_hostname'))

        print("Connection successful")
        ip = station.ifconfig()
        print(ip)

        self.ip = ip[0]

        print("IP Assigned! " + ip[0])
        f = open("ip.txt", "w")
        f.write(ip[0])
        f.close()

    def GetIP(self):
        return self.ip