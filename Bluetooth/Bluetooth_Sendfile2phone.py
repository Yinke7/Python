#!/bin/python
# -*- coding:utf-8 -*-

import bluetooth
import os
import sys
from PyOBEX.client import Client


# Scan addresses of the nearby devices and find their servers
def Bluetooth_Scan():
    print("Scan devices nearby")
    devices = bluetooth.discover_devices(lookup_names=True)
    if len(devices):
        print("Found devices")
        return devices
    else:
        print("Found none devices")
        
        return
    
# Send file to the phone
def RFCOMM_Sendfile(address, fname="test.txt", fdata=b'Hello world\n'):

    print("Searching for OBEX service on %s" % address)

    # Use the server named "OBEX Object Push" to send file
    service_matches = bluetooth.find_service(name="OBEX Object Push", address=address)
    if len(service_matches) == 0:
        print("Couldn't find the service")
        sys.exit(0)

    match = service_matches[0]
    name = match["name"]
    host = match["host"]
    port = match["port"]


    print("Service Name: %s" % match["name"])
    print("    Host:        %s" % match["host"])
    print("    Description: %s" % match["description"])
    print("    Provided By: %s" % match["provider"])
    print("    Protocol:    %s" % match["protocol"])
    print("    channel/PSM: %s" % match["port"])
    print("    svc classes: %s " % match["service-classes"])
    print("    profiles:    %s " % match["profiles"])
    print("    service id:  %s " % match["service-id"])

    print("Connecting to \"%s\" on %s" % (name, host))
    client = Client(host, port)
    client.connect()

    # The parameter [file_data] must be bytes type like [b'****'],otherwise there will be some error occur in Python3
    client.put(name=fname, file_data=fdata)
    client.disconnect()

    return

def Test(devicename):

    specdevfound = False
    devices = Bluetooth_Scan()
    if not len(devices):
        return
    for addr, name in devices:
        print("%s - %s" % (name, addr))
        if devicename == name:
            print("Lucky! Found device to send file")
            RFCOMM_Sendfile(address=addr, fdata=b'Hello Bluetooth\n')
            specdevfound = True
    if not specdevfound:
        print("Not found device wanna")
        
    return

if __name__ == "__main__":
    print("Your Bluetooth name is [%s]" % sys.argv[1])
    Test(devicename=sys.argv[1])

