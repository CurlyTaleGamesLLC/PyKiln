from machine import Pin, I2C
import mcp
import uasyncio

class led:

    def __init__(self, ledDevice, i2cDevice=None):
        self.device = ledDevice.iodevice
        self.ledPin = ledDevice.pin
        self.i2c = i2cDevice

        if self.device == "MCP23008":
            self.i2c.setup(self.ledPin, mcp.OUT)
        self.Off()
        

    async def Flash(self, flashCount, flashTime):
        flashes = range(flashCount)
        for flash in flashes:
            self.On()
            await uasyncio.sleep(flashTime)
            self.Off()
            await uasyncio.sleep(flashTime)
        self.Off()

    def On(self):
        if self.device == "GPIO":
            self.ledPin.on()
        elif self.device == "MCP23008":
            self.i2c.output(self.ledPin, True)
        else:
            print("Device not supported: " + self.device)
    
    def Off(self):
        if self.device == "GPIO":
            self.ledPin.off()
        elif self.device == "MCP23008":
            self.i2c.output(self.ledPin, False)
        else:
            print("Device not supported: " + self.device)

    def Error(self):
        # uasyncio.create_task(self.Flash(5, 0.5))
        uasyncio.run(self.Flash(5, 0.5))
    