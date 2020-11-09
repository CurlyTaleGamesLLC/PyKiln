# main.py
import gc
import uos
import ujson
import machine
import utime
import settings

# Connect to WiFi
import wifiConnect
wifiConnect.setup()

# Install Dependencies
import install

import ulogging
import utemplate
import uasyncio
import picoweb

# Custom Libraries
import temperature
import speaker
import led


def df():
    s = uos.statvfs('//')
    return ('{0} MB'.format((s[0]*s[3])/1048576))

print("Filespace Available: " + df())

app = picoweb.WebApp(__name__)

@app.route("/")
def index(req, resp):
    if settings.isConfigured():
        # redirect to "/"
        headers = {"Location": "http://localhost/index.html?ip=" + wifiConnect.ip[0]}
        yield from picoweb.start_response(resp, status="303", headers=headers)
    else:
        yield from picoweb.start_response(resp)
        htmlFile = open('/templates/setup.html', 'r')
        for line in htmlFile:
            yield from resp.awrite(line)
        yield from resp.aclose()


@app.route("/status")
def status(req, resp):
    yield from picoweb.start_response(resp)
    htmlFile = open('/templates/status.html', 'r')
    for line in htmlFile:
        yield from resp.awrite(line)
    yield from resp.aclose()

@app.route("/api/configure")
def api_configure(req, resp):
    if req.method == "POST":
        print("Configure PyKiln")
        yield from picoweb.http_error(resp, "200") # success!
        yield from req.read_form_data()
        yield from resp.aclose()
        print(req)
        print(req.form)
        print(req.form["wifi"])
        print(req.form["password"])
        print(req.form["host"])
        settings.Connect(req.form["wifi"], req.form["password"], req.form["host"])
        print(settings.data)

        uasyncio.run(reboot_delay())       
    else:
        yield from picoweb.http_error(resp, "405")
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

@app.route("/api/ip")
def api_ip(req, resp):
    yield from picoweb.start_response(resp, content_type="application/json")
    jsonData = {"ip":settings.GetIP()}
    encoded = ujson.dumps(jsonData)
    yield from resp.awrite(encoded)
    yield from resp.aclose()
    if settings.hasIP:
        print("User knows new IP, Reboot! " + settings.GetIP())
        utime.sleep(5)
        machine.reset()

    
async def reboot_delay():
    await uasyncio.sleep(4)
    print('REBOOT!')
    await uasyncio.sleep(4)
    machine.reset()
    # reboot

app.run(debug=True, port=80, host=wifiConnect.ip[0])
