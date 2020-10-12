import machine
# import utime
import uasyncio

async def PlaySong(notes, times):
    pwm = machine.PWM(machine.Pin(27))
    pwm.duty(512) # 50% duty cycle square wave
    for index in range(len(notes)):
        pwm.freq(notes[index])
        # utime.sleep(times[index])
        await uasyncio.sleep(times[index])
    pwm.deinit()

def PlayFinished():
    # Finished!
    noteTimes = [0.25, 0.25, 0.5, 0.5, 1.5] # Hold times in seconds
    noteFreq = [523, 659, 784, 988, 1047] # C Musical Scale in Hertz
    uasyncio.create_task(PlaySong(noteFreq, noteTimes)) 

def PlayWarning():
    # Warning
    noteTimes = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
    noteFreq = [587, 0, 587, 0, 587, 0, 587, 0, 587]
    uasyncio.create_task(PlaySong(noteFreq, noteTimes)) 

def PlayStart():
    # Start
    noteTimes = [0.125, 0.25]
    noteFreq = [523, 1047]
    uasyncio.create_task(PlaySong(noteFreq, noteTimes)) 






