import uasyncio
# Running on a generic board
from machine import Pin

async def CheckButton():
    button = Pin(35, Pin.IN)
    counter = 0
    while True:
        if button.value():
            counter = counter + 1
            if counter > 5:
                print("RESET WIFI")
                counter = 0
        elif counter > 0:
            counter = 0
            print("Not Held Long Enough")
        await uasyncio.sleep(1)

loop = uasyncio.get_event_loop()
loop.create_task(CheckButton())  # schedule asap
loop.run_forever()

# pretty sure I can delete this since wifi is now set up through command line
