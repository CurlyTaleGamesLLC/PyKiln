import network
import uio
import ujson

import settings

ip = ""
wifi = {
    "ssid":"",
    "password":"",
    "host":""
}

def setup():
    global wifi
    print("wifi!")
    with uio.open("wifi.json") as fp:
        wifi = ujson.load(fp)
        print(ujson.dumps(wifi))

    if len(wifi["ssid"]) > 0:
        print(wifi["ssid"])
        connect(wifi["ssid"], wifi["password"])

def connect(ssid, password):
    global ip
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        ip = station.ifconfig()
        return
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass

    station.config(dhcp_hostname='PyKiln')
    print(station.config('dhcp_hostname'))

    print("Connection successful")
    ip = station.ifconfig()
    print(ip)
    if not settings.hasIP():
        settings.SetIP(ip[0])
        print("IP Assigned! " + ip[0])
        f = open("ip.txt", "w")
        f.write(ip[0])
        f.close()