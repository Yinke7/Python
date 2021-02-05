#!/bin/python
# -*- coding:utf-8 -*-

import serial
import sys
import threading
import getopt
import os
import subprocess

SERIAL = serial.Serial()

# 继承父类threading.Thread
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        print("%s ready" % self.name)

        if "read" == self.name:
            SerialRead()
        elif "write" == self.name:
            SerialWrite()
        else:
            pass
        print("Exiting " + self.name)


def Run(baud):
    # set the port and baud for serial
    port = ""
    devices = GetSerialDevlist()
    if 1 != len(devices):
        print("There're %d ports available:" % len(devices), end="")
        for dev in devices:
            print("[%s], " % dev, end="")
        devsel = input("please select one of them\n>>>")
        print(devsel)
        for dev in devices:
            if devsel == dev:
                port = dev
    else:
        port = devices[0]
    global SERIAL
    SERIAL = serial.Serial(port=port, baudrate=baud)

    read = myThread(1, "read", 1)
    write = myThread(2, "write", 2)

    try:
        read.start()
        write.start()
    except Exception:
        SERIAL.close()
        print("serial closed")
    return

def SerialRead():
    while True:
        data = SERIAL.read()
        if data:
            print(data.decode("utf-8"), end="")

def SerialWrite():
    while True:
        line = sys.stdin.readline()
        datalist = line.split("\n")
        datalist = datalist[0].split(" ")
        try:
            for data in datalist:
                SERIAL.write(bytes.fromhex(data))
        except ValueError:
            print("ValueError: Hex string must be similar to 'AB', 'ABCD', 'AB CD'...")

def GetSerialDevlist():
    try:
        res = subprocess.check_output("ls /dev/tty* | grep ttyUSB*", shell=True)
        res = str(res, encoding="utf-8")
        devlist = res.split()
        return devlist
    except Exception as e:
        print(e)

if __name__ == "__main__":
    baud = 0
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hb:", ["help", "baud="])
    except getopt.GetoptError:
        print("usage: -b<baud>")
        sys.exit(2)
    if not opts:
        print("usage: -b<baud>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("usage: -b<baud>")
            sys.exit(2)
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-b", "--baud"):
            baud = arg
        else:
            print("usage: -b<baud>")
            sys.exit(2)
    if not baud:
        print("baud is not Invalid")
    else:
        print("baud: %s" % baud)
        # 运行脚本
        Run(baud)

