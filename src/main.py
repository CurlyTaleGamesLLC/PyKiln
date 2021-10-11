# main.py
# import gc
import uos
import ujson
import machine
import utime

import uasyncio
import picoweb

# Custom Libraries
import settings
# import temperature
import speaker
import led

# Connect to WiFi
import wifi
connection = wifi.wifi()
print(connection.ip)
# print(connection.wifi.ip)
print(connection.GetIP())

pykilnSettings = settings.settings()
# notificationSpeaker = speaker.speaker()
# notificationLED = led.led()

app = picoweb.WebApp(__name__)

# def init():
#     global pyLed
#     print("Hello World!")
#     dev = device("PyKilnV1.01")

#     print(dev.led.iodevice)
#     print(dev.led.pin)
#     print(dev.led.i2cAddress)

#     i2c = I2C(scl=dev.scl, sda=dev.sda, freq=10000)
#     print(i2c.scan())
#     if dev.ioexpander.iodevice == "MCP23008":
#         io = mcp.MCP23008(i2c, dev.ioexpander.i2cAddress)

#     # LED - why is this blocking? this should be async
#     pyLed = led(dev.led, io)
#     pyLed.Error()

# If you try to access the PyKiln by it's IP redirect to the webpage to control it
@app.route("/")
def index(req, resp):
    hostURL = "https://pykiln.com/connect/"
    headers = {"Location": hostURL + "?ip=" + connection.ip}
    yield from picoweb.start_response(resp, status="303", headers=headers)


# @app.route("/status")
# def status(req, resp):
#     yield from picoweb.start_response(resp)
#     htmlFile = open('/templates/status.html', 'r')
#     for line in htmlFile:
#         yield from resp.awrite(line)
#     yield from resp.aclose()

@app.route("/api/led")
def api_led(req, resp):
    if req.method == "POST":
        print("Test RGB LED")
        yield from picoweb.http_error(resp, "200") # success!
        yield from resp.aclose()
        notificationLED.Error()
    else:
        yield from picoweb.http_error(resp, "405") 
        yield from resp.aclose()


@app.route("/api/speaker")
def api_speaker(req, resp):
    if req.method == "POST":
        print("Test Piezo Speaker")
        yield from picoweb.http_error(resp, "200") # success!
        yield from resp.aclose()
        notificationSpeaker.PlayFinished()
    else:
        yield from picoweb.http_error(resp, "405")
        yield from resp.aclose()


@app.route("/api/reboot")
def api_reboot(req, resp):
    if req.method == "POST":
        print("Rebooting PyKiln")
        yield from picoweb.http_error(resp, "200") # success!
        yield from resp.aclose()
        machine.reset()
    else:
        yield from picoweb.http_error(resp, "405")
        yield from resp.aclose()

@app.route("/api/temperature")
def apt_temperature(req, resp):
    yield from picoweb.start_response(resp, content_type="application/json")
    jsonData = {"sensor":"temperature", "value":"10"}
    encoded = ujson.dumps(jsonData)
    yield from resp.awrite(encoded)
    yield from resp.aclose()
    readings = range(20)
    for reading in readings:
        temperature.GetTemperature()
        utime.sleep(5)


@app.route("/api/status")
def api_status(req, resp):
    yield from picoweb.start_response(resp, content_type="application/json")
    jsonData = {"sensor":"temperature", "value":"10"}
    encoded = ujson.dumps(jsonData)
    yield from resp.awrite(encoded)
    yield from resp.aclose()

    
async def reboot_delay():
    await uasyncio.sleep(4)
    print('REBOOT!')
    await uasyncio.sleep(4)
    machine.reset()
    # reboot

app.run(debug=True, port=80, host=connection.ip)
