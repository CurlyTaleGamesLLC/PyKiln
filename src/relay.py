from machine import Pin, I2C
# import machine
# import uasyncio
# import settings
import mcp


class relay:

    def __init__(self, relayDevice, i2cDevice=None):
        self.relayDevice = relayDevice.iodevice
        # self.device = self.relay.iodevice
        self.relayPin = relayDevice.pin
        self.i2c = i2cDevice

        if self.relayDevice == "MCP23008":
            self.i2c.setup(self.relayPin, mcp.OUT)
        self.Off()

    def On(self):
        if self.relayDevice == "GPIO":
            self.relayPin.on()
        elif self.relayDevice == "MCP23008":
            self.i2c.output(self.relayPin, True)
        else:
            print("Device not supported: " + self.relayDevice)

    def Off(self):
        if self.relayDevice == "GPIO":
            self.relayPin.off()
        elif self.relayDevice == "MCP23008":
            self.i2c.output(self.relayPin, False)
        else:
            print("Device not supported: " + self.relayDevice)
