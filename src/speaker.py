from machine import Pin, I2C
# import utime
import mcp
import uasyncio

class speaker:

    def __init__(self, speakerDevice, i2cDevice=None):
        self.device = speakerDevice.iodevice
        self.speakerPin = speakerDevice.pin
        self.i2c = i2cDevice

        if self.device == "MCP23008":
            self.i2c.setup(self.speakerPin, mcp.OUT)
        self.Stop()

    # Odd indexes in the list of times are pauses in the buzzer
    async def PlayBuzzer(self, times):
        for index in range(len(times)):
            if (index % 2) == 0:
                self.Play()
            else:
                self.Stop()
            # utime.sleep(times[index])
            await uasyncio.sleep(times[index])
        self.Stop()

    def PlayFinished(self):
        # Finished!
        noteTimes = [0.25, 0.25, 0.5, 0.5, 1.5] # Hold times in seconds
        # uasyncio.create_task(self.PlaySong(noteFreq, noteTimes)) 
        uasyncio.run(self.PlayBuzzer(noteTimes))
    
    def PlayFinished2(self):
        # Finished!
        noteTimes = [0.25, 0.25, 0.5, 0.5, 1.5] # Hold times in seconds
        # uasyncio.create_task(self.PlaySong(noteFreq, noteTimes)) 
        uasyncio.run(self.PlayBuzzer(noteTimes)) 

    def PlayWarning(self):
        # Warning
        noteTimes = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
        uasyncio.run(self.PlayBuzzer(noteTimes))

    def PlayWarning2(self):
        # Warning
        noteTimes = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
        uasyncio.run(self.PlayBuzzer(noteTimes))

    def PlayStart(self):
        # Start
        noteTimes = [0.125, 0.25]
        uasyncio.create_task((self.PlayBuzzer(noteTimes)))

    def Play(self):
        if self.device == "GPIO":
            self.speakerPin.on()
        elif self.device == "MCP23008":
            self.i2c.output(self.speakerPin, True)
        else:
            print("Device not supported: " + self.device)
    
    def Stop(self):
        if self.device == "GPIO":
            self.speakerPin.off()
        elif self.device == "MCP23008":
            self.i2c.output(self.speakerPin, False)
        else:
            print("Device not supported: " + self.device)






