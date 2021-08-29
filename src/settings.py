import uio
import ujson

class settings:

    def __init__(self):
        self.settingsPath = "settings.json"
        self.settingsFile = None
        self.data = None
        self.dataJSON = None
        self.LoadSettings()


    def LoadSettings(self):
        with uio.open(self.settingsPath) as fp:
            self.data = ujson.load(fp)
        self.dataJSON = ujson.dumps(self.data)
        print(self.dataJSON)

    
    def HasIP(self):
        return self.data["ip"] != ""

    def SetIP(self, ip):
        self.data["ip"] = ip
        self.WriteSettings()

    def IsConfigured(self):
        return self.data["configured"]

    def SetConfigured(self):
        self.data["configured"] = True
        self.WriteSettings()

    def WriteSettings(self):
        print("Writing Settings:")
        # Convert python object into JSON object
        self.dataJSON = ujson.dumps(self.data)

        # Overwrite the existing settings file with the new JSON data
        self.settingsFile = open(self.settingsPath, 'w')
        self.settingsFile.write(self.dataJSON)
        self.settingsFile.close()

        
        # with open(self.settingsPath, 'w') as json_file:
        #     ujson.dump(self.data, json_file)

# def df():
#     s = uos.statvfs('//')
#     return ('{0} MB'.format((s[0]*s[3])/1048576))

# print("Filespace Available: " + df())