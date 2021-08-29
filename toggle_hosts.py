#!/usr/bin/python
#coding:utf8

# This script will Enable/Disable the line in the hosts file for pykiln.com so you can more easily test PyKiln locally

from sys import platform

# The hostname that will be toggled
hostName = "pykiln.com"

# PyKiln line in host file
newName = "127.0.0.1 " + hostName + "\n"

# Based on the OS get the path to the hosts file
hostFilePath = ""
if platform == "linux" or platform == "linux2":
    # linux
    hostFilePath = "/etc/hosts"
elif platform == "darwin":
    # OS X
    hostFilePath = "/private/etc/hosts"
elif platform == "win32":
    # Windows
    hostFilePath = "c:/windows/system32/drivers/etc/hosts"

# Empty array to store the final host file data
newHostsFile = [] 

# opens the host file
hostsFile = open(hostFilePath).readlines()

# Enables/Disabled the hostname if it's in the hosts file
for line in hostsFile:
    if hostName in line:
        print("Found Host:")
        if "#" in line:
            print("Enabling " + newName)
            newHostsFile.append(newName)
        else:
            print("Disabling " + newName)
            newHostsFile.append("#" + newName)  
    else:
        newHostsFile.append(line)

# Check to see if the hostname exists in the file
hostNameExists = False
for line in newHostsFile:
    if hostName in line:
        hostNameExists = True

# If the hostname isn't in the file add it
if not hostNameExists:
    print("Adding Hostname:")
    print(newName)
    newHostsFile.append(newName)

print("Updated Hosts File:")
print(newHostsFile)

# Rewrite the contents of the hosts file.
updatedFile = open(hostFilePath, 'w')
updatedFile.writelines(newHostsFile)
updatedFile.close()
