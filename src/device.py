from machine import Pin
from iotype import iotype

class device:
    """
    Defines the pin mapping of PyKiln supported devices, currenly this is just the ESP32
    """

    def __init__(self, board):
        # GPIO pins
        self.relay = None
        self.currentSensor = None
        self.buzzer = None
        self.led = None
        
        # #I2C pins
        self.sda = None
        self.scl = None
        self.freq = None

        # #SPI SD Card Pins:
        self.sdo = None
        self.sdi = None
        self.sck = None
        self.cs = None

        # GPIO Expander - MCP23008
        self.ioexpander = None

        # Heating Zones
        self.zones = []

        # Fan & AUX
        self.aux = None
        self.fan = None

        # Temperature Sensors
        self.temps = []

        if board == "PyKilnV1.01":
            self.ESP32_MCP27008_MCP9600_v1_01()

    def ESP32_MCP27008_MCP9600_v1_01(self):
        #GPIO pins
        self.relay = iotype("GPIO", Pin(14, Pin.OUT))
        # self.relay = iotype("MCP23008", 7, 32)
        # self.currentSensor = iotype("GPIO", Pin(35))
        # self.buzzer = iotype("GPIO", Pin(32))
        self.led = iotype("GPIO", Pin(2, Pin.OUT))

        # #I2C pins
        self.sda = Pin(26)
        self.scl = Pin(25)
        self.freq = 10000

        # #SPI SD Card Pins:
        # self.sdo = iotype("GPIO", Pin(23))
        # self.sdi = iotype("GPIO", Pin(19))
        # self.sck = iotype("GPIO", Pin(18))
        # self.cs = iotype("GPIO", Pin(5))

        # #GPIO Expander - MCP23008
        addr = 32
        self.ioexpander = iotype("MCP23008", None, addr)

        # #Heating Zones
        self.zones = []
        self.zones.append(iotype("MCP23008", 0, addr))
        self.zones.append(iotype("MCP23008", 1, addr))
        self.zones.append(iotype("MCP23008", 2, addr))
        self.zones.append(iotype("MCP23008", 3, addr))
        self.zones.append(iotype("MCP23008", 4, addr))
        self.zones.append(iotype("MCP23008", 5, addr))
        self.zones.append(iotype("MCP23008", 6, addr))

        # #Fan & AUX
        # self.aux = iotype("MCP23008", 6, addr)
        # self.fan = iotype("MCP23008", 7, addr)

        # #Temperature Sensors
        self.temps = []
        self.temps.append(iotype("MCP9600", None, 96))
        self.temps.append(iotype("MCP9600", None, 98))
        self.temps.append(iotype("MCP9600", None, 101))
        self.temps.append(iotype("MCP9600", None, 103))
        




    
