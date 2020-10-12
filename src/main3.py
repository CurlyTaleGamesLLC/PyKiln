# main.py
import gc
import uos
import machine
import utime
import ujson

import settings

print(settings.data)


# Connect to WiFi
import wifiConnect
wifiConnect.setup()