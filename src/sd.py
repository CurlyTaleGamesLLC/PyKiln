import storage

# An SD card is optional, but is required for logging

sd = storage.logging()

sd.Connect()

testname = "fart.csv"

sd.Log(testname, [1,2,3,7])
sd.Log(testname, [2,2,3,6])
sd.Log(testname, [3,2,3,5])
sd.Log(testname, [4,2,3,4])
sd.Log(testname, [5,2,3,3])
sd.Log(testname, [6,2,3,2])
sd.Log(testname, [7,2,3,1])

sd.Read(testname)

# sd.DeleteAll()

# sd.Disconnect()

# testname = "2021-6-6_13-22-00_biscuit 04"
# testfilename = "log_" + testname + ".csv"
# print(testfilename)

# # print(uos.listdir('/sd'))