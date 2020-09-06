import machine
import network

ip = ""

def connect():
    global ip
    ssid = "Hey You Kids Get Off Our LAN!"
    password = "1234567890"

    machine.Pin(0, machine.Pin.OUT)

    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        ip = station.ifconfig()
        return

    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass

    print("Connection successful")
    ip = station.ifconfig()
    print(station.ifconfig())
