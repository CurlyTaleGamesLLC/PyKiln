from machine import Pin, I2C
import mcp

class zones:

    def __init__(self, dev, i2cDevice=None):
        self.i2c = i2cDevice
        self.zones = dev.zones
        for z in self.zones:
            if z.iodevice == "MCP23008":
                self.i2c.setup(z.pin, mcp.OUT)
        self.Off(0)

    def On(self, i):
        if self.zones[i].iodevice == "GPIO":
            self.zones[i].pin.on()
        elif self.zones[i].iodevice == "MCP23008":
            self.i2c.output(self.zones[i].pin, True)
        else:
            print("Device not supported: " + self.zones[i].iodevice)

    def Off(self, i):
        if self.zones[i].iodevice == "GPIO":
            self.zones[i].pin.off()
        elif self.zones[i].iodevice == "MCP23008":
            self.i2c.output(self.zones[i].pin, False)
        else:
            print("Device not supported: " + self.zones[i].iodevice)

    def RangeOn(self, indexes):
        for i in indexes:
            self.On(i)
    
    def RangeOff(self, indexes):
        for i in indexes:
            self.Off(i)

