import time
from machine import Pin, I2C
import adafruit_mcp9600
import mcp
import storage
import current

def TestMCP23008():
    print("Scanning I2C Devices for MCP23008")

    i2c = I2C(scl=Pin(25), sda=Pin(26), freq=10000)
    print(i2c.scan())

    # Connect and set up MCP23008
    io = mcp.MCP23008(i2c, 32)
    gpioPins = range(8)
    for x in gpioPins:
        # print(x)
        io.setup(x, mcp.OUT)

    print("Turning MCP23008 GPIO Pins On and Off")
    while True:
        for x in gpioPins:
            io.output(x, True)
        time.sleep(5)

        for x in gpioPins:
            io.output(x, False)
        time.sleep(5)

def TestMCP9600():
    print("Scanning I2C Devices for MCP9600")

    i2c = I2C(scl=Pin(25), sda=Pin(26), freq=10000)
    print(i2c.scan())
    sensor = adafruit_mcp9600.MCP9600(i2c, 96, "K", 0)

    print("Reading Temperature of MCP9600")
    print("Ambient, Thermocouple, Difference")
    while True:
        print((sensor.ambient_temperature, sensor.temperature, sensor.delta_temperature))
        time.sleep(1)


def TestLED():
    print("Flashing LED")
    led = Pin(2, Pin.OUT)
    while True:
        led.value(1)
        time.sleep(2)
        led.value(0)
        time.sleep(2)

def TestRelay():
    print("Turning Relay On and Off")
    relay = Pin(14, Pin.OUT)
    while True:
        relay.value(1)
        time.sleep(5)
        relay.value(0)
        time.sleep(5)

def TestBuzzer():
    print("Turning Buzzer On and Off")
    buzzer = Pin(32, Pin.OUT)
    while True:
        buzzer.value(1)
        time.sleep(1)
        buzzer.value(0)
        time.sleep(1)

def TestSDCard():
    sd = storage.logging()
    sd.Connect()
    testname = "TestSDCard.csv"

    # Append some data to the CSV file
    sd.Log(testname, [1,2,3,7])
    sd.Log(testname, [2,2,3,6])
    sd.Log(testname, [3,2,3,5])
    sd.Log(testname, [4,2,3,4])
    sd.Log(testname, [5,2,3,3])
    sd.Log(testname, [6,2,3,2])
    sd.Log(testname, [7,2,3,1])

    #Read and print the contents of the CSV file
    sd.Read(testname)
    print(sd.LogList())

def TestCurrentSensor():
    print("Reading Current Sensor")
    # Sets up the current sensor
    ctsensor = current.Current()

    # Samples the current flowing through a wire
    while True:
        ctsensor.Measure()
        time.sleep(0.1)


def Test():
    print("#################")
    print("PyKiln Self Check")
    print("#################")
    print("")
    print("1. Test LED")
    print("2. Test Buzzer")
    print("3. Test Contactor Relay")
    print("4. Test Current Sensor")
    print("5. Test SD Card")
    print("6. Test MCP9600 (Temperature Sensor)")
    print("7. Test MCP23008 (GPIO Expander)")
    print("")
    inputTest = input("Type 1-7: ")

    if inputTest == "1":
        TestLED()
    elif inputTest == "2":
        TestBuzzer()
    elif inputTest == "3":
        TestRelay()
    elif inputTest == "4":
        TestCurrentSensor()
    elif inputTest == "5":
        TestSDCard()
    elif inputTest == "6":
        TestMCP9600()
    elif inputTest == "7":
        TestMCP23008()
    else:
        print("Input not recognized")
        Test()


if __name__=="__main__":
    Test()