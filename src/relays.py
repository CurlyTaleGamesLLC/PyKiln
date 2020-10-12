import machine
import uasyncio
import settings

pins = [12, 14, 27, 26, 25, 33, 32]
relayPins = []

count = -1
for i in pins:
    print(i)
    relay = machine.Pin(i, machine.Pin.OUT)
    relay.value(0)

    if(count < settings.data["kiln"]["zones"]):
        print("adding " + str(i))
        relayPins.append(relay)
    count = count + 1
    

def StartFiring():
    global relayPins
    relayPins[0].value(1)

def StopFiring():
    global relayPins
    relayPins[0].value(0)

def Test():
    print("testing")
    uasyncio.create_task(TestEach())

def TestZones():
    uasyncio.create_task(TestAllZones())

async def TestAll():
    global pins
    print("test all")
    for i in pins:
        relay = machine.Pin(i, machine.Pin.OUT)
        print(str(i) + " ON")
        relay.value(1)
    await uasyncio.sleep(2)
    
    for i in pins:
        print(str(i) + " OFF")
        relay.value(0)
    await uasyncio.sleep(2)

async def TestEach():
    global pins
    print("test each")
    for i in pins:
        relay = machine.Pin(i, machine.Pin.OUT)
        print(str(i) + " ON")
        relay.value(1)
        await uasyncio.sleep(0.5)
        print(str(i) + " OFF")
        relay.value(0)
        await uasyncio.sleep(0.5)

async def TestAllZones():
    global relayPins
    for i in relayPins:
        i.value(1)
    await uasyncio.sleep(2)
    for i in relayPins:
        i.value(0)
    await uasyncio.sleep(2)
