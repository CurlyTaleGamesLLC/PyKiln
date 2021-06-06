
from machine import I2C

sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)

# i2c = machine.I2C(sda=sda_pin, scl=scl_pin, freq=25000)
i2c = machine.I2C(sda=sda_pin, scl=scl_pin, freq=100000)

i2c.scan()

addr = 96
data = bytearray(2)

# SENSOR CONFIGURATION REGISTER
# config sensor for thermocouple type and filter
# 5 = 0000 0101
# 7 = 0 000 0 111 
#   = unused, k type thermocouple, unused, max filter
i2c.writeto(addr, bytes([5,7]))
i2c.writeto_mem(addr, 5, 7)


# config sensor for sample and mode
# DEVICE CONFIGURATION REGISTER 
# 6 = 0000 0110
# 124 = 0 11 111 00 
# #   = 0.0625°C cold junction resolution, 12bit resolution, 128 samples, normal operation
i2c.writeto(addr, bytes([6,124]))

def InitializeMCP9600():
    global addr
    global i2c
    i2c.writeto(addr, bytes([5,7]))
    i2c.writeto(addr, bytes([6,124]))

def ReadTemp():
    global addr
    global data
    global i2c
data = bytearray(2)
i2c.readfrom_into(addr, data)
temp = (data[0]*16 + data[1]/16)
ftemp = temp*1.8+32
print('Temperature in Celsius: ' + str(temp) + ', Fahrenheit: ' + str(ftemp))




# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
#https://store.ncd.io/product/mcp9600-k-type-thermocouple-i2c-mini-module/
import smbus
import time
address = 0x65

# Get I2C bus
bus = smbus.SMBus(1)
#bus.write_byte_data(address, 0xC0, 0x00)
# config sensor for thermocouple type and filter
bus.write_byte_data(address, 0x05, 0x07)
bList = [5,7]
i2c.writeto(96, bytes(bList))
# config sensor for sample and mode
bList2 = [6,124]
i2c.writeto(96, bytes(bList2))
bus.write_byte_data(address, 0x06, 0x7c)
#bus.write_byte(address,0xC0)


while True:
        bus.write_byte(address,0x00)
        i2c.writeto(96,b'0')

        data = bus.read_i2c_block_data(address, 0x00, 2)
        i2c.readfrom(96, 2)
        i2c.readfrom(96, b'2')
        temp =( data[0]*16 + data[1]/16)
        ftemp = temp*1.8+32
        print "temp in C : %.2f temp" %temp
        print "temp in f : %.2f ftemp" %ftemp
        time.sleep(1)










# import machine
# import sys
# import utime

# ###############################################################################
# # Parameters and global variables

# # Pin definitions
# repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
# repl_led = machine.Pin(5, machine.Pin.OUT)
# sda_pin = machine.Pin(21)
# scl_pin = machine.Pin(22)

# # Create an I2C object out of our SDA and SCL pin objects
# i2c = machine.I2C(sda=sda_pin, scl=scl_pin)

# # TMP102 address on the I2C bus
# tmp102_addr = 0x48

# # TMP102 register addresses
# reg_temp = 0x00
# reg_config = 0x01

# ###############################################################################
# # Functions

# # Calculate the 2's complement of a number
# def twos_comp(val, bits):
#     if (val & (1 << (bits - 1))) != 0:
#         val = val - (1 << bits)
#     return val

# # Read temperature registers and calculate Celsius
# def read_temp():

#     # Read temperature registers
#     val = i2c.readfrom_mem(tmp102_addr, reg_temp, 2)
#     temp_c = (val[0] << 4) | (val[1] >> 5)

#     # Convert to 2s complement (temperatures can be negative)
#     temp_c = twos_comp(temp_c, 12)

#     # Convert registers value to temperature (C)
#     temp_c = temp_c * 0.0625

#     return temp_c

# # Initialize communications with the TMP102
# def init():

#     # Read CONFIG register (2 bytes) and convert to integer list
#     val = i2c.readfrom_mem(tmp102_addr, reg_config, 2)
#     val = list(val)

#     # Set to 4 Hz sampling (CR1, CR0 = 0b10)
#     val[1] = val[1] & 0b00111111
#     val[1] = val[1] | (0b10 << 6)

#     # Write 4 Hz sampling back to CONFIG
#     i2c.writeto_mem(tmp102_addr, reg_config, bytearray(val))

# ###############################################################################
# # Main script

# # Print out temperature every second
# while True:

#     # If button 0 is pressed, drop to REPL
#     if repl_button.value() == 0:
#         print("Dropping to REPL")
#         repl_led.value(1)
#         sys.exit()

#     # Read temperature and print it to the console
#     temperature = read_temp()
#     print(round(temperature, 2), "C")
#     utime.sleep(1)
