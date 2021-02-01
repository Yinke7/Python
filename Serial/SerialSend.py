#!/bin/python
# -*- coding:utf-8 -*-

import serial
import sys
import threading
import getopt


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
        print("Starting " + self.name)

        if "read" == self.name:
            SerialRead()
        elif "write" == self.name:
            SerialWrite()
        else:
            pass
        print("Exiting " + self.name)


def Run(port, baud):

    # 设置串口端口号，波特率 115200bps，超时时间 0.1s
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

if __name__ == "__main__":
    port = ""
    baud = 115200
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:b:", ["help", "port=", "baud="])
    except getopt.GetoptError:
        print("usage: -p<port> -b<baud>")
        sys.exit(2)
    if not opts:
        print("usage: -p<port> -b<baud>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("usage: -p<port> -b<baud>")
            sys.exit(2)
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-b", "--baud"):
            baud = arg
        else:
            print("usage: -p<port> -b<baud>")
            sys.exit(2)
    print("port: %s" % port)
    print("baud: %s" % baud)
    Run(port, baud)



