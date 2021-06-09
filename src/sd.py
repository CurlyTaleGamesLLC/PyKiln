import storage

sd = storage.logging()

sd.Connect()

sd.Log("fart.csv", [1,2,3,7])
sd.Log("fart.csv", [2,2,3,6])
sd.Log("fart.csv", [3,2,3,5])
sd.Log("fart.csv", [4,2,3,4])
sd.Log("fart.csv", [5,2,3,3])
sd.Log("fart.csv", [6,2,3,2])
sd.Log("fart.csv", [7,2,3,1])

sd.Read("fart.csv")

# sd.DeleteAll()

# sd.Disconnect()

# testname = "2021-6-6_13-22-00_biscuit 04"
# # testfilename = "log_" + ZeroPad(logLength) + ".csv"
# testfilename = "log_" + testname + ".csv"
# print(testfilename)

# AddToLog(testfilename, [1,2,3])
# AddToLog(testfilename, [4,5,6])
# AddToLog(testfilename, [7,8,9])
# AddToLog(testfilename, [10,11,12])

# # print(uos.listdir('/sd'))

# ReadLog(testfilename)