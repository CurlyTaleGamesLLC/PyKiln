import math
from machine import ADC, Pin

class Current():
    """Measures the current of a circuit using a non invasive current sensor. 
    The AC signal is offset to be in the 0V-3.3V range, and then sampled 
    with the ADC to find the power usage.
    """

    def __init__(self, pin=35, numTurns=2000, samples=1000):
        """Initialize Non invasive current sensor at specified ADC pin. 
        Default turns is 2000 for a 100A CT sensor
        """
        self.adc = ADC(Pin(pin))
        self.samples = samples
        self.currentCorrection = 0

        self.reading = 0.0

        # burden resistor
        self.rBurden = 100
        # number of turns of the CT sensor
        self.numTurns = numTurns

        # this is used to remove the DC bias of the AC signal
        self.offset = 1.65 # half of 3.3V
        
        # accumulated value
        self.acc = 0

        # set voltage range of ADC to 0-3.6V
        self.adc.atten(ADC.ATTN_11DB)
        # set ADC values from 0-4096
        self.adc.width(ADC.WIDTH_12BIT)

        print(self.adc.read())
        print("Calibrating Current:")
        self.Calibrate()

    def Calibrate(self):
        # This might needs to removed. Originally I was trying zero out the current sensor
        # But when there is no current flowing through the wire it isn't generating a magnetic field
        # So the readings are eratic. It makes more sense to use a simple threshold than try to zero
        # out eratic data. Once there is current flowing the readings are accurate.
        self.currentCorrection = 0
        # self.currentCorrection = self.Measure()


    def Measure(self):
        self.acc = 0

        # Read samples as fast as possible to capture an acurate reading of the current
        for i in range(0, self.samples):
            # Read analog value and convert to voltage
            self.reading = (self.adc.read() * 3.3) / 4096.0
            # Remove the DC offset
            self.reading = self.reading - self.offset
            # Calculate the sensed current
            self.reading = (self.reading / self.rBurden) * self.numTurns
            # Square the sensed current
            self.acc += self.reading * self.reading

        # Divide the total squared sensed current by the number of samples, 
        # and take the square root of that number 
        self.current = math.sqrt(self.acc / self.samples)
        # Subtract the calibration current from the result
        self.current = self.current - self.currentCorrection
        
        print('{:.12f}'.format(float(self.current)))
        return self.current