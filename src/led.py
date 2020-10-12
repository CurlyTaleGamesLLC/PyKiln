import machine
import uasyncio

ledPin = machine.Pin(2, machine.Pin.OUT)
ledPin.value(0)

async def flash(flashCount, flashTime):
    global ledPin
    flashes = range(flashCount)
    for flash in flashes:
        ledPin.value(1)
        await uasyncio.sleep(flashTime)
        ledPin.value(0)
        await uasyncio.sleep(flashTime)
    ledPin.value(0)

def On():
    global ledPin
    ledPin.value(1)

def Off():
    global ledPin
    ledPin.value(0)

def Error():
    uasyncio.create_task(flash(5, 0.5))
    