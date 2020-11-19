import machine
import network
import ubinascii
import utime
import settings

ip = ""

def setup():
    
    if settings.isConfigured():
        # set up has been completed and user has been sent the IP address of their PyKiln
        connect()
    else:
        if settings.hasWiFiNetwork():
            if settings.hasIP():
                # let the user know the IP address of their PyKiln
                broadcast()
            else:
                # an IP address hasn't been assigned yet, let's get one
                connect()
        else:
            # wifi SSID hasn't been entered yet, ask the user for the credentials
            broadcast()

def connect():
    global ip
    # machine.Pin(0, machine.Pin.OUT)
    station = network.WLAN(network.STA_IF)

    # addr = '24:62:ab:fc:9b:bd'
    # addr = '2462abfc9bbd'
    # macbytes = ubinascii.unhexlify(addr)
    # station.config(mac=macbytes)
    # 24:62:ab:fc:9b:bc

    if station.isconnected() == True:
        print("Already connected")
        ip = station.ifconfig()
        return

    station.active(True)
    
    station.connect(settings.data["network"]["wifi"], settings.data["network"]["password"])
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
        utime.sleep(2)
        machine.reset()
        # reboot

def broadcast():
    global ip
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    
    staticIP = ['192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8']
    ap.ifconfig(staticIP)
    print(ap.ifconfig())

    ip = staticIP

    if settings.hasIP():
        print("Finished Configuration - manually reboot me")
        settings.SetConfigured()

    # ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    apName = "PyKiln Setup " + ubinascii.hexlify(network.WLAN().config('mac')).decode()
    ap.config(essid=apName, password="")
