class iotype:
    """
    Specifies what pin and what device is used in mapping different boards
    """
    def __init__(self, setDevice, setPin, setAddress=None):
        self.iodevice = setDevice
        self.pin = setPin
        self.i2cAddress = setAddress

