import uasyncio
# Running on a generic board
from machine import Pin

# Custom Libraries
import max31856

import speaker
import relays
import led
import temperature
import current

async def CheckButton():
    button = Pin(35, Pin.IN)
    counter = 0
    while True:
        if button.value():
            counter = counter + 1
            if counter > 5:
                print("DEBUG TESTING:")
                counter = 0
                speaker.PlayFinished()
                relays.Test()
                led.Error()
                # temperature.GetTemperature()
        elif counter > 0:
            counter = 0
            print("Not Held Long Enough")
            # temperature.SensorTemp(16)
            current.Measure()
        await uasyncio.sleep(1)

loop = uasyncio.get_event_loop()
loop.create_task(CheckButton())  # schedule asap
loop.run_forever()
