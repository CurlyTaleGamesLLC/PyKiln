import machine
import uasyncio

class led:

    def __init__(self, ledPin=2):
        self.ledPin = machine.Pin(ledPin, machine.Pin.OUT)
        print(self.ledPin)

    async def Flash(self, flashCount, flashTime):
        flashes = range(flashCount)
        for flash in flashes:
            self.ledPin.value(1)
            await uasyncio.sleep(flashTime)
            self.ledPin.value(0)
            await uasyncio.sleep(flashTime)
        self.ledPin.value(0)

    def On(self):
        self.ledPin.value(1)

    def Off(self):
        self.ledPin.value(0)

    def Error(self):
        # uasyncio.create_task(self.Flash(5, 0.5))
        uasyncio.run(self.Flash(5, 0.5))
    