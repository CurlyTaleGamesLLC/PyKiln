from machine import Pin, I2C
import adafruit_mcp9600

class temperature:
    """
    Provides PyKiln with access to the temperature sensors. Thermocouple type and units are defined in the settings.json
    """

    def __init__(self, dev, i2cDevice=None, thermocouple="K", isFahrenheit=False):
        self.i2c = i2cDevice
        self.tempDevices = dev.temps
        self.sensors = []
        self.temps = []
        self.fahrenheit = isFahrenheit

        scan = self.i2c.scan()
        print(scan)

        # Initialize all of the MCP9600 sensors and read the current temp
        for i in range(len(self.tempDevices)):
            if self.tempDevices[i].iodevice == "MCP9600" and self.tempDevices[i].i2cAddress in scan:
                print(self.i2c)
                print(self.tempDevices[i].i2cAddress)
                print(thermocouple)

                newSensor = adafruit_mcp9600.MCP9600(self.i2c, self.tempDevices[i].i2cAddress, thermocouple, 0)
                self.sensors.append(newSensor)
                self.temps.append(self.C2F(newSensor.temperature))

                # checkSensor = adafruit_mcp9600.MCP9600(self.i2c, self.tempDevices[i].i2cAddress, thermocouple, 0)
                # checkTemp = checkSensor.temperature
                # if checkTemp != 0:
                #     self.sensors.append(checkSensor)
                #     self.temps.append(checkTemp)

    def ReadTemp(self, i):
        if self.tempDevices[i].iodevice == "MCP9600":
            return self.C2F(self.sensors[i].temperature)
        else:
            print("Device not supported: " + self.tempDevices[i].iodevice)

    def C2F(self, reading):
        if self.fahrenheit:
            return (reading * 9.0/5.0) + 32
        else:
            return reading


    def ReadAllTemps(self):
        for i in range(len(self.sensors)):
            self.temps[i] = self.ReadTemp(i)
        return self.temps
