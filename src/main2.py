import time
from machine import Pin, I2C
# from device import device
import mcp
from device import device
from led import *
from relay import *
from zones import *

pyLed = None

def Start():
    global pyLed
    print("Hello World!")
    dev = device("PyKilnV1.01")

    print(dev.led.iodevice)
    print(dev.led.pin)
    print(dev.led.i2cAddress)

    i2c = I2C(scl=dev.scl, sda=dev.sda, freq=10000)
    print(i2c.scan())
    if dev.ioexpander.iodevice == "MCP23008":
        io = mcp.MCP23008(i2c, dev.ioexpander.i2cAddress)

    # LED - why is this blocking? this should be async
    pyLed = led(dev.led, io)
    pyLed.Error()

    # Relay
    # pyRelay = relay(dev.relay, io)
    # pyRelay.On()
    # time.sleep(2)
    # pyRelay.Off()
    # time.sleep(2)
    # pyRelay.On()
    # time.sleep(2)
    # pyRelay.Off()
    # time.sleep(2)

    # Zones
    pyZones = zones(dev, io)
    pyZones.RangeOn(range(2))
    time.sleep(2)
    pyZones.RangeOff(range(2))
    time.sleep(2)
    pyZones.RangeOn(range(2))
    time.sleep(2)
    pyZones.RangeOff(range(2))
    time.sleep(2)

    # pyZones.On(0)
    # time.sleep(2)
    # pyZones.Off(0)
    # time.sleep(2)
    # pyZones.On(0)
    # time.sleep(2)
    # pyZones.Off(0)
    # time.sleep(2)

if __name__=="__main__":
    Start()
