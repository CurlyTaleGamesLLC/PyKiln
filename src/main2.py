# main.py
# import gc
import uos
import ujson
import machine
import utime
import settings

# import blink

import uasyncio
import picoweb

# Custom Libraries
import temperature
import speaker
import led

# Connect to WiFi
import wifi
wifi.setup()


app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    # redirect to "/"
    hostURL = "http://pykiln.com/pykiln/"
    if wifi.wifi.host == "":
        hostURL = "http://" + wifi.wifi.host + "/pykiln/"
    
    headers = {"Location": hostURL + "?ip=" + wifi.ip[0]}
    
    yield from picoweb.start_response(resp, status="303", headers=headers)


@app.route("/status")
def status(req, resp):
    yield from picoweb.start_response(resp)
    htmlFile = open('/templates/status.html', 'r')
    for line in htmlFile:
        yield from resp.awrite(line)
    yield from resp.aclose()

@app.route("/api/led")
def api_led(req, resp):
    if req.method == "POST":
        print("Test RGB LED")
        yield from picoweb.http_error(resp, "200") # success!
        yield from resp.aclose()
        led.Error()
    else:
        yield from picoweb.http_error(resp, "405") 
        yield from resp.aclose()


@app.route("/api/speaker")
def api_speaker(req, resp):
    if req.method == "POST":
        print("Test Piezo Speaker")
        yield from picoweb.http_error(resp, "200") # success!
        yield from resp.aclose()
        speaker.PlayFinished()
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

app.run(debug=True, port=80, host=wifi.ip[0])
