import machine
# import utime
import uasyncio

class speaker:

    def __init__(self, pinNumber=15):
        self.pinNumber = pinNumber
        #self.ledPin = machine.Pin(self.ledPin, machine.Pin.OUT)

    async def PlaySong(self, notes, times):
        pwm = machine.PWM(machine.Pin(self.pinNumber))
        pwm.duty(512) # 50% duty cycle square wave
        for index in range(len(notes)):
            pwm.freq(notes[index])
            # utime.sleep(times[index])
            await uasyncio.sleep(times[index])
        pwm.deinit()

    def PlayFinished(self):
        # Finished!
        noteTimes = [0.25, 0.25, 0.5, 0.5, 1.5] # Hold times in seconds
        noteFreq = [2093, 2637, 3136, 3951, 4186] # C Musical Scale in Hertz - up a few octatives to match resonant frequency of piezo speaker
        # noteFreq = [523, 659, 784, 988, 1047] # C Musical Scale in Hertz
        # uasyncio.create_task(self.PlaySong(noteFreq, noteTimes)) 
        uasyncio.run(self.PlaySong(noteFreq, noteTimes))
    
    def PlayFinished2(self):
        # Finished!
        noteTimes = [0.25, 0.25, 0.5, 0.5, 1.5] # Hold times in seconds
        noteFreq = [1000, 2000, 8000, 2000, 4000] # C Musical Scale in Hertz - up a few octatives to match resonant frequency of piezo speaker
        # noteFreq = [523, 659, 784, 988, 1047] # C Musical Scale in Hertz
        # uasyncio.create_task(self.PlaySong(noteFreq, noteTimes)) 
        uasyncio.run(self.PlaySong(noteFreq, noteTimes)) 

    def PlayWarning(self):
        # Warning
        noteTimes = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
        # noteFreq = [587, 0, 587, 0, 587, 0, 587, 0, 587]
        noteFreq = [2349, 0, 2349, 0, 2349, 0, 2349, 0, 2349]
        uasyncio.run(self.PlaySong(noteFreq, noteTimes))

    def PlayWarning2(self):
        # Warning
        noteTimes = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
        # noteFreq = [587, 0, 587, 0, 587, 0, 587, 0, 587]
        noteFreq = [4000, 0, 4000, 0, 4000, 0, 4000, 0, 4000]
        uasyncio.run(self.PlaySong(noteFreq, noteTimes))

    def PlayStart(self):
        # Start
        noteTimes = [0.125, 0.25]
        # noteFreq = [523, 1047]
        noteFreq = [2093, 4186] # up a few octatives to match resonant frequency of piezo speaker
        uasyncio.create_task((self.PlaySong(noteFreq, noteTimes)))






