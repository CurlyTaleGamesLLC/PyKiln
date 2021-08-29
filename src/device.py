from machine import Pin
from iotype import iotype

class device:
    """
    Defines the pin mapping of PyKiln supported devices
    """

    def __init__(self):
        #GPIO pins
        self.relay = None
        self.currentSensor = None
        self.buzzer = None
        self.led = None
        
        #I2C pins
        self.sda = None
        self.scl = None

        #SPI SD Card Pins:
        self.sdo = None
        self.sdi = None
        self.sck = None
        self.cs = None

        #GPIO Expander - MCP23008
        self.ioexpander = None

        #Heating Zones
        self.zone1 = None
        self.zone2 = None
        self.zone3 = None
        self.zone4 = None
        self.zone5 = None
        self.zone6 = None

        #Fan & AUX
        self.aux = None
        self.fan = None

        #Temperature Sensors
        self.temp1 = None
        self.temp2 = None
        self.temp3 = None
        self.temp4 = None

        self.ESP32_MCP27008_MCP9600_v1_01()
    
    def ESP32_MCP27008_MCP9600_v1_01(self):

        #GPIO pins
        self.relay = iotype("GPIO", Pin(14))
        self.currentSensor = iotype("GPIO", Pin(35))
        self.buzzer = iotype("GPIO", Pin(32))
        self.led = iotype("GPIO", Pin(2))

        #I2C pins
        self.sda = iotype("GPIO", Pin(26))
        self.scl = iotype("GPIO", Pin(25))

        #SPI SD Card Pins:
        self.sdo = iotype("GPIO", Pin(23))
        self.sdi = iotype("GPIO", Pin(19))
        self.sck = iotype("GPIO", Pin(18))
        self.cs = iotype("GPIO", Pin(5))

        #GPIO Expander - MCP23008
        address = 32
        self.ioexpander = iotype("MCP23008", None, address)

        #Heating Zones
        self.zone1 = iotype("MCP23008", 0, address)
        self.zone2 = iotype("MCP23008", 1, address)
        self.zone3 = iotype("MCP23008", 2, address)
        self.zone4 = iotype("MCP23008", 3, address)
        self.zone5 = iotype("MCP23008", 4, address)
        self.zone6 = iotype("MCP23008", 5, address)

        #Fan & AUX
        self.aux = iotype("MCP23008", 6, address)
        self.fan = iotype("MCP23008", 7, address)

        #Temperature Sensors
        self.temp1 = iotype("MCP9600", None, 96)
        self.temp2 = iotype("MCP9600", None, 96)
        self.temp3 = iotype("MCP9600", None, 96)
        self.temp4 = iotype("MCP9600", None, 96)
        




    
