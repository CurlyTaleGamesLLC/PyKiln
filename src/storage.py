import uos
import machine
# from micropython import const

# sck = 18
# cs = 5
# miso = 19
# mosi = 23

# log file names
# log_2021-6-6_13-45-00_name of firing schedule

# get the list of files in the directory
# if it's above 1000
# sort the list of files, and delete the oldest one (the first one)

# _newLine = const("\r\n")

class logging:
    """
    Logging Kiln firing data to a microSD card.
    """

    _newLine = "\r\n"

    def __init__(self, sdPath="/sd/", maxLogs=5):
        self.sdPath = sdPath
        self.root = "/"
        self.maxLogs = maxLogs
        self.line = ""
        self.logFile = None
        self.sdcard = None
        self.connected = False
        print(sdPath)  

    def Connect(self, slot=2):
        try:
            self.sdcard = machine.SDCard(slot=slot)
            uos.mount(self.sdcard, self.sdPath)
            print(uos.listdir(self.sdPath))
            uos.chdir(self.sdPath)
            self.connected = True
            # logLength = len(uos.listdir(self.sdPath))
        except:
            print("Could not connect to SD card")
            self.connected = False

        

    # this isn't currently working
    def Disconnect(self):
        if self.connected:
            uos.chdir(self.root)
            uos.umount(self.sdPath)

    def LogList(self):
        # this could probably be cached, and updated only when a new log is created

        # Don't get the lst of log files if the SD card isn't connected
        if not self.connected:
            return
        
        uos.chdir(self.sdPath)
        logfiles = uos.listdir(self.sdPath)
        for log in logfiles:
            print(log)
            if not log.endswith(".csv"):
                logfiles.remove(log)

        uos.chdir(self.root)
        
        return logfiles

    def Log(self, filename, logData):
        """
        Add to an existing firing log, or create a new one.
        Requires the name of the CSV file to write to
        Requires an array of temperatures, the first one is the target temperature
        """

        # Don't log anything if the SD card isn't connected
        if not self.connected:
            # print("Not Connected to SD card, can't log")
            return

        # Check if file exists or not
        uos.chdir(self.sdPath)
        self.line = ""
        if filename in uos.listdir(self.sdPath):
            self.line += self._newLine
        
        # Convert the array of temperatures to CSV format 
        for i in range(len(logData)):
            self.line += str(logData[i])
            if i < len(logData) - 1:
                self.line += ","
        print(self.line)

        self.logFile = open(filename, 'a')
        self.logFile.write(self.line)
        self.logFile.close()
        uos.chdir(self.root)

    def Read(self, filename):
        # Don't read anything if the SD card isn't connected
        if not self.connected:
            return

        uos.chdir(self.sdPath)
        # Reads Each Line
        self.line = ""
        for line in open(filename):
            self.line += line
        print(self.line)
        uos.chdir(self.root)

    def DeleteOldestLog(self):
        # Don't delete anything if the SD card isn't connected
        if not self.connected:
            return
        
        logLength3 = len(uos.listdir(self.sdPath))
        if logLength3 > 8:
            uos.remove()

    def DeleteAll(self):
        # Don't delete anything if the SD card isn't connected
        if not self.connected:
            return

        uos.chdir(self.sdPath)
        logFiles = uos.listdir()
        logLength2 = len(logFiles)

        for i in range(logLength2):
            if not logFiles[i].endswith(".csv"):
                # if logFiles[i] != 'System Volume Information':
                rm(logFiles[i])
                # try:
                #     uos.remove(logFiles[i])
                # except:
                #     uos.rmdir(logFiles[i])
        
        uos.chdir(self.root)

def rm(d):  # Remove file or tree
    try:
        if uos.stat(d)[0] & 0x4000:  # Dir
            for f in uos.ilistdir(d):
                if f[0] not in ('.', '..'):
                    rm("/".join((d, f[0])))  # File or Dir
            uos.rmdir(d)
        else:  # File
            uos.remove(d)
    except:
        print("rm of '%s' failed" % d)