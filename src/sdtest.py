import uos
import machine

# sck = 18
# cs = 5
# miso = 19
# mosi = 23

# log file names
# log_2021-6-6_13-45-00_name of firing schedule

# get the list of files in the directory
# if it's above 1000
# sort the list of files, and delete the oldest one (the first one)



def LogList():

    with open("loglist.csv", 'w') as filetowrite:
        filetowrite.write('new content')


    line = ""
    # check if file exists
    if "loglist.csv" in uos.listdir('/sd'):
        # log file exists, append to it
        append_write = 'a'
        line += ","
        file1 = open('/sd/loglist.csv')
        # file1lines = file1.readlines()
        # file1.read()
        logFileData = file1.readline()
        print(logFileData)
        logCounts = logFileData.split(",")
        logCountLength = len(logCounts)
        print(logCounts)
        line += str(int(logCounts[logCountLength - 1]) + 1)

    else:
        append_write = 'w' # write new file
        line += str(1)

    
    logFile = open("/sd/loglist.csv", append_write)
    logFile.write(line)
    logFile.close()

def AddToLog(filename, logData):
    # Check if file exists or not
    line = ""
    if filename in uos.listdir('/sd'):
        append_write = 'a' # append mode
        line += "\r\n"
    else:
        append_write = 'w' # write new file
    
    length = len(logData)
    for i in range(length):
        # print(str(logData[i]))
        line += str(logData[i])
        if i < len(logData) - 1:
            line += ","
    print(line)

    logFile = open("/sd/" + filename, append_write)
    logFile.write(line)
    logFile.close()

def ReadLog(filename):
    # Reads whole file

    # Reads Each Line
    logData = ""
    for line in open("/sd/" + filename):
        # print(line)
        logData += line
    print(logData)

def DeleteOldestLog():
    logLength3 = len(uos.listdir('/sd'))
    if logLength3 > 8:
        uos.remove()

def DeleteAll():
    logFiles = uos.listdir('/sd')
    logLength2 = len(logFiles)
    for i in range(logLength2):
        if logFiles[i] != 'System Volume Information':
            uos.remove('/sd/' + logFiles[i])
        

def ZeroPad(value):
    stringValue = str(value)
    zeros = 8 - len(stringValue)
    for i in range(zeros):
        stringValue = "0" + stringValue
    return stringValue

# list_of_files = os.listdir('log')    

# if len(list_of_files) >= 25:
#     oldest_file = min(list_of_files, key=os.path.getctime)
#     os.remove(os.path.abspath(oldest_file))

uos.mount(machine.SDCard(slot=2), "/sd")

dirList = uos.listdir('/sd')
print(dirList)
print(sorted(dirList))

logLength = len(uos.listdir('/sd'))
maxLogs = 10


# print(ZeroPad(4))

testname = "2021-6-6_13-22-00_biscuit 04"
# testfilename = "log_" + ZeroPad(logLength) + ".csv"
testfilename = "log_" + testname + ".csv"
print(testfilename)

AddToLog(testfilename, [1,2,3])
AddToLog(testfilename, [4,5,6])
AddToLog(testfilename, [7,8,9])
AddToLog(testfilename, [10,11,12])

print(uos.listdir('/sd'))

ReadLog(testfilename)

# DeleteAll()

LogList()


uos.umount('/sd')

