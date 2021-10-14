from machine import Pin, I2C
import mcp

class relay:

    """
    Allows PyKiln to control the main power to the kiln. 
    The relay is turned on at the start of a firing schedule and off at the end.
    """

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
