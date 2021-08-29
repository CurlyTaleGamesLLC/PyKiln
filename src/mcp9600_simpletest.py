# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# Ported to Micropython by Ben Nyx for Curly Tale Games LLC

import time
from machine import Pin, I2C
import adafruit_mcp9600
import mcp

relay = Pin(4, Pin.OUT)
relay.value(1)
time.sleep(2)

# 5v
# [32, 103]

# 3.33v
# [32, 100]

# 1.66v
# [32, 98]

# 0v
# [32, 96]


# i2c = I2C(1, freq=15000)
# I2C bus 1 default pins:
# scl = 25
# sda = 26

i2c = I2C(scl=Pin(25), sda=Pin(26), freq=10000)

# i2c = I2C(0, freq=100000)
# I2C bus 0 default pins:
# scl = 18
# sda = 19

# i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=15000)
# i2c = I2C(scl=Pin(22), sda=Pin(21), freq=15000)
print(i2c.scan())

mcp2 = adafruit_mcp9600.MCP9600(i2c, 96, "K", 0)

fanPin = 7

io = mcp.MCP23008(i2c, 32)
io.setup(fanPin, mcp.OUT)
io.setup(3, mcp.OUT)
io.setup(0, mcp.OUT)
io.setup(1, mcp.OUT)

while True:
    print((mcp2.ambient_temperature, mcp2.temperature, mcp2.delta_temperature))
    io.output(1,True)
    io.output(fanPin,True)
    time.sleep(1)
    io.output(1,False)
    io.output(fanPin,False)
    time.sleep(1)
