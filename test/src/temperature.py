import uasyncio
import max31856
import settings

pins = [4, 16, 17, 5]
csPins = []
count = 0
for i in pins:
    print(i)
    if count < settings.data["kiln"]["sensors"]:
        print("adding Temp " + str(i))
        csPins.append(i)
    count = count + 1

def GetTemperature():
    print("Getting Temps")
    uasyncio.create_task(GetTemps())

async def GetTemps():
    global csPins
    for i in csPins:
        SensorTemp(i)
        await uasyncio.sleep(0.5)

def SensorTemp(csPin):
    # Connect to MAX31856
    # csPin = 5
    misoPin = 19
    mosiPin = 23
    clkPin = 18
    max = max31856.max31856(csPin, misoPin, mosiPin, clkPin)

    # Thermocouple Temp
    thermoTempC = max.readThermocoupleTemp()
    thermoTempF = (thermoTempC * 9.0/5.0) + 32
    if settings.data["kiln"]["units"] == "fahrenheit":
        print("Thermocouple Temp: %f degF" % thermoTempF)
    else:
        print("Thermocouple Temp: %f degC" % thermoTempC)
    # Chip Temp
    juncTempC = max.readJunctionTemp()
    juncTempF = (juncTempC * 9.0/5.0) + 32
    if settings.data["kiln"]["units"] == "fahrenheit":
        print("Cold Junction Temp: %f degF" % juncTempF)
    else:
        print("Cold Junction Temp: %f degC" % juncTempC)
