from machine import ADC, Pin
import cmath as math
import utime

adc = None
currentCorrection = 0

def Init():
    global adc
    global currentCorrection
    adc = ADC(Pin(34))
    # print(adc.read())
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)
    print(adc.read())
    currentCorrection = Measure()

#Function that Calculate Root Mean Square
# def rmsValue(arr):
#     square = 0
#     mean = 0.0
#     root = 0.0
#     #Calculate square
#     for i in range(len(arr)): 
#         square += (arr[i]**2)
#     #Calculate Mean
#     mean = (square / (float)(len(arr))
#     #Calculate Root
#     root = cmath.sqrt(mean) 
#     return root

def Measure():
    global adc
    global currentCorrection
    
    print("Measure Current Lopp")
    isReading = True
    samples = 480 # Measure current for 1/10 of a second
    reading = 0.0
    rBurden = 100
    numTurns = 2000
    offset = 1.65
    acc = 0

    end_time = utime.ticks_ms()

    print("samples = " + str(samples))
    start_time = utime.ticks_ms()
    for i in range(0, samples):
        # Read analog value and convert to voltage
        reading = (adc.read() * 3.3) / 4096.0
        # Remove the DC offset
        reading = reading - offset
        # Calculate the sensed current
        reading = (reading / rBurden) * numTurns
        # Square the sensed current
        acc += reading * reading

        # uasyncio is too slow, we need to use sleep_us to get the speeds to read a 60 hertz sine wave
        # this delay and sample rate works out to measuring 6 cycles with 80 samples per cycle
        # the sleep value is tuned to account for overhead of reading 480 samples in 1/10 a second
        utime.sleep_us(88)

    end_time = utime.ticks_ms()

    print(str(utime.ticks_diff(end_time, start_time)))
    current = math.sqrt(acc / samples)
    current = current - currentCorrection
    print("current = " + str(current))
    return current

Init()