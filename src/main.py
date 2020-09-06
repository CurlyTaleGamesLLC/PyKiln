# main.py
import gc
import uos
import ujson
import machine
import utime

# Connect to WiFi
import wifiConnect
wifiConnect.connect()

# Install Dependencies
import install

import ulogging
import utemplate
import uasyncio
import picoweb

# Custom Libraries
import max31856

rled = None
gled = None
bled = None

def df():
    s = uos.statvfs('//')
    return ('{0} MB'.format((s[0]*s[3])/1048576))

print("Filespace Available: " + df())

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    # redirect to "/"
    headers = {"Location": "http://localhost/index.html?ip=" + wifiConnect.ip[0]}
    yield from picoweb.start_response(resp, status="303", headers=headers)

@app.route("/status")
def status(req, resp):
    # yield from picoweb.start_response(resp)
    # yield from app.render_template(resp, "status.html", (req,))

    yield from picoweb.start_response(resp)
    htmlFile = open('/templates/status.html', 'r')
    for line in htmlFile:
        yield from resp.awrite(line)


@app.route("/api/led")
def api_led(req, resp):
    if req.method == "POST":
        print("Test RGB LED")
        yield from picoweb.http_error(resp, "200") # success!
        # LED
        # led_rgb(255,0,255)
        led_rgb_flash(255, 0, 255, 5, 0.5)
    else:
        yield from picoweb.http_error(resp, "405") 


@app.route("/api/speaker")
def api_speaker(req, resp):
    if req.method == "POST":
        print("Test Piezo Speaker")
        yield from picoweb.http_error(resp, "200") # success!

        # Finished!
        noteTimes = [0.25, 0.25, 0.5, 0.5, 1.5]
        noteFreq = [523, 659, 784, 988, 1047] # C Musical Scale in Hertz

        # Warning
        # noteTimes = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
        # noteFreq = [587, 0, 587, 0, 587, 0, 587, 0, 587]

        # Start
        # noteTimes = [0.125, 0.25]
        # noteFreq = [523, 1047]

        PlaySong(noteFreq, noteTimes)
    else:
        yield from picoweb.http_error(resp, "405")


@app.route("/api/reboot")
def api_reboot(req, resp):
    if req.method == "POST":
        print("Rebooting PyKiln")
        yield from picoweb.http_error(resp, "200") # success!
        machine.reset()
    else:
        yield from picoweb.http_error(resp, "405")

@app.route("/api/temperature")
def apt_temperature(req, resp):
    yield from picoweb.start_response(resp, content_type="application/json")
    jsonData = {"sensor":"temperature", "value":"10"}
    encoded = ujson.dumps(jsonData)
    yield from resp.awrite(encoded)
    readings = range(20)
    for reading in readings:
        get_temp()
        utime.sleep(5)


@app.route("/api/status")
def api_status(req, resp):
    yield from picoweb.start_response(resp, content_type="application/json")
    jsonData = {"sensor":"temperature", "value":"10"}
    encoded = ujson.dumps(jsonData)
    yield from resp.awrite(encoded)

def get_temp():
    csPin = 5
    misoPin = 19
    mosiPin = 23
    clkPin = 18
    max = max31856.max31856(csPin,misoPin,mosiPin,clkPin)

    thermoTempC = max.readThermocoupleTemp()
    thermoTempF = (thermoTempC * 9.0/5.0) + 32
    # print ("Thermocouple Temp: %f degF" % thermoTempF)
    # print ("Thermocouple Temp: %f degC" % thermoTempC)
    juncTempC = max.readJunctionTemp()
    juncTempF = (juncTempC * 9.0/5.0) + 32
    print ("Cold Junction Temp: %f degF" % juncTempF)
    # print ("Cold Junction Temp: %f degC" % juncTempC)

def PlaySong(notes, times):
    pwm = machine.PWM(machine.Pin(27))
    pwm.duty(512) # 50% duty cycle square wave
    # for note in noteFreq:
    #     pwm.freq(note)
    #     utime.sleep(noteTime)
    for index in range(len(notes)):
        pwm.freq(notes[index])
        utime.sleep(times[index])
    pwm.deinit()

def led_rgb(r, g, b):
    global rled
    global gled
    global bled
    rled = machine.PWM(machine.Pin(13), freq=1000, duty=int((r/255) * 1023))
    gled = machine.PWM(machine.Pin(12), freq=1000, duty=int((g/255) * 1023))
    bled = machine.PWM(machine.Pin(14), freq=1000, duty=int((b/255) * 1023))


def led_rgb_off():
    global rled
    global gled
    global bled
    rled.deinit()
    gled.deinit()
    bled.deinit()

def led_rgb_flash(r, g, b, flashCount, flashTime):
    flashes = range(flashCount)
    for flash in flashes:
        led_rgb(r, g, b)
        utime.sleep(flashTime)
        led_rgb(0, 0, 0)
        utime.sleep(flashTime)
    led_rgb_off()

    


app.run(debug=True, port=80, host=wifiConnect.ip[0])
