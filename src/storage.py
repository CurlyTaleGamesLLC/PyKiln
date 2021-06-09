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

    # sdPath="/sd" <- might need to remove trailing slash
    def __init__(self, sdPath="/sd/", maxLogs=5):
        self.sdPath = sdPath
        self.maxLogs = maxLogs
        self.line = ""
        self.logFile = None
        self.sdcard = None
        print(sdPath)  

    def Connect(self, slot=2):
        self.sdcard = machine.SDCard(slot=slot)
        uos.mount(self.sdcard, self.sdPath)
        print(uos.listdir(self.sdPath))
        uos.chdir(self.sdPath)
        # logLength = len(uos.listdir(self.sdPath))

    # this isn't currently working
    def Disconnect(self):
        uos.chdir('/')
        uos.umount(self.sdPath)

    # def LogList():

    #     with open("loglist.csv", 'w') as filetowrite:
    #         filetowrite.write('new content')


    #     line = ""
    #     # check if file exists
    #     if "loglist.csv" in uos.listdir('/sd'):
    #         # log file exists, append to it
    #         append_write = 'a'
    #         line += ","
    #         file1 = open('/sd/loglist.csv')
    #         # file1lines = file1.readlines()
    #         # file1.read()
    #         logFileData = file1.readline()
    #         print(logFileData)
    #         logCounts = logFileData.split(",")
    #         logCountLength = len(logCounts)
    #         print(logCounts)
    #         line += str(int(logCounts[logCountLength - 1]) + 1)

    #     else:
    #         append_write = 'w' # write new file
    #         line += str(1)

        
    #     logFile = open("/sd/loglist.csv", append_write)
    #     logFile.write(line)
    #     logFile.close()

    def Log(self, filename, logData):
        """
        Add to an existing firing log, or create a new one.
        Requires the name of the CSV file to write to
        Requires an array of temperatures, the first one is the target temperature
        """
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

    def Read(self, filename):
        # uos.chdir(self.sdPath)
        # Reads Each Line
        self.line = ""
        for line in open(filename):
            self.line += line
        print(self.line)

    def DeleteOldestLog(self):
        logLength3 = len(uos.listdir(self.sdPath))
        if logLength3 > 8:
            uos.remove()

    def DeleteAll(self):
        uos.chdir(self.sdPath)
        logFiles = uos.listdir()
        logLength2 = len(logFiles)
        for i in range(logLength2):
            if logFiles[i] != 'System Volume Information':
                uos.remove(logFiles[i])