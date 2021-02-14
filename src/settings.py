import uio
import ujson

with uio.open("settings.json") as fp:
    data = ujson.load(fp)

print(ujson.dumps(data))

# def hasWiFiNetwork():
#     global data
#     return data["network"]["wifi"] != ""

# def Connect(wifi, password, host):
#     global data
#     data["network"]["wifi"] = wifi
#     data["network"]["password"] = password
#     data["network"]["host"] = host
#     data["configured"] = False

#     WriteSettings()
# 
    # with open('settings.json', 'w') as json_file:
    #     ujson.dump(data, json_file)

def df():
    s = uos.statvfs('//')
    return ('{0} MB'.format((s[0]*s[3])/1048576))
    
print("Filespace Available: " + df())

def hasIP():
    global data
    return data["ip"] != ""

# def GetIP():
#     global data
#     return data["ip"]

def SetIP(ip):
    global data
    data["ip"] = ip
    WriteSettings()

# def isConfigured():
#     global data
#     return data["configured"]

# def SetConfigured():
#     global data
#     data["configured"] = True
#     WriteSettings()

def WriteSettings():
    global data
    with open('settings.json', 'w') as json_file:
        ujson.dump(data, json_file)